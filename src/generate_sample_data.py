"""
Generate Sample Marketing Campaign Data
Use this if you don't have access to the Kaggle dataset yet
"""

import pandas as pd
import numpy as np
from pathlib import Path

def generate_sample_data(n_samples=5000):
    """Generate synthetic marketing campaign data for testing"""
    
    np.random.seed(42)
    
    # Demographics
    ages = np.random.randint(18, 80, n_samples)
    jobs = np.random.choice(['admin.', 'technician', 'services', 'management', 
                            'retired', 'blue-collar', 'unemployed', 'entrepreneur',
                            'housemaid', 'self-employed', 'student'], n_samples)
    marital = np.random.choice(['married', 'single', 'divorced'], n_samples)
    education = np.random.choice(['primary', 'secondary', 'tertiary', 'unknown'], n_samples)
    
    # Financial
    default = np.random.choice(['no', 'yes'], n_samples, p=[0.98, 0.02])
    balance = np.random.randint(-5000, 50000, n_samples)
    housing = np.random.choice(['yes', 'no'], n_samples, p=[0.6, 0.4])
    loan = np.random.choice(['no', 'yes'], n_samples, p=[0.85, 0.15])
    
    # Campaign details
    contact = np.random.choice(['cellular', 'telephone', 'unknown'], n_samples, p=[0.65, 0.25, 0.1])
    day = np.random.randint(1, 32, n_samples)
    month = np.random.choice(['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                             'jul', 'aug', 'sep', 'oct', 'nov', 'dec'], n_samples)
    duration = np.random.randint(0, 3000, n_samples)
    campaign = np.random.randint(1, 50, n_samples)
    pdays = np.random.choice([-1] + list(range(0, 500)), n_samples)
    previous = np.random.randint(0, 40, n_samples)
    poutcome = np.random.choice(['unknown', 'failure', 'success', 'other'], n_samples)
    
    # Target variable (with some logic for realism)
    # Higher conversion for: younger age, cellular contact, higher education, fewer campaigns
    conversion_prob = 0.1  # base rate
    
    # Adjust probabilities based on features
    probs = np.full(n_samples, conversion_prob)
    probs[ages < 35] *= 2.4  # Young people convert better
    probs[contact == 'cellular'] *= 1.5  # Cellular works better
    probs[education == 'tertiary'] *= 1.8  # Higher education converts better
    probs[campaign <= 3] *= 1.5  # Fewer contacts work better
    probs[duration > 500] *= 2.0  # Longer calls convert better
    
    # Cap probabilities at 1.0
    probs = np.minimum(probs, 1.0)
    
    # Generate target
    y = np.random.binomial(1, probs)
    y = np.where(y == 1, 'yes', 'no')
    
    # Create DataFrame
    df = pd.DataFrame({
        'age': ages,
        'job': jobs,
        'marital': marital,
        'education': education,
        'default': default,
        'balance': balance,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'day': day,
        'month': month,
        'duration': duration,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
        'poutcome': poutcome,
        'y': y
    })
    
    return df

if __name__ == "__main__":
    print("Generating sample marketing campaign data...")
    
    # Generate data
    df = generate_sample_data(n_samples=10000)
    
    # Save to data folder
    output_path = Path("data/bank-marketing.csv")
    df.to_csv(output_path, index=False)
    
    print(f"✅ Sample data generated: {len(df)} records")
    print(f"📁 Saved to: {output_path}")
    print(f"\nConversion rate: {(df['y'] == 'yes').mean()*100:.2f}%")
    print(f"\nThis is SAMPLE DATA for testing purposes.")
    print(f"For real analysis, download the actual dataset from Kaggle:")
    print(f"https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset")
