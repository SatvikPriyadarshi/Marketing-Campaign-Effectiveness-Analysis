"""
Main Analysis Script for Marketing Campaign Effectiveness
Run this script to perform complete analysis
"""

import pandas as pd
from pathlib import Path
from data_preprocessing import DataPreprocessor
from kpi_calculator import KPICalculator
from visualization import CampaignVisualizer

def main():
    print("="*60)
    print("MARKETING CAMPAIGN EFFECTIVENESS ANALYSIS")
    print("="*60)
    
    # Define paths
    data_path = Path("data/bank-marketing.csv")
    processed_path = Path("data/processed_data.csv")
    
    # Check if data exists
    if not data_path.exists():
        print(f"\n⚠️  Dataset not found at {data_path}")
        print("\nPlease download the Bank Marketing Dataset from Kaggle:")
        print("https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset")
        print(f"And place it in the 'data' folder as 'bank-marketing.csv'")
        return
    
    # Step 1: Data Preprocessing
    print("\n" + "="*60)
    print("STEP 1: DATA PREPROCESSING")
    print("="*60)
    
    preprocessor = DataPreprocessor(data_path)
    df = preprocessor.load_data()
    preprocessor.explore_data()
    df = preprocessor.clean_data()
    preprocessor.save_processed_data(processed_path)
    
    # Step 2: KPI Calculation
    print("\n" + "="*60)
    print("STEP 2: KPI CALCULATION")
    print("="*60)
    
    calculator = KPICalculator(df)
    kpis = calculator.generate_kpi_report()
    
    # Step 3: Visualization
    print("\n" + "="*60)
    print("STEP 3: GENERATING VISUALIZATIONS")
    print("="*60)
    
    visualizer = CampaignVisualizer(df)
    visualizer.generate_all_visualizations()
    
    # Step 4: Key Insights
    print("\n" + "="*60)
    print("KEY INSIGHTS & RECOMMENDATIONS")
    print("="*60)
    
    # Calculate key insights
    age_conv = df.groupby('age_group')['converted'].mean() * 100
    best_age = age_conv.idxmax()
    best_age_rate = age_conv.max()
    avg_rate = df['converted'].mean() * 100
    multiplier = best_age_rate / avg_rate
    
    channel_conv = df.groupby('contact')['converted'].mean() * 100
    best_channel = channel_conv.idxmax()
    best_channel_rate = channel_conv.max()
    
    print(f"\n✅ TOP INSIGHTS:")
    print(f"\n1. AGE GROUP PERFORMANCE:")
    print(f"   • The {best_age} age group shows the highest conversion rate at {best_age_rate:.2f}%")
    print(f"   • This is {multiplier:.2f}x higher than the overall average ({avg_rate:.2f}%)")
    print(f"   • Recommendation: Focus marketing budget on {best_age} demographic")
    
    print(f"\n2. CHANNEL EFFECTIVENESS:")
    print(f"   • {best_channel.capitalize()} channel performs best with {best_channel_rate:.2f}% conversion")
    print(f"   • Recommendation: Prioritize {best_channel} for future campaigns")
    
    # Campaign frequency insights
    campaign_bins = [0, 1, 2, 3, 5, 10, 100]
    campaign_labels = ['1', '2', '3', '4-5', '6-10', '10+']
    df['campaign_group'] = pd.cut(df['campaign'], bins=campaign_bins, 
                                   labels=campaign_labels, include_lowest=True)
    camp_conv = df.groupby('campaign_group')['converted'].mean() * 100
    optimal_contacts = camp_conv.idxmax()
    optimal_rate = camp_conv.max()
    
    print(f"\n3. CONTACT FREQUENCY:")
    print(f"   • Optimal contact frequency: {optimal_contacts} times ({optimal_rate:.2f}% conversion)")
    print(f"   • Recommendation: Limit contacts to {optimal_contacts} per campaign to maximize efficiency")
    
    # Monthly performance
    if 'month' in df.columns:
        month_conv = df.groupby('month')['converted'].mean() * 100
        best_month = month_conv.idxmax()
        best_month_rate = month_conv.max()
        print(f"\n4. SEASONAL TRENDS:")
        print(f"   • Best performing month: {best_month.upper()} ({best_month_rate:.2f}% conversion)")
        print(f"   • Recommendation: Increase campaign intensity during high-performing months")
    
    # ROI Analysis
    clv = kpis.get('CLV', 0)
    cac = kpis.get('CAC', 1)
    clv_cac_ratio = clv / cac if cac > 0 else 0
    
    print(f"\n5. FINANCIAL METRICS:")
    print(f"   • CLV to CAC Ratio: {clv_cac_ratio:.2f}x")
    if clv_cac_ratio > 3:
        print(f"   • Status: ✅ EXCELLENT - Strong return on marketing investment")
    elif clv_cac_ratio > 1:
        print(f"   • Status: ⚠️  ACCEPTABLE - Room for improvement")
    else:
        print(f"   • Status: ❌ POOR - Marketing spend exceeds customer value")
    
    print(f"\n   • ROI: {kpis.get('ROI', 0):.2f}%")
    print(f"   • Recommendation: {'Continue current strategy' if clv_cac_ratio > 3 else 'Optimize targeting and reduce CAC'}")
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)
    print(f"\n📊 Visualizations saved in: outputs/figures/")
    print(f"📄 Processed data saved in: data/processed_data.csv")
    print("\nNext Steps:")
    print("1. Review visualizations in the outputs/figures folder")
    print("2. Share dashboard_summary.png with stakeholders")
    print("3. Implement recommendations in next campaign cycle")
    print("4. Upload project to GitHub with README and screenshots")
    
if __name__ == "__main__":
    main()
