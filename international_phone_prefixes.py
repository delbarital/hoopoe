def international_phone_prefixes_to_country(df, source_data_name):
    df = df
    international_phone_prefixes_to_country = {
        '93':	'afghanistan',
        '355':	'albania',
        '213':	'algeria',
        '1684':	'american samoa',
        '376':	'andorra',
        '244':	'angola',
        '1264':	'anguilla',
        '672':	'antarctica',
        '1268':	'antigua and barbuda',
        '54':	'argentina',
        '374':	'armenia',
        '297':	'aruba',
        '61':	'australia',
        '43':	'austria',
        '994':	'azerbaijan',
        '1242':	'bahamas',
        '973':	'bahrain',
        '880':	'bangladesh',
        '1246':	'barbados',
        '375':	'belarus',
        '32':	'belgium',
        '501':	'belize',
        '229':	'benin',
        '1441':	'bermuda',
        '975':	'bhutan',
        '591':	'bolivia',
        '387':	'bosnia and herzegovina',
        '267':	'botswana',
        '55':	'brazil',
        '246':	'british indian ocean territory',
        '1284':	'british virgin islands',
        '673':	'brunei',
        '359':	'bulgaria',
        '226':	'burkina faso',
        '257':	'burundi',
        '855':	'cambodia',
        '237':	'cameroon',
        '1':	'canada',
        '238':	'cape verde',
        '1345':	'cayman islands',
        '236':	'central african republic',
        '235':	'chad',
        '56':	'chile',
        '86':	'china',
        '61':	'christmas island',
        '61':	'cocos islands',
        '57':	'colombia',
        '269':	'comoros',
        '682':	'cook islands',
        '506':	'costa rica',
        '385':	'croatia',
        '53':	'cuba',
        '599':	'curacao',
        '357':	'cyprus',
        '420':	'czech republic',
        '243':	'democratic republic of the congo',
        '45':	'denmark',
        '253':	'djibouti',
        '1767':	'dominica',
        '1809':	'dominican republic',
        '670':	'east timor',
        '593':	'ecuador',
        '20':	'egypt',
        '503':	'el salvador',
        '240':	'equatorial guinea',
        '291':	'eritrea',
        '372':	'estonia',
        '251':	'ethiopia',
        '500':	'falkland islands',
        '298':	'faroe islands',
        '679':	'fiji',
        '358':	'finland',
        '33':	'france',
        '689':	'french polynesia',
        '241':	'gabon',
        '220':	'gambia',
        '995':	'georgia',
        '49':	'germany',
        '233':	'ghana',
        '350':	'gibraltar',
        '30':	'greece',
        '299':	'greenland',
        '1473':	'grenada',
        '1671':	'guam',
        '502':	'guatemala',
        '441481':	'guernsey',
        '224':	'guinea',
        '245':	'guinea-bissau',
        '592':	'guyana',
        '509':	'haiti',
        '504':	'honduras',
        '852':	'hong kong',
        '36':	'hungary',
        '354':	'iceland',
        '91':	'india',
        '62':	'indonesia',
        '98':	'iran',
        '964':	'iraq',
        '353':	'ireland',
        '441624':	'isle of man',
        '972':	'israel',
        '39':	'italy',
        '225':	'ivory coast',
        '1876':	'jamaica',
        '81':	'japan',
        '441534':	'jersey',
        '962':	'jordan',
        '7':	'kazakhstan',
        '254':	'kenya',
        '686':	'kiribati',
        '383':	'kosovo',
        '965':	'kuwait',
        '996':	'kyrgyzstan',
        '856':	'laos',
        '371':	'latvia',
        '961':	'lebanon',
        '266':	'lesotho',
        '231':	'liberia',
        '218':	'libya',
        '423':	'liechtenstein',
        '370':	'lithuania',
        '352':	'luxembourg',
        '853':	'macau',
        '389':	'macedonia',
        '261':	'madagascar',
        '265':	'malawi',
        '60':	'malaysia',
        '960':	'maldives',
        '223':	'mali',
        '356':	'malta',
        '692':	'marshall islands',
        '222':	'mauritania',
        '230':	'mauritius',
        '262':	'mayotte',
        '52':	'mexico',
        '691':	'micronesia',
        '373':	'moldova',
        '377':	'monaco',
        '976':	'mongolia',
        '382':	'montenegro',
        '1664':	'montserrat',
        '212':	'morocco',
        '258':	'mozambique',
        '95':	'myanmar',
        '264':	'namibia',
        '674':	'nauru',
        '977':	'nepal',
        '31':	'netherlands',
        '599':	'netherlands antilles',
        '687':	'new caledonia',
        '64':	'new zealand',
        '505':	'nicaragua',
        '227':	'niger',
        '234':	'nigeria',
        '683':	'niue',
        '850':	'north korea',
        '1670':	'northern mariana islands',
        '47':	'norway',
        '968':	'oman',
        '92':	'pakistan',
        '680':	'palau',
        '970':	'palestine',
        '507':	'panama',
        '675':	'papua new guinea',
        '595':	'paraguay',
        '51':	'peru',
        '63':	'philippines',
        '64':	'pitcairn',
        '48':	'poland',
        '351':	'portugal',
        '1787':	'puerto rico',
        '974':	'qatar',
        '242':	'republic of the congo',
        '262':	'reunion',
        '40':	'romania',
        '7':	'russia',
        '250':	'rwanda',
        '590':	'saint barthelemy',
        '290':	'saint helena',
        '1869':	'saint kitts and nevis',
        '1758':	'saint lucia',
        '590':	'saint martin',
        '508':	'saint pierre and miquelon',
        '1784':	'saint vincent and the grenadines',
        '685':	'samoa',
        '378':	'san marino',
        '239':	'sao tome and principe',
        '966':	'saudi arabia',
        '221':	'senegal',
        '381':	'serbia',
        '248':	'seychelles',
        '232':	'sierra leone',
        '65':	'singapore',
        '1721':	'sint maarten',
        '421':	'slovakia',
        '386':	'slovenia',
        '677':	'solomon islands',
        '252':	'somalia',
        '27':	'south africa',
        '82':	'south korea',
        '211':	'south sudan',
        '34':	'spain',
        '94':	'sri lanka',
        '249':	'sudan',
        '597':	'suriname',
        '47':	'svalbard and jan mayen',
        '268':	'swaziland',
        '46':	'sweden',
        '41':	'switzerland',
        '963':	'syria',
        '886':	'taiwan',
        '992':	'tajikistan',
        '255':	'tanzania',
        '66':	'thailand',
        '228':	'togo',
        '690':	'tokelau',
        '676':	'tonga',
        '1868':	'trinidad and tobago',
        '216':	'tunisia',
        '90':	'turkey',
        '993':	'turkmenistan',
        '1649':	'turks and caicos islands',
        '688':	'tuvalu',
        '1340':	'u.s. virgin islands',
        '256':	'uganda',
        '380':	'ukraine',
        '971':	'united arab emirates',
        '44':	'united kingdom',
        '1':	'united states',
        '598':	'uruguay',
        '998':	'uzbekistan',
        '678':	'vanuatu',
        '379':	'vatican',
        '58':	'venezuela',
        '84':	'vietnam',
        '681':	'wallis and futuna',
        '212':	'western sahara',
        '967':	'yemen',
        '260':	'zambia',
        '263':	'zimbabwe'
    }
    df.replace({source_data_name: international_phone_prefixes_to_country}, inplace=True)
    return df

def country_to_international_phone_prefixes(df, source_data_name):
    df = df
    country_to_international_phone_prefixes = {
        'afghanistan':	'93',
        'albania':	'355',
        'algeria':	'213',
        'american samoa':	'1684',
        'andorra':	'376',
        'angola':	'244',
        'anguilla':	'1264',
        'antarctica':	'672',
        'antigua and barbuda':	'1268',
        'argentina':	'54',
        'armenia':	'374',
        'aruba':	'297',
        'australia':	'61',
        'austria':	'43',
        'azerbaijan':	'994',
        'bahamas':	'1242',
        'bahrain':	'973',
        'bangladesh':	'880',
        'barbados':	'1246',
        'belarus':	'375',
        'belgium':	'32',
        'belize':	'501',
        'benin':	'229',
        'bermuda':	'1441',
        'bhutan':	'975',
        'bolivia':	'591',
        'bosnia and herzegovina':	'387',
        'botswana':	'267',
        'brazil':	'55',
        'british indian ocean territory':	'246',
        'british virgin islands':	'1284',
        'brunei':	'673',
        'bulgaria':	'359',
        'burkina faso':	'226',
        'burundi':	'257',
        'cambodia':	'855',
        'cameroon':	'237',
        'canada':	'1',
        'cape verde':	'238',
        'cayman islands':	'1345',
        'central african republic':	'236',
        'chad':	'235',
        'chile':	'56',
        'china':	'86',
        'christmas island':	'61',
        'cocos islands':	'61',
        'colombia':	'57',
        'comoros':	'269',
        'cook islands':	'682',
        'costa rica':	'506',
        'croatia':	'385',
        'cuba':	'53',
        'curacao':	'599',
        'cyprus':	'357',
        'czech republic':	'420',
        'democratic republic of the congo':	'243',
        'denmark':	'45',
        'djibouti':	'253',
        'dominica':	'1767',
        'dominican republic':	'1809',
        'east timor':	'670',
        'ecuador':	'593',
        'egypt':	'20',
        'el salvador':	'503',
        'equatorial guinea':	'240',
        'eritrea':	'291',
        'estonia':	'372',
        'ethiopia':	'251',
        'falkland islands':	'500',
        'faroe islands':	'298',
        'fiji':	'679',
        'finland':	'358',
        'france':	'33',
        'french polynesia':	'689',
        'gabon':	'241',
        'gambia':	'220',
        'georgia':	'995',
        'germany':	'49',
        'ghana':	'233',
        'gibraltar':	'350',
        'greece':	'30',
        'greenland':	'299',
        'grenada':	'1473',
        'guam':	'1671',
        'guatemala':	'502',
        'guernsey':	'441481',
        'guinea':	'224',
        'guinea-bissau':	'245',
        'guyana':	'592',
        'haiti':	'509',
        'honduras':	'504',
        'hong kong':	'852',
        'hungary':	'36',
        'iceland':	'354',
        'india':	'91',
        'indonesia':	'62',
        'iran':	'98',
        'iraq':	'964',
        'ireland':	'353',
        'isle of man':	'441624',
        'israel':	'972',
        'italy':	'39',
        'ivory coast':	'225',
        'jamaica':	'1876',
        'japan':	'81',
        'jersey':	'441534',
        'jordan':	'962',
        'kazakhstan':	'7',
        'kenya':	'254',
        'kiribati':	'686',
        'kosovo':	'383',
        'kuwait':	'965',
        'kyrgyzstan':	'996',
        'laos':	'856',
        'latvia':	'371',
        'lebanon':	'961',
        'lesotho':	'266',
        'liberia':	'231',
        'libya':	'218',
        'liechtenstein':	'423',
        'lithuania':	'370',
        'luxembourg':	'352',
        'macau':	'853',
        'macedonia':	'389',
        'madagascar':	'261',
        'malawi':	'265',
        'malaysia':	'60',
        'maldives':	'960',
        'mali':	'223',
        'malta':	'356',
        'marshall islands':	'692',
        'mauritania':	'222',
        'mauritius':	'230',
        'mayotte':	'262',
        'mexico':	'52',
        'micronesia':	'691',
        'moldova':	'373',
        'monaco':	'377',
        'mongolia':	'976',
        'montenegro':	'382',
        'montserrat':	'1664',
        'morocco':	'212',
        'mozambique':	'258',
        'myanmar':	'95',
        'namibia':	'264',
        'nauru':	'674',
        'nepal':	'977',
        'netherlands':	'31',
        'netherlands antilles':	'599',
        'new caledonia':	'687',
        'new zealand':	'64',
        'nicaragua':	'505',
        'niger':	'227',
        'nigeria':	'234',
        'niue':	'683',
        'north korea':	'850',
        'northern mariana islands':	'1670',
        'norway':	'47',
        'oman':	'968',
        'pakistan':	'92',
        'palau':	'680',
        'palestine':	'970',
        'panama':	'507',
        'papua new guinea':	'675',
        'paraguay':	'595',
        'peru':	'51',
        'philippines':	'63',
        'pitcairn':	'64',
        'poland':	'48',
        'portugal':	'351',
        'puerto rico':	'1787',
        'qatar':	'974',
        'republic of the congo':	'242',
        'reunion':	'262',
        'romania':	'40',
        'russia':	'7',
        'rwanda':	'250',
        'saint barthelemy':	'590',
        'saint helena':	'290',
        'saint kitts and nevis':	'1869',
        'saint lucia':	'1758',
        'saint martin':	'590',
        'saint pierre and miquelon':	'508',
        'saint vincent and the grenadines':	'1784',
        'samoa':	'685',
        'san marino':	'378',
        'sao tome and principe':	'239',
        'saudi arabia':	'966',
        'senegal':	'221',
        'serbia':	'381',
        'seychelles':	'248',
        'sierra leone':	'232',
        'singapore':	'65',
        'sint maarten':	'1721',
        'slovakia':	'421',
        'slovenia':	'386',
        'solomon islands':	'677',
        'somalia':	'252',
        'south africa':	'27',
        'south korea':	'82',
        'south sudan':	'211',
        'spain':	'34',
        'sri lanka':	'94',
        'sudan':	'249',
        'suriname':	'597',
        'svalbard and jan mayen':	'47',
        'swaziland':	'268',
        'sweden':	'46',
        'switzerland':	'41',
        'syria':	'963',
        'taiwan':	'886',
        'tajikistan':	'992',
        'tanzania':	'255',
        'thailand':	'66',
        'togo':	'228',
        'tokelau':	'690',
        'tonga':	'676',
        'trinidad and tobago':	'1868',
        'tunisia':	'216',
        'turkey':	'90',
        'turkmenistan':	'993',
        'turks and caicos islands':	'1649',
        'tuvalu':	'688',
        'u.s. virgin islands':	'1340',
        'uganda':	'256',
        'ukraine':	'380',
        'united arab emirates':	'971',
        'united kingdom':	'44',
        'united states':	'1',
        'uruguay':	'598',
        'uzbekistan':	'998',
        'vanuatu':	'678',
        'vatican':	'379',
        'venezuela':	'58',
        'vietnam':	'84',
        'wallis and futuna':	'681',
        'western sahara':	'212',
        'yemen':	'967',
        'zambia':	'260',
        'zimbabwe':	'263'     
    }
    df.replace({source_data_name: country_to_international_phone_prefixes}, inplace=True)
    return df