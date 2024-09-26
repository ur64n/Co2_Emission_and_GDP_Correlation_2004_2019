import pandas as pd

# File path
file_path = '/home/urban/Projekty/etl_test/portfolio/AirQualityAnalysis/data/raw/WDICSV.csv'

# Load data
df = pd.read_csv(file_path)

# Filter countries
countries = ['Poland', 'Germany', 'France', 'Russian Federation']
years = [str(year) for year in range(2015, 2020)]  # Lata, dla których będziemy liczyć średnią

# Dictionary with indicators
indicators = {
    'GDP': 'GDP (constant 2015 US$)',  # PKB w stałych cenach
    'CO2_total': 'CO2 emissions (kt)',  # Emisje CO2 (kt)
    'CO2_per_capita': 'CO2 emissions (metric tons per capita)',  # Emisje CO2 na osobę
    'CO2_from_transport': 'CO2 emissions from transport (% of total fuel combustion)',  # Emisje z transportu
    'CO2_intensity': 'CO2 intensity (kg per kg of oil equivalent energy use)',  # Intensywność CO2
    'renewable_energy': 'Combustible renewables and waste (% of total energy)'  # Odnawialna energia
}

# Filtering data for selected countries and indicators
filtered_df = df[df['Country Name'].isin(countries) & df['Indicator Name'].isin(indicators.values())]

# Change data structure to have indicators in separate columns
melted_df = filtered_df.melt(id_vars=['Country Name', 'Indicator Name'], value_vars=[str(year) for year in range(2004, 2020)], var_name='Year', value_name='Value')

# Pivot data to have indicators in separate columns
pivot_df = melted_df.pivot_table(index=['Country Name', 'Year'], columns='Indicator Name', values='Value').reset_index()

# Function to calculate moving average for the last 10 years
def calculate_moving_average(df, year, indicator, country):
    years_range = list(range(year-10, year))
    years_range = [str(yr) for yr in years_range]
    subset = df[(df['Year'].isin(years_range)) & (df['Country Name'] == country)]
    return subset[indicator].mean()

# Creating a copy of the pivot_df DataFrame
for year in range(2015, 2020):
    for country in countries:
        for indicator in indicators.values():
            avg_value = calculate_moving_average(pivot_df, year, indicator, country)
            # Uzupełniamy puste dane średnią
            pivot_df.loc[(pivot_df['Year'] == str(year)) & (pivot_df['Country Name'] == country) & (pivot_df[indicator].isna()), indicator] = avg_value

# Save data to CSV
pivot_df.to_csv('enhanced_correlation_ready_data.csv', index=False)

print(pivot_df)
