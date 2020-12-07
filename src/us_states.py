def us_state_abbr_to_state_name(df, source_data_name):
    df = df
    state_abbr_to_fullname = {
        'al':	'alabama',
        'ak':	'alaska',
        'az':	'arizona',
        'ar':	'arkansas',
        'ca':	'california',
        'co':	'colorado',
        'ct':	'connecticut',
        'de':	'delaware',
        'fl':	'florida',
        'ga':	'georgia',
        'hi':	'hawaii',
        'id':	'idaho',
        'il':	'illinois',
        'in':	'indiana',
        'ia':	'iowa',
        'ks':	'kansas',
        'ky':	'kentucky',
        'la':	'louisiana',
        'me':	'maine',
        'md':	'maryland',
        'ma':	'massachusetts',
        'mi':	'michigan',
        'mn':	'minnesota',
        'ms':	'mississippi',
        'mo':	'missouri',
        'mt':	'montana',
        'ne':	'nebraska',
        'nv':	'nevada',
        'nh':	'new hampshire',
        'nj':	'new jersey',
        'nm':	'new mexico',
        'ny':	'new york',
        'nc':	'north carolina',
        'nd':	'north dakota',
        'oh':	'ohio',
        'ok':	'oklahoma',
        'or':	'oregon',
        'pa':	'pennsylvania',
        'ri':	'rhode island',
        'sc':	'south carolina',
        'sd':	'south dakota',
        'tn':	'tennessee',
        'tx':	'texas',
        'ut':	'utah',
        'vt':	'vermont',
        'va':	'virginia',
        'wa':	'washington',
        'wv':	'west virginia',
        'wi':	'wisconsin',
        'wy':	'wyoming',
        'as': 'american samoa',
        'dc': 'district of columbia',
        'fm': 'federated states of micronesia',
        'gu': 'guam',
        'mh': 'marshall island',
        'mp': 'northern mariana islands',
        'pw': 'palau',
        'pr': 'puerto rico',
        'vi': 'virgin islands'

    }
    df.replace({source_data_name: state_abbr_to_fullname}, inplace=True)
    return df

def us_state_full_name_to_state_abbr(df, source_data_name):
    df = df
    state_fullname_to_abbr = {
        'alabama':  'al',
        'alaska':   'ak',
        'arizona':	'az',
        'arkansas':	'ar',
        'california':	'ca',
        'colorado':	'co',
        'connecticut':	'ct',
        'delaware':	'de',
        'florida':	'fl',
        'georgia':	'ga',
        'hawaii':	'hi',
        'idaho':	'id',
        'illinois':	'il',
        'indiana':	'in',
        'iowa':	'ia',
        'kansas':	'ks',
        'kentucky':	'ky',
        'louisiana':	'la',
        'maine':	'me',
        'maryland':	'md',
        'massachusetts':	'ma',
        'michigan':	'mi',
        'minnesota':	'mn',
        'mississippi':	'ms',
        'missouri':	'mo',
        'montana':	'mt',
        'nebraska':	'ne',
        'nevada':	'nv',
        'new hampshire':	'nh',
        'new jersey':	'nj',
        'new mexico':	'nm',
        'new york':	'ny',
        'north carolina':	'nc',
        'north dakota':	'nd',
        'ohio':	'oh',
        'oklahoma':	'ok',
        'oregon':	'or',
        'pennsylvania':	'pa',
        'rhode island':	'ri',
        'south carolina':	'sc',
        'south dakota':	'sd',
        'tennessee':	'tn',
        'texas':	'tx',
        'utah':	'ut',
        'vermont':	'vt',
        'virginia':	'va',
        'washington':	'wa',
        'west virginia':	'wv',
        'wisconsin':	'wi',
        'wyoming':	'wy',
        'american samoa':	'as',
        'district of columbia': 'dc',
        'federated states of micronesia': 'fm',
        'guam': 'gu',
        'marshall island': 'mh',
        'northern mariana islands': 'mp', 
        'palau': 'pw',
        'puerto rico': 'pr',
        'virgin islands': 'vi' 
    }
    df.replace({source_data_name: state_fullname_to_abbr}, inplace=True)
    return df


def us_state_full_name_to_population(df, source_data_name):
    df = df
    state_full_name_to_population = {
        'california':	'39512223',
        'texas':	'28995881',
        'florida':	'21477737',
        'new york':	'19453561',
        'illinois':	'12671821',
        'pennsylvania':	'12801989',
        'ohio':	'11689100',
        'georgia':	'10617423',
        'north carolina':	'10488084',
        'michigan':	'9986857',
        'new jersey':	'8882190',
        'virginia':	'8535519',
        'washington':	'7614893',
        'arizona':	'7278717',
        'massachusetts':	'6949503',
        'tennessee':	'6833174',
        'indiana':	'6732219',
        'missouri':	'6137428',
        'maryland':	'6045680',
        'wisconsin':	'5822434',
        'colorado':	'5758736',
        'minnesota':	'5639632',
        'south carolina':	'5148714',
        'alabama':	'4903185',
        'louisiana':	'4648794',
        'kentucky':	'4467673',
        'oregon':	'4217737',
        'oklahoma':	'3956971',
        'connecticut':	'3565287',
        'utah':	'3205958',
        'iowa':	'3155070',
        'nevada':	'3080156',
        'arkansas':	'3017825',
        'mississippi':	'2976149',
        'kansas':	'2913314',
        'new mexico':	'2096829',
        'nebraska':	'1934408',
        'west virginia':	'1792147',
        'idaho':	'1787065',
        'hawaii':	'1415872',
        'new hampshire':	'1359711',
        'maine':	'1344212',
        'montana':	'1068778',
        'rhode island':	'1059361',
        'delaware':	'973764',
        'south dakota':	'884659',
        'north dakota':	'762062',
        'alaska':	'731545',
        'district of columbia':	'705749',
        'vermont':	'623989',
        'wyoming':	'578759'
    }
    df.replace({source_data_name: state_full_name_to_population}, inplace=True)
    return df

def us_state_full_name_to_area_rank(df, source_data_name):
    df = df
    state_full_name_to_area_rank = {
        'alaska':	'1',
        'texas':	'2',
        'california':	'3',
        'montana':	'4',
        'new mexico':	'5',
        'arizona':	'6',
        'nevada':	'7',
        'colorado':	'8',
        'oregon':	'9',
        'wyoming':	'10',
        'michigan':	'11',
        'minnesota':	'12',
        'utah':	'13',
        'idaho':	'14',
        'kansas':	'15',
        'nebraska':	'16',
        'south dakota':	'17',
        'washington':	'18',
        'north dakota':	'19',
        'oklahoma':	'20',
        'missouri':	'21',
        'florida':	'22',
        'wisconsin':	'23',
        'georgia':	'24',
        'illinois':	'25',
        'iowa':	'26',
        'new york':	'27',
        'north carolina':	'28',
        'arkansas':	'29',
        'alabama':	'30',
        'louisiana':	'31',
        'mississippi':	'32',
        'pennsylvania':	'33',
        'ohio':	'34',
        'virginia':	'35',
        'tennessee':	'36',
        'kentucky':	'37',
        'indiana':	'38',
        'maine':	'39',
        'south carolina':	'40',
        'west virginia':	'41',
        'maryland':	'42',
        'hawaii':	'43',
        'massachusetts':	'44',
        'vermont':	'45',
        'new hampshire':	'46',
        'new jersey':	'47',
        'connecticut':	'48',
        'delaware':	'49',
        'rhode island':	'50'
    }
    df.replace({source_data_name: state_full_name_to_area_rank}, inplace=True)
    return df

def us_state_full_name_to_capital_city(df, source_data_name):
    df = df
    state_fullname_to_capital_city_name = {
        'alabama':	'montgomery',
        'alaska':	'juneau',
        'arizona':	'phoenix',
        'arkansas':	'little Rock',
        'california':	'sacramento',
        'colorado':	'denver',
        'connecticut':	'hartford',
        'delaware':	'dover',
        'florida':	'tallahassee',
        'georgia':	'atlanta',
        'hawaii':	'honolulu',
        'idaho':	'boise',
        'illinois':	'springfield',
        'indiana':	'indianapolis',
        'iowa':	'des Moines',
        'kansas':	'topeka',
        'kentucky':	'frankfort',
        'louisiana':	'baton Rouge',
        'maine':	'augusta',
        'maryland':	'annapolis',
        'massachusetts':	'boston',
        'michigan':	'lansing',
        'minnesota':	'saint Paul',
        'mississippi':	'jackson',
        'missouri':	'jefferson City',
        'montana':	'helena',
        'nebraska':	'lincoln',
        'nevada':	'carson City',
        'new Hampshire':	'concord',
        'new Jersey':	'trenton',
        'new Mexico':	'santa Fe',
        'new York':	'albany',
        'north Carolina':	'raleigh',
        'north Dakota':	'bismarck',
        'ohio':	'columbus',
        'oklahoma':	'oklahoma city',
        'oregon':	'salem',
        'pennsylvania':	'harrisburg',
        'rhode Island':	'providence',
        'south Carolina':	'columbia',
        'south Dakota':	'pierre',
        'tennessee':	'nashville',
        'texas':	'austin',
        'utah':	'salt lake city',
        'vermont':	'montpelier',
        'virginia':	'richmond',
        'washington':	'olympia',
        'west Virginia':	'charleston',
        'wisconsin':	'madison',
        'wyoming':	'cheyenne'
        #TODO: add special teritorries
    }
    df.replace({source_data_name: state_fullname_to_capital_city_name}, inplace=True)
    return df

def us_capital_city_population_2019(df, source_data_name):
    df = df
    us_capital_city_population_2019 = {
        'montgomery':	'198525',
        'juneau':	'32113',
        'phoenix':	'1680992',
        'little rock':	'197312',
        'sacramento':	'513624',
        'denver':	'727211',
        'hartford':	'122105',
        'dover':	'38079',
        'tallahassee':	'194500',
        'atlanta':	'506811',
        'honolulu':	'345064',
        'boise':	'228959',
        'springfield':	'114230',
        'indianapolis':	'876384',
        'des moines':	'214237',
        'topeka':	'125310',
        'frankfort':	'27679',
        'baton rouge':	'220236',
        'augusta':	'18681',
        'annapolis':	'39174',
        'boston':	'692600',
        'lansing':	'118210',
        'saint paul':	'308096',
        'jackson':	'160628',
        'jefferson city':	'42838',
        'helena':	'32315',
        'lincoln':	'289102',
        'carson city':	'55916',
        'concord':	'43627',
        'trenton':	'83203',
        'santa fe':	'84683',
        'albany':	'96460',
        'raleigh':	'474069',
        'bismarck':	'73529',
        'columbus':	'898553',
        'oklahoma city':	'655057',
        'salem':	'174365',
        'harrisburg':	'49528',
        'providence':	'179883',
        'columbia':	'131674',
        'pierre':	'13646',
        'nashville':	'670820',
        'austin':	'978908',
        'salt lake city':	'200567',
        'montpelier':	'7855',
        'richmond':	'230436',
        'olympia':	'46478',
        'charleston':	'46536',
        'madison':	'259680',
        'cheyenne':	'64235'
    }
    df.replace({source_data_name: us_capital_city_population_2019}, inplace=True)
    return df

def us_capital_city_population_2019_msa(df, source_data_name):
    df = df
    us_capital_city_population_2019_msa = {
        'montgomery':	'373290',
        'juneau':	'32113',
        'phoenix':	'4948203',
        'little rock':	'742384',
        'sacramento':	'2363730',
        'denver':	'2967239',
        'hartford':	'1204877',
        'dover':	'180786',
        'tallahassee':	'387227',
        'atlanta':	'6020364',
        'honolulu':	'974563',
        'boise':	'749202',
        'springfield':	'206868',
        'indianapolis':	'2074537',
        'des moines':	'699292',
        'topeka':	'231969',
        'frankfort':	'73663',
        'baton rouge':	'854884',
        'augusta':	'122302',
        'annapolis':	'2800053',
        'boston':	'4873019',
        'lansing':	'550391',
        'saint paul':	'3654908',
        'jackson':	'594806',
        'jefferson city':	'151235',
        'helena':	'77414',
        'lincoln':	'336374',
        'carson city':	'55916',
        'concord':	'151391',
        'trenton':	'367430',
        'santa fe':	'150358',
        'albany':	'880381',
        'raleigh':	'1390785',
        'bismarck':	'128949',
        'columbus':	'2122271',
        'oklahoma City':	'1408950',
        'salem':	'433903',
        'harrisburg':	'577941',
        'providence':	'1624578',
        'columbia':	'838433',
        'pierre':	'20672',
        'nashville':	'1934317',
        'austin':	'2227083',
        'salt lake city':	'1232696',
        'montpelier':	'7855',
        'richmond':	'1291900',
        'olympia':	'290536',
        'charleston':	'257074',
        'madison':	'664865',
        'cheyenne':	'99500'
    }
    df.replace({source_data_name: us_capital_city_population_2019_msa}, inplace=True)
    return df

def us_capital_city_population_2019_csa(df, source_data_name):
    df = df
    us_capital_city_population_2019_csa = {
        'montgomery':	'461516',
        'juneau':	'32113',
        'phoenix':	'5002221',
        'little rock':	'908941',
        'sacramento':	'2639124',
        'denver':	'3617927',
        'hartford':	'1470083',
        'dover':	'7209620',
        'tallahassee':	'387227',
        'atlanta':	'6853392',
        'honolulu':	'974563',
        'boise':	'831235',
        'springfield':	'306399',
        'indianapolis':	'2457286',
        'des moines':	'877991',
        'topeka':	'231969',
        'frankfort':	'745033',
        'baton rouge':	'854884',
        'augusta':	'122302',
        'annapolis':	'9814928',
        'boston':	'8287710',
        'lansing':	'550391',
        'saint paul':	'4027861',
        'jackson':	'674340',
        'jefferson city':	'151235',
        'helena':	'77414',
        'lincoln':	'357887',
        'carson city':	'637973',
        'concord':	'8287710',
        'trenton':	'22589036',
        'santa fe':	'1158464',
        'albany':	'1167594',
        'raleigh':	'2079687',
        'bismarck':	'128949',
        'columbus':	'2525639',
        'oklahoma city':	'1481542',
        'salem':	'3259710',
        'harrisburg':	'1271801',
        'providence':	'8287710',
        'columbia':	'963048',
        'pierre':	'20672',
        'nashville':	'2062547',
        'austin':	'2227083',
        'salt lake city':	'2641048',
        'montpelier':	'7855',
        'richmond':	'1291900',
        'olympia':	'4903675',
        'charleston':	'776694',
        'madison':	'892661',
        'cheyenne':	'99500'
    }
    df.replace({source_data_name: us_capital_city_population_2019_csa}, inplace=True)
    return df

def us_state_total_area_rank(df, source_data_name):
    df = df
    us_state_total_area_rank = {
        'alaska': 	'1',
        'texas': 	'2',
        'california': 	'3',
        'montana': 	'4',
        'new mexico': 	'5',
        'arizona': 	'6',
        'nevada': 	'7',
        'colorado': 	'8',
        'oregon': 	'9',
        'wyoming': 	'10',
        'michigan': 	'11',
        'minnesota': 	'12',
        'utah': 	'13',
        'idaho': 	'14',
        'kansas': 	'15',
        'nebraska': 	'16',
        'south dakota': 	'17',
        'washington': 	'18',
        'north dakota': 	'19',
        'oklahoma': 	'20',
        'missouri': 	'21',
        'florida': 	'22',
        'wisconsin': 	'23',
        'georgia': 	'24',
        'illinois': 	'25',
        'iowa': 	'26',
        'new york': 	'27',
        'north carolina': 	'28',
        'arkansas': 	'29',
        'alabama': 	'30',
        'louisiana': 	'31',
        'mississippi': 	'32',
        'pennsylvania': 	'33',
        'ohio': 	'34',
        'virginia': 	'35',
        'tennessee': 	'36',
        'kentucky': 	'37',
        'indiana': 	'38',
        'maine': 	'39',
        'south carolina': 	'40',
        'west virginia': 	'41',
        'maryland': 	'42',
        'hawaii': 	'43',
        'massachusetts': 	'44',
        'vermont': 	'45',
        'new hampshire': 	'46',
        'new jersey': 	'47',
        'connecticut': 	'48',
        'delaware': 	'49',
        'rhode island': 	'50'
    }
    df.replace({source_data_name: us_state_total_area_rank}, inplace=True)
    return df