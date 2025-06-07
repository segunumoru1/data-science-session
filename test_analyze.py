import pandas as pd
import unittest
from analyze import analyze

class TestAnalyze(unittest.TestCase):

    def test_analyze(self):
        df = analyze(
            'C:\\Users\\SEGUN\\Documents\\Ify Data Science MC\\factbook_population.csv',
            'C:\\Users\\SEGUN\\Documents\\Ify Data Science MC\\factbook_obesity.csv'
        )
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)
        self.assertIn('Country', df.columns)
        self.assertIn('Obesity Rate', df.columns)
        self.assertIn('Population', df.columns)

    def test_filtered_data(self):
        df = analyze(
            'C:\\Users\\SEGUN\\Documents\\Ify Data Science MC\\factbook_population.csv',
            'C:\\Users\\SEGUN\\Documents\\Ify Data Science MC\\factbook_obesity.csv'
        )
        filtered_df = df[(df['Obesity Rate'] > 20) & (df['Population'] > 10000000)]
        self.assertFalse(filtered_df.empty)
        self.assertTrue((filtered_df['Obesity Rate'] > 20).all())
        self.assertTrue((filtered_df['Population'] > 10000000).all())

    def test_top_countries(self):
        df = analyze(
            'C:\\Users\\SEGUN\\Documents\\Ify Data Science MC\\factbook_population.csv',
            'C:\\Users\\SEGUN\\Documents\\Ify Data Science MC\\factbook_obesity.csv'
        )
        filtered_df = df[(df['Obesity Rate'] > 20) & (df['Population'] > 10000000)]
        sorted_df = filtered_df.sort_values(by='Obesity Rate', ascending=False)
        top_countries = sorted_df.head(8)
        
        self.assertEqual(len(top_countries), 8)
        self.assertTrue((top_countries['Obesity Rate'] > 20).all())
        self.assertTrue((top_countries['Population'] > 10000000).all())

if __name__ == '__main__':
    unittest.main()
