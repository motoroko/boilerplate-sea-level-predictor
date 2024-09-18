import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(12,6))
    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'], label='Data')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series([i for i in range(df['Year'].min(), 2051)])
    plt.plot(years, slope * years + intercept, label='Fit: All Data', color='red')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000].copy()
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years = pd.Series([i for i in range(df_recent['Year'].min(), 2051)])
    plt.plot(years, slope_recent * years + intercept_recent, label='Fit: From 2000', color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()