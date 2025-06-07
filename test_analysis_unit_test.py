import pandas as pd
import unittest
from analyze import analyze

class TestAnalyze(unittest.TestCase):

    # ...existing test methods...

    def test_analysis_matches_result_csv(self):
        # Run the analysis
        df = analyze(
            'C:\\Users\\SEGUN\\Documents\\Ify Data Science Sessions\\factbook_population.csv',
            'C:\\Users\\SEGUN\\Documents\\Ify Data Science Sessions\\factbook_obesity.csv'
        )
        # Load the expected result
        result_path = 'result.csv'
        expected_df = pd.read_csv(result_path)

        # Ensure 'Obesity Rate' and 'Country' columns exist in both DataFrames
        for col in ['Obesity Rate', 'Country']:
            if col not in df.columns or col not in expected_df.columns:
                self.fail(f"'{col}' column not found in one of the DataFrames for sorting and comparison.")

        # Get top 10 countries by obesity rate from both DataFrames
        df_top10 = df.sort_values(by='Obesity Rate', ascending=False).head(10).sort_values(by='Country').reset_index(drop=True)
        expected_top10 = expected_df.sort_values(by='Obesity Rate', ascending=False).head(10).sort_values(by='Country').reset_index(drop=True)

        # Compare DataFrames
        try:
            pd.testing.assert_frame_equal(df_top10, expected_top10, check_dtype=False)
        except AssertionError as e:
            self.fail(f"Top 10 analysis result does not match result.csv:\n{e}")

if __name__ == '__main__':
    unittest.main()