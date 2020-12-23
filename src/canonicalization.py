# string to lowercaes, remove dashse, dots and double spaces
def prepare_names(df):
    df = df.str.lower()
    df = df.str.replace('-',' ')
    df = df.str.replace('  ',' ')
    df = df.str.replace('.',' ')
    return df

def prepare_abbr(df):
    df = prepare_names(df)
    df = df.str.replace(' ', '')
    return df

def remove_plus(df):
    df = df.replace('+', '')
    return df