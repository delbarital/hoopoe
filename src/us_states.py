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

def us_state_total_area(df, source_data_name):
    df = df
    us_state_total_area = {
        'alaska': 	'1723337',
        'texas': 	'695662',
        'california': 	'423967',
        'montana': 	'380831',
        'new mexico': 	'314917',
        'arizona': 	'295234',
        'nevada': 	'286380',
        'colorado': 	'269601',
        'oregon': 	'254799',
        'wyoming': 	'253335',
        'michigan': 	'250487',
        'minnesota': 	'225163',
        'utah': 	'219882',
        'idaho': 	'216443',
        'kansas': 	'213100',
        'nebraska': 	'200330',
        'south dakota': 	'199729',
        'washington': 	'184661',
        'north dakota': 	'183108',
        'oklahoma': 	'181037',
        'missouri': 	'180540',
        'florida': 	'170312',
        'wisconsin': 	'169635',
        'georgia': 	'153910',
        'illinois': 	'149995',
        'iowa': 	'145746',
        'new york': 	'141297',
        'north carolina': 	'139391',
        'arkansas': 	'137732',
        'alabama': 	'135767',
        'louisiana': 	'135659',
        'mississippi': 	'125438',
        'pennsylvania': 	'119280',
        'ohio': 	'116098',
        'virginia': 	'110787',
        'tennessee': 	'109153',
        'kentucky': 	'104656',
        'indiana': 	'94326',
        'maine': 	'91633',
        'south carolina': 	'82933',
        'west virginia': 	'62756',
        'maryland': 	'32131',
        'hawaii': 	'28313',
        'massachusetts': 	'27336',
        'vermont': 	'24906',
        'new hampshire': 	'24214',
        'new jersey': 	'22591',
        'connecticut': 	'14357',
        'delaware': 	'6446',
        'rhode island': 	'4001'
    }
    df.replace({source_data_name: us_state_total_area}, inplace=True)
    return df

def us_state_land_area_rank(df, source_data_name):
    df = df
    us_state_land_area_rank = {
        'alaska': 	'1',
        'texas': 	'2',
        'california': 	'3',
        'montana': 	'4',
        'new mexico': 	'5',
        'arizona': 	'6',
        'nevada': 	'7',
        'colorado': 	'8',
        'oregon': 	'10',
        'wyoming': 	'9',
        'michigan': 	'22',
        'minnesota': 	'14',
        'utah': 	'12',
        'idaho': 	'11',
        'kansas': 	'13',
        'nebraska': 	'15',
        'south dakota': 	'16',
        'washington': 	'20',
        'north dakota': 	'17',
        'oklahoma': 	'19',
        'missouri': 	'18',
        'florida': 	'26',
        'wisconsin': 	'25',
        'georgia': 	'21',
        'illinois': 	'24',
        'iowa': 	'23',
        'new york': 	'30',
        'north carolina': 	'29',
        'arkansas': 	'27',
        'alabama': 	'28',
        'louisiana': 	'33',
        'mississippi': 	'31',
        'pennsylvania': 	'32',
        'ohio': 	'35',
        'virginia': 	'36',
        'tennessee': 	'34',
        'kentucky': 	'37',
        'indiana': 	'38',
        'maine': 	'39',
        'south carolina': 	'40',
        'west virginia': 	'41',
        'maryland': 	'42',
        'hawaii': 	'47',
        'massachusetts': 	'45',
        'vermont': 	'43',
        'new hampshire': 	'44',
        'new jersey': 	'46',
        'connecticut': 	'48',
        'delaware': 	'49',
        'rhode island': 	'50'
    }
    df.replace({source_data_name: us_state_land_area_rank}, inplace=True)
    return df

def us_state_land_area(df, source_data_name):
    df = df
    us_state_land_area = {
        'alaska': 	'1477953',
        'texas': 	'676587',
        'california': 	'403466',
        'montana': 	'376962',
        'new mexico': 	'314161',
        'arizona': 	'294207',
        'nevada': 	'284332',
        'colorado': 	'268431',
        'oregon': 	'248608',
        'wyoming': 	'251470',
        'michigan': 	'146435',
        'minnesota': 	'206232',
        'utah': 	'212818',
        'idaho': 	'214045',
        'kansas': 	'211754',
        'nebraska': 	'198974',
        'south dakota': 	'196350',
        'washington': 	'172119',
        'north dakota': 	'178711',
        'oklahoma': 	'177660',
        'missouri': 	'178040',
        'florida': 	'138887',
        'wisconsin': 	'140268',
        'georgia': 	'148959',
        'illinois': 	'143793',
        'iowa': 	'144669',
        'new york': 	'122057',
        'north carolina': 	'125920',
        'arkansas': 	'134771',
        'alabama': 	'131171',
        'louisiana': 	'111898',
        'mississippi': 	'121531',
        'pennsylvania': 	'115883',
        'ohio': 	'105829',
        'virginia': 	'102279',
        'tennessee': 	'106798',
        'kentucky': 	'102269',
        'indiana': 	'92789',
        'maine': 	'79883',
        'south carolina': 	'77857',
        'west virginia': 	'62259',
        'maryland': 	'25142',
        'hawaii': 	'16635',
        'massachusetts': 	'20202',
        'vermont': 	'23871',
        'new hampshire': 	'23187',
        'new jersey': 	'19047',
        'connecticut': 	'12542',
        'delaware': 	'5047',
        'rhode island': 	'2678'
    }
    df.replace({source_data_name: us_state_land_area}, inplace=True)
    return df

def us_state_water_area_rank(df, source_data_name):
    df = df
    us_state_water_area_rank = {
        'alaska': 	'1',
        'texas': 	'8',
        'california': 	'6',
        'montana': 	'26',
        'new mexico': 	'49',
        'arizona': 	'48',
        'nevada': 	'36',
        'colorado': 	'44',
        'oregon': 	'20',
        'wyoming': 	'37',
        'michigan': 	'2',
        'minnesota': 	'9',
        'utah': 	'17',
        'idaho': 	'33',
        'kansas': 	'42',
        'nebraska': 	'41',
        'south dakota': 	'29',
        'washington': 	'11',
        'north dakota': 	'24',
        'oklahoma': 	'30',
        'missouri': 	'32',
        'florida': 	'3',
        'wisconsin': 	'4',
        'georgia': 	'22',
        'illinois': 	'19',
        'iowa': 	'45',
        'new york': 	'7',
        'north carolina': 	'10',
        'arkansas': 	'31',
        'alabama': 	'23',
        'louisiana': 	'5',
        'mississippi': 	'25',
        'pennsylvania': 	'28',
        'ohio': 	'14',
        'virginia': 	'15',
        'tennessee': 	'35',
        'kentucky': 	'34',
        'indiana': 	'39',
        'maine': 	'12',
        'south carolina': 	'21',
        'west virginia': 	'50',
        'maryland': 	'18',
        'hawaii': 	'13',
        'massachusetts': 	'16',
        'vermont': 	'46',
        'new hampshire': 	'47',
        'new jersey': 	'27',
        'connecticut': 	'38',
        'delaware': 	'40',
        'rhode island': 	'43'
    }
    df.replace({source_data_name: us_state_water_area_rank}, inplace=True)
    return df

def us_state_water_area(df, source_data_name):
    df = df
    us_state_water_area = {
        'alaska': 	'245384',
        'texas': 	'19075',
        'california': 	'20501',
        'montana': 	'3869',
        'new mexico': 	'757',
        'arizona': 	'1026',
        'nevada': 	'2048',
        'colorado': 	'1170',
        'oregon': 	'6191',
        'wyoming': 	'1864',
        'michigan': 	'104052',
        'minnesota': 	'18930',
        'utah': 	'7064',
        'idaho': 	'2398',
        'kansas': 	'1346',
        'nebraska': 	'1356',
        'south dakota': 	'3379',
        'washington': 	'12542',
        'north dakota': 	'4397',
        'oklahoma': 	'3377',
        'missouri': 	'2501',
        'florida': 	'31424',
        'wisconsin': 	'29367',
        'georgia': 	'4951',
        'illinois': 	'6202',
        'iowa': 	'1077',
        'new york': 	'19240',
        'north carolina': 	'13471',
        'arkansas': 	'2961',
        'alabama': 	'4597',
        'louisiana': 	'23761',
        'mississippi': 	'3907',
        'pennsylvania': 	'3397',
        'ohio': 	'10269',
        'virginia': 	'8508',
        'tennessee': 	'2355',
        'kentucky': 	'2387',
        'indiana': 	'1537',
        'maine': 	'11750',
        'south carolina': 	'5076',
        'west virginia': 	'497',
        'maryland': 	'6990',
        'hawaii': 	'11678',
        'massachusetts': 	'7134',
        'vermont': 	'1035',
        'new hampshire': 	'1027',
        'new jersey': 	'3544',
        'connecticut': 	'1816',
        'delaware': 	'1399',
        'rhode island': 	'1324'
    }
    df.replace({source_data_name: us_state_water_area}, inplace=True)
    return df