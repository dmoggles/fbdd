from typing import List
from fbdd.definitions.core import DataAttribute
from fbdd.operations.filter import apply_filter
from fbdd.operations import filter_objects as filters
from fbdd.operations.filter_objects import Filter
from fbdd.definitions import fbref_columns as fc
from fbdd.operations.aggregations import aggregate_by
from scipy.optimize import least_squares
from scipy import stats
from matplotlib import pyplot as plt
import numpy as np
from highlight_text import ax_text
import pandas as pd

VIOLIN_PLOT_SECTION_COLOURS = ["#0061FF", "#4061D8", "#8061B0", "#BF6189", "#FF6161"]
IN_OPACITY = 1
OUT_OPACITY = 0.3
SMALL_SCALE = 0.75


def prep_data(data, player, year, stats_to_use):
    player_league = (
        data.pipe(
            apply_filter,
            [Filter(fc.PLAYER, player, filters.EQ), Filter(fc.YEAR, year, filters.EQ)],
        )
        .col(fc.COMPETITION)
        .item()
    )

    player_league_data = data.pipe(
        apply_filter,
        [
            Filter(fc.COMPETITION, player_league, filters.EQ),
            Filter(fc.YEAR, year, filters.EQ),
        ],
    ).pipe(aggregate_by, [fc.PLAYER])[stats_to_use]

    return player_league_data


def get_layout(stats_to_use, n_cols):
    if len(stats_to_use) % n_cols > 0:
        return (int(len(stats_to_use) / n_cols + 1), n_cols)
    else:
        return (int(len(stats_to_use) / n_cols), n_cols)


def get_quantiles(kde, league_data, stat):
    return [
        least_squares(
            lambda x: kde.integrate_box_1d(0, x) / kde.integrate_box_1d(0, league_data.col(stat).max()) - 0.2 * (i + 1),
            league_data.col(stat).min(),
            gtol=1e-15,
            jac="3-point",
        ).x[0]
        for i in range(0, 4)
    ]


def get_player_stat_line(data, player, stat):
    return data.pipe(apply_filter, [Filter(fc.PLAYER, player, filters.EQ)]).col(stat).item()


def draw_filled_curve(ax: plt.Axes, kde, min_v, max_v, y_mult, color, opacity):
    xs = np.linspace(min_v, max_v, 30)
    ys = kde.evaluate(xs) * y_mult

    ax.plot(xs, ys, c=color, alpha=opacity, zorder=1)
    ax.fill_between(xs, ys, 0, alpha=opacity - 0.05, color=color, zorder=1)


def estimate_maxima(data):
    kde = stats.gaussian_kde(data)
    no_samples = 100
    samples = np.linspace(0, data.max(), no_samples)
    probs = kde.evaluate(samples)
    return probs.max()


def draw_half_violin(ax: plt.Axes, data, d, quantiles, stat, player_statline, kde, max_stat):

    for i in range(5):
        if i == 0:
            min_v = 0
        else:
            min_v = quantiles[i - 1]

        if i < 4:
            max_v = quantiles[i]
        else:
            max_v = max_stat

        if player_statline >= min_v and player_statline < max_v:
            draw_filled_curve(
                ax,
                kde,
                min_v,
                player_statline,
                d,
                VIOLIN_PLOT_SECTION_COLOURS[i],
                IN_OPACITY,
            )
            draw_filled_curve(
                ax,
                kde,
                player_statline,
                max_v,
                d,
                VIOLIN_PLOT_SECTION_COLOURS[i],
                OUT_OPACITY,
            )
        else:
            if player_statline < min_v:
                opacity = OUT_OPACITY
            else:
                opacity = IN_OPACITY
            draw_filled_curve(ax, kde, min_v, max_v, d, VIOLIN_PLOT_SECTION_COLOURS[i], opacity)


def plot_single_violin(
    ax,
    data,
    player1,
    player2,
    player1_year,
    player2_year,
    stat,
    player_highlight_colors,
):
    players = [player1, player2]
    years = [player1_year, player2_year]
    player_league_data = [
        prep_data(data, players[0], years[0], stat),
        prep_data(data, players[1], years[1], stat),
    ]
    kdes = [
        stats.gaussian_kde(player_league_data[0].col(stat).fillna(0)),
        stats.gaussian_kde(player_league_data[1].col(stat).fillna(0)),
    ]
    quantiles = [
        get_quantiles(kdes[0], player_league_data[0], stat),
        get_quantiles(kdes[1], player_league_data[1], stat),
    ]
    player_stat_line = [
        get_player_stat_line(player_league_data[0], players[0], stat),
        get_player_stat_line(player_league_data[1], players[1], stat),
    ]
    max_cdfs = [
        kdes[0].integrate_box_1d(0, player_league_data[0].col(stat).max()),
        kdes[0].integrate_box_1d(0, player_league_data[1].col(stat).max()),
    ]
    max_stat = max(player_league_data[0].col(stat).max(), player_league_data[1].col(stat).max())
    max_kde = max(
        estimate_maxima(player_league_data[0].col(stat)),
        estimate_maxima(player_league_data[1].col(stat)),
    )
    for i, d in enumerate([1, -1]):
        draw_half_violin(
            ax,
            player_league_data[i],
            d,
            quantiles[i],
            stat,
            player_stat_line[i],
            kdes[i],
            max_stat,
        )
    # ax.plot([0,max_stat], [0,0],  zorder=1)
    ax.hlines(0, 0, max_stat, color="black")

    player_ys = [
        kdes[0].evaluate(player_stat_line[0]),
        -kdes[1].evaluate(player_stat_line[1]),
    ]
    for i in range(2):
        ax.scatter(
            [player_stat_line[i]],
            [player_ys[i]],
            color=player_highlight_colors[i],
            zorder=2,
            s=60,
        )
        ax.vlines(
            player_stat_line[i],
            0,
            player_ys[i],
            color=player_highlight_colors[i],
            zorder=2,
            linewidths=3,
        )
        # ax.annotate(f"{player_stat_line[i]}", xy=(player_stat_line[i], player_ys[i]), xytext=(max_stat*0.95,max_kde*1.1*(1-i*2)), arrowprops=dict(facecolor=player_highlight_colors[i], shrink=0.05))
        pct = kdes[i].integrate_box_1d(0, player_stat_line[i])
        if i == 0:

            text = f"{players[i]}-{years[i]}: {player_stat_line[i]:.2f}\npct: {pct*100:.2f}%"
            va = "top"
        else:
            text = f"pct: {pct*100:.2f}%\n{players[i]}-{years[i]}: {player_stat_line[i]:.2f}"
            va = "bottom"
        ax.text(
            max_stat * 0.99,
            max_kde * 1.18 * (1 - i * 2),
            text,
            ha="right",
            va=va,
            color=player_highlight_colors[i],
        )

    ax.get_yaxis().set_visible(False)
    ax.set_xlim(left=0, right=max_stat)
    ax.set_ylim(-max_kde * 1.2, max_kde * 1.2)
    ax.tick_params(axis="both", which="both", length=0)
    ax.title.set_text(stat.N)


def plot_violin(
    data: pd.DataFrame,
    player1: str,
    player2: str,
    player1_year: int,
    player2_year: int,
    stats_to_use: List[DataAttribute],
    player_highlight_colors: List[str] = ["darkgreen", "olive"],
    small: bool = False,
    n_cols: int = 2,
) -> plt.Figure:
    """
    Plot a violin plot distribution comparison for a two players for a given list of stats

    Args:
        data (pd.DataFrame): Player data dataframe.  Must be aggregated by player and year already
        player1 (str): player 1 name
        player2 (str): patient 2 name
        player1_year (int): player 1 season year
        player2_year (int): player 2 season year
        stats_to_use (List[DataAttribute]): list of attributes to compare
        player_highlight_colors (List[str], optional): Names of colours used to highlight players. Defaults to ['darkgreen', 'olive'].
        small (bool, optional): Make a small chart.  Does not reliably work. Defaults to False.
        n_cols (int, optional): Number of columns in the layout. Defaults to 2.
    """
    plt.rcParams.update({"figure.autolayout": True})
    rows, cols = get_layout(stats_to_use, n_cols)
    main = np.arange(rows * cols).reshape(rows, cols)

    layout = np.concatenate([np.tile(["title"], (1, cols)), main, np.tile(["annot"], (1, cols))])

    fig, axes = plt.subplot_mosaic(
        layout,
        figsize=(
            5 * cols * (SMALL_SCALE if small else 1),
            (1 + 2.5 * rows) * (SMALL_SCALE if small else 1),
        ),
        gridspec_kw={"height_ratios": [0.025] + [0.95 / rows] * rows + [0.025]},
    )
    axes_list = [v for k, v in axes.items() if k not in ["annot", "title"]]
    for ax, stat in zip(axes_list, stats_to_use):
        plot_single_violin(
            ax,
            data,
            player1,
            player2,
            player1_year,
            player2_year,
            stat,
            player_highlight_colors,
        )
    for ax in axes_list[len(stats_to_use) :]:
        ax.axis("off")

    title = f"<{player1} {player1_year}> vs <{player2} {player2_year}>"
    ax_text(
        0.5,
        0.5,
        title,
        highlight_textprops=[
            {"color": player_highlight_colors[0]},
            {"color": player_highlight_colors[1]},
        ],
        size=16 * (SMALL_SCALE if small else 1),
        fig=fig,
        textalign="center",
        ha="center",
        va="center",
        ax=axes["title"],
    )

    ax_text(
        0.05,
        0.5,
        "@ChicagoDmitry, data from fbref",
        size=10 * (SMALL_SCALE if small else 1),
        fig=fig,
        textalign="center",
        ha="center",
        va="center",
        ax=axes["annot"],
        alpha=0.5,
    )
    axes["title"].axis("off")
    axes["annot"].axis("off")
    fig.tight_layout()
    return fig
