"""
KPI Calculator Module for Marketing Campaign Analysis
Calculates ROI, CAC, CLV, Conversion Rate, and other metrics
"""

import pandas as pd
import numpy as np

class KPICalculator:
    def __init__(self, df):
        self.df = df
        self.kpis = {}
        
    def calculate_conversion_rate(self, group_by=None):
        """Calculate conversion rate overall or by segment"""
        if group_by:
            conversion_rates = self.df.groupby(group_by)['converted'].agg(['sum', 'count'])
            conversion_rates['conversion_rate'] = (conversion_rates['sum'] / conversion_rates['count'] * 100).round(2)
            return conversion_rates
        else:
            total_contacts = len(self.df)
            total_conversions = self.df['converted'].sum()
            conversion_rate = (total_conversions / total_contacts * 100).round(2)
            return conversion_rate
    
    def calculate_cac(self, total_marketing_spend=None, cost_per_contact=50):
        """
        Calculate Customer Acquisition Cost
        CAC = Total Marketing Spend / Number of Customers Acquired
        """
        if total_marketing_spend is None:
            # Estimate based on number of contacts
            total_marketing_spend = len(self.df) * cost_per_contact
        
        customers_acquired = self.df['converted'].sum()
        cac = total_marketing_spend / customers_acquired if customers_acquired > 0 else 0
        
        self.kpis['CAC'] = round(cac, 2)
        self.kpis['Total_Marketing_Spend'] = total_marketing_spend
        self.kpis['Customers_Acquired'] = customers_acquired
        
        return cac
    
    def calculate_roi(self, avg_customer_value=1000):
        """
        Calculate Return on Investment
        ROI = (Revenue - Cost) / Cost * 100
        """
        revenue = self.df['converted'].sum() * avg_customer_value
        cost = self.kpis.get('Total_Marketing_Spend', len(self.df) * 50)
        
        roi = ((revenue - cost) / cost * 100) if cost > 0 else 0
        
        self.kpis['ROI'] = round(roi, 2)
        self.kpis['Revenue'] = revenue
        
        return roi
    
    def calculate_clv(self, avg_customer_value=1000, retention_rate=0.75, discount_rate=0.10):
        """
        Calculate Customer Lifetime Value
        CLV = (Average Customer Value * Retention Rate) / (1 + Discount Rate - Retention Rate)
        """
        clv = (avg_customer_value * retention_rate) / (1 + discount_rate - retention_rate)
        self.kpis['CLV'] = round(clv, 2)
        return clv
    
    def calculate_campaign_effectiveness(self):
        """Calculate campaign effectiveness by contact frequency"""
        if 'campaign' in self.df.columns:
            campaign_stats = self.df.groupby('campaign').agg({
                'converted': ['sum', 'count', 'mean']
            }).round(4)
            campaign_stats.columns = ['conversions', 'total_contacts', 'conversion_rate']
            campaign_stats['conversion_rate'] = (campaign_stats['conversion_rate'] * 100).round(2)
            return campaign_stats
        return None
    
    def calculate_channel_performance(self, channel_col='contact'):
        """Calculate performance by marketing channel"""
        if channel_col in self.df.columns:
            channel_stats = self.df.groupby(channel_col).agg({
                'converted': ['sum', 'count', 'mean']
            })
            channel_stats.columns = ['conversions', 'total_contacts', 'conversion_rate']
            channel_stats['conversion_rate'] = (channel_stats['conversion_rate'] * 100).round(2)
            return channel_stats
        return None
    
    def generate_kpi_report(self):
        """Generate comprehensive KPI report"""
        print("\n" + "="*50)
        print("MARKETING CAMPAIGN KPI REPORT")
        print("="*50)
        
        # Overall metrics
        overall_conversion = self.calculate_conversion_rate()
        cac = self.calculate_cac()
        roi = self.calculate_roi()
        clv = self.calculate_clv()
        
        print(f"\n📊 Overall Performance Metrics:")
        print(f"   Total Contacts: {len(self.df):,}")
        print(f"   Total Conversions: {self.df['converted'].sum():,}")
        print(f"   Conversion Rate: {overall_conversion}%")
        print(f"   Customer Acquisition Cost (CAC): ${cac:,.2f}")
        print(f"   Customer Lifetime Value (CLV): ${clv:,.2f}")
        print(f"   Return on Investment (ROI): {roi:.2f}%")
        print(f"   CLV to CAC Ratio: {(clv/cac):.2f}x")
        
        # Age group analysis
        if 'age_group' in self.df.columns:
            print(f"\n👥 Conversion Rate by Age Group:")
            age_conversion = self.calculate_conversion_rate('age_group')
            print(age_conversion[['conversion_rate']].to_string())
        
        # Channel performance
        channel_perf = self.calculate_channel_performance()
        if channel_perf is not None:
            print(f"\n📱 Performance by Channel:")
            print(channel_perf.to_string())
        
        # Campaign effectiveness
        campaign_eff = self.calculate_campaign_effectiveness()
        if campaign_eff is not None:
            print(f"\n📞 Campaign Contact Frequency Analysis:")
            print(campaign_eff.head(10).to_string())
        
        print("\n" + "="*50)
        
        return self.kpis

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv("data/processed_data.csv")
    
    calculator = KPICalculator(df)
    kpis = calculator.generate_kpi_report()
