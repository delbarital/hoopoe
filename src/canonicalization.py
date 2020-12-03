# string to lowercaes, remove dashse and double spaces
def prepare_names(df):
    df = df.str.lower()
    df = df.str.replace('-',' ')
    df = df.str.replace('  ',' ')
    return df

def remove_plus(df):
    df = df.replace('+', '')
    return df