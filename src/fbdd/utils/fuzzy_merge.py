from fuzzywuzzy import process
import pandas as pd

def fuzzy_merge(df_1, df_2, key1, key2, threshold=90, limit=2):
    """
    :param df_1: the left table to join
    :param df_2: the right table to join
    :param key1: key column of the left table
    :param key2: key column of the right table
    :param threshold: how close the matches should be to return a match, based on Levenshtein distance
    :param limit: the amount of matches that will get returned, these are sorted high to low
    :return: dataframe with boths keys and matches
    """
    s = df_2[key2].tolist()
    
    m = df_1[key1].apply(lambda x: process.extract(x, s, limit=limit))    
    df_1[f'__fuzzy_{key2}'] = m
    
    m2 = df_1[f'__fuzzy_{key2}'].apply(lambda x: ', '.join([i[0] for i in x if i[1] >= threshold]))
    df_1[f'__fuzzy_{key2}'] = m2
    
    return df_1


def create_fuzzy_merge_reference_column(df1:pd.DataFrame, df2:pd.DataFrame, fuzzy_col1:str, fuzzy_col2:str, threshold=70, limit=1):
    """
    :param df1: the left table to join
    :param df2: the right table to join
    :param fuzzy_col1: key column of the left table
    :param fuzzy_col2: key column of the right table
    :param threshold: how close the matches should be to return a match, based on Levenshtein distance
    :param limit: the amount of matches that will get returned, these are sorted high to low
    :return: dataframe with boths keys and matches
    """
    df_ref = fuzzy_merge( df1.groupby(fuzzy_col1).first().reset_index()[[fuzzy_col1]], df2.groupby(fuzzy_col2).first().reset_index()[[fuzzy_col2]],fuzzy_col1,fuzzy_col2, threshold=threshold, limit=limit)
    df1[f'__fuzzy_{fuzzy_col2}']=pd.merge(df1, df_ref, how='left', left_on=fuzzy_col1, right_on=fuzzy_col1)[f'__fuzzy_{fuzzy_col2}']
    return df1

