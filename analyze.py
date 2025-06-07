import pandas as pd

def analyze(factbook_pop: str, factbook_obesity: str) -> pd.DataFrame:
    """
    Analyze the Factbook population and obesity datasets.

    Parameters:
    - factbook_pop: Path to the Factbook population dataset.
    - factbook_obesity: Path to the Factbook obesity dataset.

    Returns:
    - DataFrame with merged and analyzed data.
    """
    # Load datasets
    pop_df = pd.read_csv('factbook_pop.csv')
    obesity_df = pd.read_csv('factbook_obesity.csv')
    print("Population Data Preview:")
    print(pop_df.head())
    print("Obesity Data Preview:")
    print(obesity_df.head())

    # Ensure 'Country' column exists in both DataFrames
    if 'Country' not in pop_df.columns or 'Country' not in obesity_df.columns:
        raise KeyError("Both datasets must contain a 'Country' column for merging.")

    # Merge the datasets on a common column ('Country')
    merged_df = pd.merge(pop_df, obesity_df, on='Country', how='inner')
    print("Merged Data Preview:")
    print(merged_df.head())

    return merged_df

df = analyze(
    'C:\\Users\\SEGUN\\Documents\\Ify Data Science MC\\factbook_population.csv',
    'C:\\Users\\SEGUN\\Documents\\Ify Data Science MC\\factbook_obesity.csv'
)
# Display the first few rows of the merged DataFrame
print("\nMerged DataFrame:")
print(df.head())

# filter obesity rate greater than 20% and population greater than 10 million
filtered_df = df[(df['Obesity Rate'] > 20) & (df['Population'] > 10000000)]

# sort by obesity rate in descending order
sorted_df = filtered_df.sort_values(by='Obesity Rate', ascending=False)

# select the top 10 countries
top_countries = sorted_df.head(10)

# index the resulting DataFrame by 'Country' from 1 to 10
top_countries.index = range(1, len(top_countries) + 1)
# display the top 10 countries with obesity rate greater than 20% and population greater than 10 million
print("\nTop 10 Countries:")
print(top_countries)