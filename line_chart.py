import pandas as pd
import matplotlib.pyplot as plt

# Data loading
file_path = '/home/urban/Projekty/etl_test/portfolio/AirQualityAnalysis/data/transformed/corelation_data.csv'
df = pd.read_csv(file_path)

# Indicators
gdp_indicator = 'GDP (constant 2015 US$)'
co2_indicator = 'CO2 emissions (kt)'

# Grouping data by country
grouped_df = df.groupby('Country Name')

# Loop over each country and plot line chart
for country, data in grouped_df:
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Create first axis
    color = 'tab:blue'
    ax1.set_xlabel('Rok')
    ax1.set_ylabel('Emisje CO2 (kt)', color=color)
    ax1.plot(data['Year'], data[co2_indicator], color=color, label=co2_indicator)
    ax1.tick_params(axis='y', labelcolor=color)
    
    # Add second axis
    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('PKB (constant 2015 US$)', color=color)
    ax2.plot(data['Year'], data[gdp_indicator], color=color, label=gdp_indicator)
    ax2.tick_params(axis='y', labelcolor=color)
    
    # Add title and grid
    plt.title(f'Zmiany emisji CO2 i PKB dla {country} (2010-2019)')
    ax1.grid(True)
    
    # Display plot
    fig.tight_layout()
    plt.show()
