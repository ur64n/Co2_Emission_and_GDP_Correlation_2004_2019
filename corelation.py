import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data loading
file_path = '/home/urban/Projekty/etl_test/portfolio/AirQualityAnalysis/data/transformed/corelation_data.csv'
df = pd.read_csv(file_path)

# Data preview
print(df.head())

# Grouping data by country
grouped_df = df.groupby('Country Name')

# Initialize DataFrame for correlation results
correlation_results = pd.DataFrame()

# Loop over each country and calculate correlation
for country, data in grouped_df:
    # Filter relevant data
    relevant_data = data[['CO2 emissions (kt)', 'CO2 emissions (metric tons per capita)', 
                          'CO2 emissions from transport (% of total fuel combustion)', 
                          'CO2 intensity (kg per kg of oil equivalent energy use)', 
                          'Combustible renewables and waste (% of total energy)', 
                          'GDP (constant 2015 US$)']]
    
    # Drop rows with missing values
    relevant_data = relevant_data.dropna()
    
    # Calculate correlation matrix
    correlation_matrix = relevant_data.corr()
    
    # Display correlation for each country
    print(f"Korelacja dla {country}:\n", correlation_matrix)
    
    # Save correlation results for each country
    correlation_results[country] = correlation_matrix['GDP (constant 2015 US$)']
    
    # Plot correlation matrix for Russian Federation
    if country == 'Russian Federation':
        plt.figure(figsize=(10, 8))  # Zwiększamy rozmiar wykresu
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
        plt.xticks(rotation=45, ha='right')  # Obracamy etykiety osi X dla lepszej widoczności
        plt.title(f"Korelacja wskaźników dla {country}")
        plt.tight_layout()
        plt.show()

# Save correlation results to CSV
correlation_results.to_csv('correlation_results.csv')
