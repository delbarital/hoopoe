def remove_double_spaces_and_dashes(df):
    df = df.str.lower()
    df = df.str.replace('-',' ')
    df = df.str.replace('  ',' ')
    return df

def remove_plus(df):
    df = df.replace('+', '')
    return df
