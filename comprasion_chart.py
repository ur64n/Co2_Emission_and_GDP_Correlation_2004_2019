import pandas as pd
import matplotlib.pyplot as plt

# Data loading
data = pd.read_csv('/home/urban/Projekty/etl_test/portfolio/AirQualityAnalysis/data/transformed/corelation_data.csv') #path to file

# Function to calculate percentage change
def calculate_percentage_change(df, country, indicator):
    country_data = df[df['Country Name'] == country]
    base_value = country_data[indicator].iloc[0]
    return (country_data[indicator] / base_value) * 100

# Countries to analyze
countries = ['France', 'Germany', 'Poland', 'Russian Federation']

# Create DataFrame
scaled_data = pd.DataFrame()

# Transform data to percentage change
for country in countries:
    country_data = data[data['Country Name'] == country]
    new_data = pd.DataFrame({
        'Year': country_data['Year'].values,
        'Country': country,
        'CO2 emissions (kt)': calculate_percentage_change(data, country, 'CO2 emissions (kt)'),
        'GDP (constant 2015 US$)': calculate_percentage_change(data, country, 'GDP (constant 2015 US$)')
    })
    scaled_data = pd.concat([scaled_data, new_data], ignore_index=True)

# Line chart
plt.figure(figsize=(12, 8))

# Iterate over countries
for country in countries:
    plt.plot(scaled_data[scaled_data['Country'] == country]['Year'],
             scaled_data[scaled_data['Country'] == country]['CO2 emissions (kt)'],
             label=f'Emisje CO2 {country}')
    
    plt.plot(scaled_data[scaled_data['Country'] == country]['Year'],
             scaled_data[scaled_data['Country'] == country]['GDP (constant 2015 US$)'],
             linestyle='dashed', label=f'PKB {country}')

# Chart settings
plt.title('Procentowa zmiana emisji CO2 i PKB (2004 = 100%)', fontsize=14)
plt.xlabel('Rok', fontsize=12)
plt.ylabel('Procentowa zmiana (%)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
