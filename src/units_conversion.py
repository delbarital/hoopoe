# Temprature units
def f_to_c(df,source_data_name):
    df[source_data_name] = (df[source_data_name] - 32) * 5/9
    return df

def c_to_f(df,source_data_name):
    df[source_data_name] = df[source_data_name]* 5/9 + 32
    return df  

def c_to_k(df,source_data_name):
    df[source_data_name] = df[source_data_name] + 273.15
    return df

def k_to_c(df,source_data_name):
    df[source_data_name] = df[source_data_name] - 273.15
    return df

def k_to_f(df,source_data_name):
    df[source_data_name] = (df[source_data_name] - 273.15) * 9/5 + 32
    return df

def f_to_k(df,source_data_name):
    df[source_data_name] = (df[source_data_name] - 32) * 5/9 + 273.15
    return df