"""
Data Preprocessing Module for Marketing Campaign Analysis
"""

import pandas as pd
import numpy as np
from pathlib import Path

class DataPreprocessor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        
    def load_data(self):
        """Load the marketing campaign dataset"""
        print("Loading data...")
        self.df = pd.read_csv(self.data_path)
        print(f"Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        return self.df
    
    def explore_data(self):
        """Basic data exploration"""
        print("\n=== Data Overview ===")
        print(self.df.info())
        print("\n=== First Few Rows ===")
        print(self.df.head())
        print("\n=== Statistical Summary ===")
        print(self.df.describe())
        print("\n=== Missing Values ===")
        print(self.df.isnull().sum())
        
    def clean_data(self):
        """Clean and prepare data for analysis"""
        print("\nCleaning data...")
        
        # Handle missing values
        if 'unknown' in self.df.values:
            for col in self.df.columns:
                if self.df[col].dtype == 'object':
                    self.df[col] = self.df[col].replace('unknown', np.nan)
        
        # Convert target variable to binary
        if 'y' in self.df.columns:
            self.df['converted'] = (self.df['y'] == 'yes').astype(int)
        
        # Create age groups
        if 'age' in self.df.columns:
            self.df['age_group'] = pd.cut(self.df['age'], 
                                          bins=[0, 25, 35, 45, 55, 65, 100],
                                          labels=['<25', '25-35', '35-45', '45-55', '55-65', '65+'])
        
        # Extract month and day features
        if 'month' in self.df.columns:
            month_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
                          'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
            self.df['month_num'] = self.df['month'].map({m: i+1 for i, m in enumerate(month_order)})
        
        print("Data cleaning completed!")
        return self.df
    
    def save_processed_data(self, output_path):
        """Save processed data"""
        self.df.to_csv(output_path, index=False)
        print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    data_path = Path("data/bank-marketing.csv")
    output_path = Path("data/processed_data.csv")
    
    preprocessor = DataPreprocessor(data_path)
    preprocessor.load_data()
    preprocessor.explore_data()
    preprocessor.clean_data()
    preprocessor.save_processed_data(output_path)
