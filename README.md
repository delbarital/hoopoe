# Hoopoe
## A fast and easy way to enrich your data

Hoopoe is a data enrichment service that makes it easy to improve your data-centric services and increase the accuracy of your ML models.

Hoopoe saves you time in scraping data and loading it to Pandas Dataframes. Instead, just specify the data you already have in your dataframe and its type, and specify the desired data you would like to add.

## Current development status
Hoopoe is in its early days, and offered as a pre-alpha version, therefore, bugs are expected. In addition, the current dataset avialability is low. You can check the list below to find out which datasets and translations are already available. This list will be updated from time to time.

## Available datasets
<ul>
<li>US states</li>
    <ul>
        <li>State name abbriviation (USPS abbreviation)</li>
        <li>Full state name</li>
        <li>State population</li>
        <li>State capital city:</li>
            <ul>
                <li>State capital city name</li>
                <li>State capital city population:</li>
                    <ul>
                        <li>Population</li>
                        <li>MSA/µSA population (Metropolitan statistical area / Micropolitan statistical area)</li>
                        <li>CSA population (Combined statistical area)</li>
                    </ul>
            </ul>
        <li>State area:</li>
            <ul>
                <li>State area rank</li>
            </ul>
    </ul>
<li>Country calling codes (international call prefixes)</li>
    <ul>
        <li>Country name</li>
        <li>International calling code</li>
    </ul>

<li>Units of measure</li>
    <ul>
        <li>Celsius</li>
        <li>farenheit</li>
        <li>Kelvin</li>
    </ul>
</ul>

<br>

## Work in progress datasets
<ul>
<li>US states ISO 3166 code</li>
<li>US states area</li>
<li>US states time zone</li>
<li>US states density</li>
<li>US population rank</li>
<li>US states income rank</li>
<li>US states density rank</li>
<li>US city population</li>
<li>Population by country</li>
<li>Capital City by country</li>
<li>Countries time zone</li>
<li>Countries official language</li>
<li>Countries area</li>
<li>Countries capital city</li> 
</ul>

# How to use

Currently Hoopoe supports enrichments of Pandas Dataframes and single strings.
For basic usage, after installation, import hoopoe and use the hoopoe enrich function as follows:<br>
hoopoe.enrich(data, source_data_name, source_data_type, target_data_type)

<b>data</b> - Either a string or a Pandas dataframe.<br>
<b>source_data_name</b> - the dataframe column name of the column you want to enrich.<br>
<b>source_data_type</b> - the Hoopoe source data type. For example us_state_name_abbr for a column holding abbriviations of us state.<br>
<b>target_data_type</b> - the target Hoopoe data type you would like Hoopoe to return. For example, for country name, return the target date type phone_prefix for country calling code.

## Enrichment options
| Category | Source data type desc. | Hoopoe source_data_type | Target data type desc. | Hoopoe target_data_type
| ------ | ------ | ------ | ------ | ------ |
| Places | Two letter abbriviations of USA states name (USPS abbreviation) | us_state_name_abbr | Full USA states name  | us_state_name_full | 
| Places | Full USA states name  | us_state_name_full | Two letter abbriviations of USA states name (USPS abbreviation) | us_state_name_abbr |
| Places | Full USA states name  | us_state_name_full | State population (2019) | us_state_population |
| Places | Full USA state name | us_state_name_full | State capital city name | us_state_capital_city
| Places | Capital city name | us_capital_city_name | City population 2019 est.| us_capital_city_population 
| Places | Capital city name | us_capital_city_name | City population (Metropolitan/Micropolitan Statistical Area - MSA) 2019 est.| us_capital_city_population_msa
| Places | Capital city name | us_capital_city_name | City population (Combined Statistical Area - CSA) 2019 est. | us_capital_city_population_csa
| Places | Full USA state name | us_state_name_full | State area rank | us_state_area_rank
| Phone numbers | Country name | country_name | Intenational phone prefix | phone_prefix
| Phone numbers | Intenational phone prefix | phone_prefix | Country name | country_name
| Units - Tempreture | Celsius | celsius | Farenheit | farenheit
| Units - Tempreture | Celsius | celsius | Kelvin | kelvin
| Units - Tempreture | Farenheit | farenheit | Celsius | celsius
| Units - Tempreture | Farenheit | farenheit | Kelvin | kelvin
| Units - Tempreture | Kelvin | kelvin | Celsius | celsius
| Units - Tempreture | Kelvin | kelvin | Farenheit | farenheit

<br><br>

# Installing
To install Hoopoe, run the following in your virtualenv:

`$ pip install hoopoe`

# Developing Hoopoe
To install Hoopoe, along with the tools you need to develop and run tests, run the following in your virtualenv:

`$ pip install -e .[dev]`

# Dependencies
* [Pandas](https://pandas.pydata.org)
<br><br>
## Dev dependencies (only for contributers)
* [pytest](https://pytest.org)
* [check-manifest](https://github.com/mgedmin/check-manifest)

# Licence
MIT License