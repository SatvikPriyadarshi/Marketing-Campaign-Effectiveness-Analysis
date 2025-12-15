# Quick Start Guide ⚡

## Run Analysis in 3 Steps

### Step 1: Get the Data
**Option A - Real Data (Recommended for portfolio)**
1. Go to: https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset
2. Download the dataset
3. Save as: `data/bank-marketing.csv`

**Option B - Sample Data (For testing)**
```bash
python src/generate_sample_data.py
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Analysis
```bash
python src/main_analysis.py
```

**That's it!** Check `outputs/figures/` for visualizations.

---

## Alternative: One-Click Run

### Windows
```bash
run_analysis.bat
```

### Linux/Mac
```bash
chmod +x run_analysis.sh
./run_analysis.sh
```

---

## What You'll Get

### 📊 7 Visualizations
1. Conversion by Age Group
2. Channel Performance
3. Campaign Frequency Analysis
4. Monthly Trends
5. Education Impact
6. Job Type Analysis
7. Executive Dashboard

### 📈 Key Metrics
- ROI (Return on Investment)
- CAC (Customer Acquisition Cost)
- CLV (Customer Lifetime Value)
- Conversion Rates
- CLV/CAC Ratio

### 💡 Actionable Insights
- Best performing age groups
- Most effective channels
- Optimal contact frequency
- Seasonal trends
- Financial health metrics

---

## Troubleshooting

**Problem: "No module named 'pandas'"**
```bash
pip install pandas numpy matplotlib seaborn
```

**Problem: "File not found: bank-marketing.csv"**
```bash
# Generate sample data
python src/generate_sample_data.py
```

**Problem: "Permission denied"**
```bash
# Linux/Mac only
chmod +x run_analysis.sh
```

---

## File Locations

| What | Where |
|------|-------|
| Dataset | `data/bank-marketing.csv` |
| Visualizations | `outputs/figures/*.png` |
| Processed Data | `data/processed_data.csv` |
| Main Script | `src/main_analysis.py` |
| Notebook | `notebooks/campaign_analysis.ipynb` |

---

## Next Steps

1. ✅ Run the analysis
2. 📊 Review visualizations in `outputs/figures/`
3. 📝 Customize README.md with your name
4. 🚀 Upload to GitHub (see GITHUB_GUIDE.md)
5. 💼 Add to your portfolio
6. 📱 Share on LinkedIn

---

## Need More Help?

- **Setup Instructions**: See `INSTRUCTIONS.md`
- **GitHub Upload**: See `GITHUB_GUIDE.md`
- **Project Details**: See `PROJECT_SUMMARY.md`
- **Full Documentation**: See `README.md`

---

**Time to Complete**: 5-10 minutes
**Difficulty**: Beginner-friendly
**Impact**: Portfolio-ready project ⭐

Good luck! 🎯
