# Hoopoe
## A fast and easy way to enrich your data

Hoopoe is a data enrichment service that makes it easy to improve your data-centric services and increase the accuracy of your ML models.

Hoopoe saves you time in scraping data and load it to Pandas Dataframes. Instead, just specify the data you already have in your dataframe and its type, and specify the desired data you would like to add.

## Current development status
Hoopoe is in its early days, therefore, bugs are expected. In addition, the current dataset avialability is low. You can check the list below to find out which datasets and translations are already available. This list will be updated from time to time.

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
</ul>

## Work in progress datasets
<ul>
<li>US states ISO 3166 code</li>
<li>US states area</li>
<li>US states time zone</li>
<li>US states density</li>
<li>US population rank</li>
<li>US states income rank</li>
<li>US states density rank</li>
<li>Population by country</li>
<li>Capital City by country</li>
<li>Countries time zone</li>
<li>Countries official language</li>
</ul>

# How to use

Currently Hoopoe supports enrichments of Pandas Dataframes and single strings.
For basic usage, after installation, import hoopoe and use the hoopoe enrich function as follows:<br>
hoopoe.enrich(data, source_data_name, source_data_type, target_data_type)

<b>data</b> - Either a string or a Pandas data frame.<br>
<b>source_data_name</b> - the dataframe column name of the column you want to enrich.<br>
<b>source_data_type</b> - the Hoopoe source data type. For example us_state_name_abbr for a column holding abbriviations of us state.<br>
<b>target_data_type</b> - the target Hoopoe data type you would like Hoopoe to return. For example, for country name, return the target date type phone_prefix for country calling code.

# Installing

# Dependencies
* [NumPy](https://www.numpy.org)
* [Pandas](https://pandas.pydata.org)

# Licence
MIT License