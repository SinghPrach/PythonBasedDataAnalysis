# Dataset Link-https://www.kaggle.com/datasets/shashwatwork/impact-of-covid19-pandemic-on-the-global-economy

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Reading the Data
data_transformed = pd.read_csv(r"C:\Users\psingh484\Desktop\Data\April\Covid19\transformed_data.csv")
data_raw = pd.read_csv(r"C:\Users\psingh484\Desktop\Data\April\Covid19\raw_data.csv")
# print(data_transformed)
# print(data_raw)

# print(data_transformed.head())
# .head(x) returns first x rows, otherwise first 5 rows if x is not mentioned.
# print(data_raw.head())

# Renaming the columns
# rankings_pd.rename(columns = {'test':'TEST'}, inplace = True)\

value_count=data_transformed["COUNTRY"].value_counts()
value_mode=data_transformed["COUNTRY"].value_counts().mode()
# print(value_count)
# print(value_mode)
# print(type(value_count))
# Aggregating the data

code = data_transformed["CODE"].unique().tolist()
country = data_transformed["COUNTRY"].unique().tolist()
# print(code)
# print(len(code))
# print(country)
# print(type(code))
# print(type(country))
hdi = []
tc = []
td = []
sti = []
population = data_transformed["POP"].unique().tolist()
gdp = []

for i in country:
    hdi.append((data_transformed.loc[data_transformed["COUNTRY"] == i, "HDI"]).sum()/294)
    tc.append((data_raw.loc[data_raw["location"] == i, "total_cases"]).sum())
    td.append((data_raw.loc[data_raw["location"] == i, "total_deaths"]).sum())
    sti.append((data_transformed.loc[data_transformed["COUNTRY"] == i, "STI"]).sum()/294)
    population.append((data_raw.loc[data_raw["location"] == i, "population"]).sum()/294)

# Understanding loc
# result = df.loc['Row_2', 'Name']
# df = pd.DataFrame({'Weight': [45, 88, 56, 15, 71],
#                    'Name': ['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'],
#                    'Age': [14, 25, 55, 8, 21]})
# Create the index
# index_ = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5']
# Print the result
# print(result)
# 'Andrea'

aggregated_data = pd.DataFrame(list(zip(code, country, hdi, tc, td, sti, population)),
                               columns = ["Country Code", "Country", "HDI",
                                          "Total Cases", "Total Deaths",
                                          "Stringency Index", "Population"])
# print(aggregated_data.head())
# print(aggregated_data)

# Sorting Data According to Total Cases
data_sorted_tot_cases = aggregated_data.sort_values(by=["Total Cases"], ascending=False)
# print(data_sorted_tot_cases.head())

# Top 10 Countries with Highest Covid Cases
data_top10Covid = data_sorted_tot_cases.head(10)
# print(data_top10Covid)

data_top10Covid["GDP Before Covid"] = [65279.53, 8897.49, 2100.75,
                            11497.65, 7027.61, 9946.03,
                            29564.74, 6001.40, 6424.98, 42354.41]
data_top10Covid["GDP During Covid"] = [63543.58, 6796.84, 1900.71,
                            10126.72, 6126.87, 8346.70,
                            27057.16, 5090.72, 5332.77, 40284.64]
# print(data_top10Covid)

# Analyzing the Spread of Covid-19
figure_Spread_Covid19 = px.bar(data_top10Covid, y='Total Cases', x='Country',
            title="Countries with Highest Covid Cases")
# figure_Spread_Covid19.show()
# Analyzing the deaths due to Covid-19
figure_Death_Covid19 = px.bar(data_top10Covid, y='Total Deaths', x='Country',
            title="Countries with Highest Deaths")
# figure_Death_Covid19.show()

# Percentage of Total Cases and Deaths
cases = data_top10Covid["Total Cases"].sum()
deceased = data_top10Covid["Total Deaths"].sum()

labels = ["Total Cases", "Total Deaths"]
values = [cases, deceased]

fig_percent = px.pie(data_top10Covid, values=values, names=labels,
             title='Percentage of Total Cases and Deaths', hole=0.5)
# fig_percent.show()
# Calculating the death rate of Covid-19 cases:
death_rate = (data_top10Covid["Total Deaths"].sum() / data_top10Covid["Total Cases"].sum()) * 100
print("Death Rate = ", death_rate)

# Stringency index is a composite measure of response indicators, including school closures,
# workplace closures, and travel bans. It shows how strictly countries are following these measures
# to control the spread of covid-19:
fig_si = px.bar(data_top10Covid, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'],
             color='Stringency Index', height=400,
             title= "Stringency Index during Covid-19")
fig_si.show()

# Analyzing Covid-19 Impacts on Economy
fig_eco_preCovid = px.bar(data_top10Covid, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'],
             color='GDP Before Covid', height=400,
             title="GDP Per Capita Before Covid-19")
fig_eco_preCovid.show()

fig_eco_AftCovid = px.bar(data_top10Covid, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'],
             color='GDP During Covid', height=400,
             title="GDP Per Capita During Covid-19")
fig_eco_AftCovid.show()

# Comparing the GDP per capita before covid-19 and during covid-19 to have a
# look at the impact of covid-19 on the GDP per capita:
fig_compare_gdp = go.Figure()
fig_compare_gdp.add_trace(go.Bar(
    x=data_top10Covid["Country"],
    y=data_top10Covid["GDP Before Covid"],
    name='GDP Per Capita Before Covid-19',
    marker_color='indianred'
))
fig_compare_gdp.add_trace(go.Bar(
    x=data_top10Covid["Country"],
    y=data_top10Covid["GDP During Covid"],
    name='GDP Per Capita During Covid-19',
    marker_color='lightsalmon'
))
fig_compare_gdp.update_layout(barmode='group', xaxis_tickangle=-45)
fig_compare_gdp.show()

# Human Development Index is a statistic composite index of life expectancy, education, and
# per capita indicators. Let’s have a look at how many countries were spending their budget on
# the human development:
fig_hdi = px.bar(data_top10Covid, x='Country', y='Total Cases',
             hover_data=['Population', 'Total Deaths'],
             color='HDI', height=400,
             title="Human Development Index during Covid-19")
fig_hdi.show()
# In this task, we studied the spread of covid-19 among the countries and its impact on the global economy.
# We saw that the outbreak of covid-19 resulted in the highest number of covid-19 cases and deaths in the
# united states. One major reason behind this is the stringency index of the United States.
# It is comparatively low according to the population.
# We also analyzed how the GDP per capita of every country was affected during the outbreak of covid-19.
