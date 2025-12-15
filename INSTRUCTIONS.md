# Setup and Run Instructions

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Step-by-Step Setup

### 1. Download the Dataset
1. Go to Kaggle: https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset
2. Download the dataset (you may need to create a free Kaggle account)
3. Place the downloaded CSV file in the `data/` folder
4. Rename it to `bank-marketing.csv`

### 2. Install Dependencies
```bash
# Navigate to project directory
cd marketing-campaign-analysis

# Install required packages
pip install -r requirements.txt
```

### 3. Run the Analysis

#### Option A: Run Complete Analysis Script
```bash
# Run from project root
python src/main_analysis.py
```

This will:
- Load and preprocess the data
- Calculate all KPIs (ROI, CAC, CLV, Conversion Rate)
- Generate all visualizations
- Display key insights and recommendations

#### Option B: Run Jupyter Notebook (Interactive)
```bash
# Start Jupyter Notebook
jupyter notebook

# Open: notebooks/campaign_analysis.ipynb
# Run cells sequentially
```

#### Option C: Run Individual Modules
```bash
# Data preprocessing only
python src/data_preprocessing.py

# KPI calculation only
python src/kpi_calculator.py

# Visualizations only
python src/visualization.py
```

## Expected Outputs

### Generated Files
- `data/processed_data.csv` - Cleaned and processed dataset
- `outputs/kpi_summary.csv` - Summary of key metrics
- `outputs/figures/*.png` - All visualization charts

### Visualizations Created
1. `conversion_by_age.png` - Conversion rates across age groups
2. `channel_performance.png` - Performance by marketing channel
3. `campaign_frequency.png` - Optimal contact frequency analysis
4. `monthly_trends.png` - Seasonal performance trends
5. `education_impact.png` - Conversion by education level
6. `job_analysis.png` - Performance by job type
7. `dashboard_summary.png` - Comprehensive dashboard overview

## Troubleshooting

### Issue: Dataset not found
**Solution:** Make sure you've downloaded the dataset from Kaggle and placed it in the `data/` folder as `bank-marketing.csv`

### Issue: Module import errors
**Solution:** Make sure you're running scripts from the project root directory, or add the src folder to your Python path:
```bash
export PYTHONPATH="${PYTHONPATH}:./src"  # Linux/Mac
set PYTHONPATH=%PYTHONPATH%;./src  # Windows
```

### Issue: Missing packages
**Solution:** Install all requirements:
```bash
pip install -r requirements.txt
```

## Customization

### Adjust KPI Assumptions
Edit these values in `src/main_analysis.py` or the Jupyter notebook:
```python
COST_PER_CONTACT = 50  # Cost per marketing contact
AVG_CUSTOMER_VALUE = 1000  # Average revenue per customer
RETENTION_RATE = 0.75  # Customer retention rate
DISCOUNT_RATE = 0.10  # Discount rate for CLV calculation
```

### Modify Visualizations
Edit `src/visualization.py` to customize:
- Color schemes
- Chart types
- Figure sizes
- Labels and titles

## Next Steps

1. **Review Results**: Check the `outputs/figures/` folder for all visualizations
2. **Share Insights**: Use `dashboard_summary.png` for presentations
3. **Document Findings**: Add your insights to the README
4. **Upload to GitHub**: 
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Marketing Campaign Analysis"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

## Project Structure
```
marketing-campaign-analysis/
├── data/                      # Dataset files
│   └── bank-marketing.csv     # Download from Kaggle
├── notebooks/                 # Jupyter notebooks
│   └── campaign_analysis.ipynb
├── src/                       # Python scripts
│   ├── data_preprocessing.py
│   ├── kpi_calculator.py
│   ├── visualization.py
│   └── main_analysis.py
├── outputs/                   # Generated files
│   └── figures/              # Visualization images
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── INSTRUCTIONS.md          # This file
```

## Support
For issues or questions, please check:
- Dataset documentation on Kaggle
- Python package documentation
- Project README.md

Happy analyzing! 📊
