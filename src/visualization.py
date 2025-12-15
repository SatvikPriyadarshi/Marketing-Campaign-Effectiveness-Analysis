"""
Visualization Module for Marketing Campaign Analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

class CampaignVisualizer:
    def __init__(self, df, output_dir='outputs/figures'):
        self.df = df
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Set style
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 6)
        
    def plot_conversion_by_age(self):
        """Plot conversion rates by age group"""
        if 'age_group' not in self.df.columns:
            print("Age group column not found")
            return
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        age_conv = self.df.groupby('age_group')['converted'].agg(['sum', 'count'])
        age_conv['rate'] = (age_conv['sum'] / age_conv['count'] * 100).round(2)
        
        colors = sns.color_palette("viridis", len(age_conv))
        bars = ax.bar(age_conv.index, age_conv['rate'], color=colors, edgecolor='black', linewidth=1.2)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        ax.set_xlabel('Age Group', fontsize=12, fontweight='bold')
        ax.set_ylabel('Conversion Rate (%)', fontsize=12, fontweight='bold')
        ax.set_title('Conversion Rate by Age Group', fontsize=14, fontweight='bold', pad=20)
        ax.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'conversion_by_age.png', dpi=300, bbox_inches='tight')
        print(f"Saved: conversion_by_age.png")
        plt.close()
        
    def plot_channel_performance(self):
        """Plot performance by marketing channel"""
        if 'contact' not in self.df.columns:
            print("Contact channel column not found")
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        channel_stats = self.df.groupby('contact').agg({
            'converted': ['sum', 'count']
        })
        channel_stats.columns = ['conversions', 'total_contacts']
        channel_stats['conversion_rate'] = (channel_stats['conversions'] / 
                                            channel_stats['total_contacts'] * 100).round(2)
        
        # Plot 1: Total contacts by channel
        colors1 = sns.color_palette("Set2", len(channel_stats))
        bars1 = ax1.bar(channel_stats.index, channel_stats['total_contacts'], 
                       color=colors1, edgecolor='black', linewidth=1.2)
        ax1.set_xlabel('Channel', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Total Contacts', fontsize=12, fontweight='bold')
        ax1.set_title('Campaign Volume by Channel', fontsize=13, fontweight='bold')
        
        for bar in bars1:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height):,}', ha='center', va='bottom', fontsize=10)
        
        # Plot 2: Conversion rate by channel
        colors2 = sns.color_palette("coolwarm", len(channel_stats))
        bars2 = ax2.bar(channel_stats.index, channel_stats['conversion_rate'], 
                       color=colors2, edgecolor='black', linewidth=1.2)
        ax2.set_xlabel('Channel', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Conversion Rate (%)', fontsize=12, fontweight='bold')
        ax2.set_title('Conversion Rate by Channel', fontsize=13, fontweight='bold')
        
        for bar in bars2:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'channel_performance.png', dpi=300, bbox_inches='tight')
        print(f"Saved: channel_performance.png")
        plt.close()
        
    def plot_campaign_frequency(self):
        """Plot conversion rate by campaign contact frequency"""
        if 'campaign' not in self.df.columns:
            print("Campaign column not found")
            return
        
        # Group campaign contacts into bins
        campaign_bins = [0, 1, 2, 3, 5, 10, 100]
        campaign_labels = ['1', '2', '3', '4-5', '6-10', '10+']
        self.df['campaign_group'] = pd.cut(self.df['campaign'], bins=campaign_bins, 
                                           labels=campaign_labels, include_lowest=True)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        campaign_conv = self.df.groupby('campaign_group')['converted'].agg(['sum', 'count'])
        campaign_conv['rate'] = (campaign_conv['sum'] / campaign_conv['count'] * 100).round(2)
        
        colors = sns.color_palette("rocket", len(campaign_conv))
        bars = ax.bar(range(len(campaign_conv)), campaign_conv['rate'], 
                     color=colors, edgecolor='black', linewidth=1.2)
        
        ax.set_xticks(range(len(campaign_conv)))
        ax.set_xticklabels(campaign_conv.index)
        ax.set_xlabel('Number of Contacts', fontsize=12, fontweight='bold')
        ax.set_ylabel('Conversion Rate (%)', fontsize=12, fontweight='bold')
        ax.set_title('Campaign Effectiveness by Contact Frequency', fontsize=14, fontweight='bold', pad=20)
        
        for i, bar in enumerate(bars):
            height = bar.get_height()
            count = campaign_conv.iloc[i]['count']
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%\n(n={count:,})', ha='center', va='bottom', fontsize=9)
        
        ax.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(self.output_dir / 'campaign_frequency.png', dpi=300, bbox_inches='tight')
        print(f"Saved: campaign_frequency.png")
        plt.close()

    def plot_monthly_trends(self):
        """Plot conversion trends by month"""
        if 'month' not in self.df.columns:
            print("Month column not found")
            return
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        month_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
                      'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        
        monthly_stats = self.df.groupby('month')['converted'].agg(['sum', 'count'])
        monthly_stats['rate'] = (monthly_stats['sum'] / monthly_stats['count'] * 100).round(2)
        monthly_stats = monthly_stats.reindex([m for m in month_order if m in monthly_stats.index])
        
        ax.plot(range(len(monthly_stats)), monthly_stats['rate'], 
               marker='o', linewidth=2.5, markersize=8, color='#2E86AB')
        ax.fill_between(range(len(monthly_stats)), monthly_stats['rate'], alpha=0.3, color='#2E86AB')
        
        ax.set_xticks(range(len(monthly_stats)))
        ax.set_xticklabels([m.upper() for m in monthly_stats.index], rotation=45)
        ax.set_xlabel('Month', fontsize=12, fontweight='bold')
        ax.set_ylabel('Conversion Rate (%)', fontsize=12, fontweight='bold')
        ax.set_title('Monthly Campaign Performance Trends', fontsize=14, fontweight='bold', pad=20)
        ax.grid(True, alpha=0.3)
        
        # Add value labels
        for i, (idx, row) in enumerate(monthly_stats.iterrows()):
            ax.text(i, row['rate'], f"{row['rate']:.1f}%", 
                   ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / 'monthly_trends.png', dpi=300, bbox_inches='tight')
        print(f"Saved: monthly_trends.png")
        plt.close()
        
    def plot_education_impact(self):
        """Plot conversion rate by education level"""
        if 'education' not in self.df.columns:
            print("Education column not found")
            return
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        edu_conv = self.df.groupby('education')['converted'].agg(['sum', 'count'])
        edu_conv['rate'] = (edu_conv['sum'] / edu_conv['count'] * 100).round(2)
        edu_conv = edu_conv.sort_values('rate', ascending=True)
        
        colors = sns.color_palette("mako", len(edu_conv))
        bars = ax.barh(range(len(edu_conv)), edu_conv['rate'], color=colors, 
                      edgecolor='black', linewidth=1.2)
        
        ax.set_yticks(range(len(edu_conv)))
        ax.set_yticklabels(edu_conv.index)
        ax.set_xlabel('Conversion Rate (%)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Education Level', fontsize=12, fontweight='bold')
        ax.set_title('Conversion Rate by Education Level', fontsize=14, fontweight='bold', pad=20)
        
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2.,
                   f' {width:.1f}%', ha='left', va='center', fontsize=10, fontweight='bold')
        
        ax.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.savefig(self.output_dir / 'education_impact.png', dpi=300, bbox_inches='tight')
        print(f"Saved: education_impact.png")
        plt.close()
        
    def plot_job_analysis(self):
        """Plot conversion rate by job type"""
        if 'job' not in self.df.columns:
            print("Job column not found")
            return
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        job_conv = self.df.groupby('job')['converted'].agg(['sum', 'count'])
        job_conv['rate'] = (job_conv['sum'] / job_conv['count'] * 100).round(2)
        job_conv = job_conv.sort_values('rate', ascending=True)
        
        colors = sns.color_palette("Spectral", len(job_conv))
        bars = ax.barh(range(len(job_conv)), job_conv['rate'], color=colors,
                      edgecolor='black', linewidth=1.2)
        
        ax.set_yticks(range(len(job_conv)))
        ax.set_yticklabels(job_conv.index)
        ax.set_xlabel('Conversion Rate (%)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Job Type', fontsize=12, fontweight='bold')
        ax.set_title('Conversion Rate by Job Type', fontsize=14, fontweight='bold', pad=20)
        
        for i, bar in enumerate(bars):
            width = bar.get_width()
            count = job_conv.iloc[i]['count']
            ax.text(width, bar.get_y() + bar.get_height()/2.,
                   f' {width:.1f}% (n={count:,})', ha='left', va='center', fontsize=9)
        
        ax.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.savefig(self.output_dir / 'job_analysis.png', dpi=300, bbox_inches='tight')
        print(f"Saved: job_analysis.png")
        plt.close()
        
    def create_dashboard_summary(self):
        """Create a comprehensive dashboard summary"""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
        
        # KPI Summary
        ax1 = fig.add_subplot(gs[0, :])
        ax1.axis('off')
        
        total_contacts = len(self.df)
        total_conversions = self.df['converted'].sum()
        conversion_rate = (total_conversions / total_contacts * 100)
        
        kpi_text = f"""
        MARKETING CAMPAIGN DASHBOARD - KEY METRICS
        
        Total Contacts: {total_contacts:,}  |  Total Conversions: {total_conversions:,}  |  Overall Conversion Rate: {conversion_rate:.2f}%
        """
        ax1.text(0.5, 0.5, kpi_text, ha='center', va='center', fontsize=14, 
                fontweight='bold', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        # Age group performance
        if 'age_group' in self.df.columns:
            ax2 = fig.add_subplot(gs[1, 0])
            age_conv = self.df.groupby('age_group')['converted'].mean() * 100
            age_conv.plot(kind='bar', ax=ax2, color='skyblue', edgecolor='black')
            ax2.set_title('Conversion by Age', fontweight='bold')
            ax2.set_ylabel('Rate (%)')
            ax2.tick_params(axis='x', rotation=45)
        
        # Channel performance
        if 'contact' in self.df.columns:
            ax3 = fig.add_subplot(gs[1, 1])
            channel_conv = self.df.groupby('contact')['converted'].mean() * 100
            channel_conv.plot(kind='bar', ax=ax3, color='lightcoral', edgecolor='black')
            ax3.set_title('Conversion by Channel', fontweight='bold')
            ax3.set_ylabel('Rate (%)')
            ax3.tick_params(axis='x', rotation=45)
        
        # Monthly trends
        if 'month' in self.df.columns:
            ax4 = fig.add_subplot(gs[1, 2])
            month_conv = self.df.groupby('month')['converted'].mean() * 100
            ax4.plot(month_conv.values, marker='o', color='green', linewidth=2)
            ax4.set_title('Monthly Trends', fontweight='bold')
            ax4.set_ylabel('Rate (%)')
            ax4.grid(True, alpha=0.3)
        
        # Education impact
        if 'education' in self.df.columns:
            ax5 = fig.add_subplot(gs[2, :2])
            edu_conv = self.df.groupby('education')['converted'].mean() * 100
            edu_conv = edu_conv.sort_values(ascending=True)
            edu_conv.plot(kind='barh', ax=ax5, color='orange', edgecolor='black')
            ax5.set_title('Conversion by Education Level', fontweight='bold')
            ax5.set_xlabel('Rate (%)')
        
        # Campaign frequency
        if 'campaign' in self.df.columns:
            ax6 = fig.add_subplot(gs[2, 2])
            campaign_bins = [0, 1, 2, 3, 5, 10, 100]
            self.df['camp_group'] = pd.cut(self.df['campaign'], bins=campaign_bins)
            camp_conv = self.df.groupby('camp_group')['converted'].mean() * 100
            camp_conv.plot(kind='bar', ax=ax6, color='purple', edgecolor='black')
            ax6.set_title('Contact Frequency Impact', fontweight='bold')
            ax6.set_ylabel('Rate (%)')
            ax6.tick_params(axis='x', rotation=45)
        
        plt.savefig(self.output_dir / 'dashboard_summary.png', dpi=300, bbox_inches='tight')
        print(f"Saved: dashboard_summary.png")
        plt.close()
        
    def generate_all_visualizations(self):
        """Generate all visualizations"""
        print("\nGenerating visualizations...")
        self.plot_conversion_by_age()
        self.plot_channel_performance()
        self.plot_campaign_frequency()
        self.plot_monthly_trends()
        self.plot_education_impact()
        self.plot_job_analysis()
        self.create_dashboard_summary()
        print("\nAll visualizations generated successfully!")

if __name__ == "__main__":
    df = pd.read_csv("data/processed_data.csv")
    visualizer = CampaignVisualizer(df)
    visualizer.generate_all_visualizations()
