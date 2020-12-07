import us_states
import international_phone_prefixes
import units_conversion
import canonicalization

import pandas as pd

def enrich(data=None, source_data_name=None, source_data_type=None, target_data_type=None):
    if data == None:
        # TODO: Make sure this is the right exception for this situation.
        raise ValueError("No data was provided.")
    if source_data_name == None and source_data_type == None:
        # TODO: Make sure this is the right exception for this situation.
        raise ValueError("No source_data_name or source_data_type were provided.")
    if source_data_name == None:
        source_data_name = source_data_type
    if source_data_type == None:
        source_data_type = source_data_name
    if target_data_type == None:
        raise ValueError("No target_data_type were provided.")
 

    if isinstance(data, str) or isinstance(data, int):
        return str_enrich(str=data, source_data_type=source_data_type, target_data_type=target_data_type)
    if isinstance(data,  pd.DataFrame):
        if source_data_name==None:
            source_data_name = source_data_type
        return df_enrich(data, source_data_name, source_data_type, target_data_type)
    
def str_enrich(str, source_data_type, target_data_type):
    # We implement this function using the df_enrich. We basically send the string as a df to df_enrich
    # and later extract the answer from the df as a string and return it. 
    result_df = df_enrich(pd.DataFrame.from_dict({source_data_type: [str]}), source_data_name=source_data_type, source_data_type=source_data_type, target_data_type=target_data_type)
    result = result_df[target_data_type][0]
    if result == str:
        raise KeyError(f'The key {str} does not exist')
    return result

def df_enrich(df, source_data_name, source_data_type, target_data_type):
    # We copy the content of the original data to a new column and later replace the copied data
    # with the translated data.
    df[target_data_type] = df[source_data_name]
    if source_data_type == 'us_state_name_abbr' or source_data_type == 'us_state_name_full':
        df[target_data_type] = canonicalization.prepare_names(df[target_data_type])
    if source_data_type == 'us_state_name_abbr' and target_data_type == 'us_state_name_full':
        df = us_states.us_state_abbr_to_state_name(df, target_data_type)
    if source_data_type == 'us_state_name_full' and target_data_type == 'us_state_name_abbr':
        df = us_states.us_state_full_name_to_state_abbr(df, target_data_type)
    if source_data_type == 'us_state_name_full' and target_data_type == 'us_state_population':
        df = us_states.us_state_full_name_to_population(df, target_data_type)
    if source_data_type == 'us_state_name_full' and target_data_type == 'us_state_capital_city':
        df = us_states.us_state_full_name_to_capital_city(df, target_data_type)
    if source_data_type == 'us_state_name_full' and target_data_type == 'us_state_area_rank':
        df = us_states.us_state_full_name_to_area_rank(df, target_data_type)
    if source_data_type == 'us_capital_city_name' and target_data_type == 'us_capital_city_population':
        df = us_states.us_capital_city_population_2019(df, target_data_type)
    if source_data_type == 'us_capital_city_name' and target_data_type == 'us_capital_city_population_msa':
        df = us_states.us_capital_city_population_2019_msa(df, target_data_type)
    if source_data_type == 'us_capital_city_name' and target_data_type == 'us_capital_city_population_csa':
        df = us_states.us_capital_city_population_2019_csa(df, target_data_type)

    if source_data_type == 'int_phone_prefix' and target_data_type == 'country_name':
        df[target_data_type] = canonicalization.remove_plus(df[target_data_type])
        df = international_phone_prefixes.international_phone_prefixes_to_country(df, target_data_type)

    if source_data_type == 'celsius' and target_data_type == 'farenheit':
        df = units_conversion.c_to_f(df, target_data_type)
    if source_data_type == 'celsius' and target_data_type == 'kelvin':
        df = units_conversion.c_to_k(df, target_data_type)
    if source_data_type == 'farenheit' and target_data_type == 'celsius':
        df = units_conversion.f_to_c(df, target_data_type)    
    if source_data_type == 'farenheit' and target_data_type == 'kelvin':
        df = units_conversion.f_to_k(df, target_data_type)    
    if source_data_type == 'kelvin' and target_data_type == 'celsius':
        df = units_conversion.k_to_c(df, target_data_type)    
    if source_data_type == 'kelvin' and target_data_type == 'farenheit':
        df = units_conversion.k_to_f(df, target_data_type)    


    return df