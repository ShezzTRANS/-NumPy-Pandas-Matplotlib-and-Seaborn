"""
Seaborn Examples - Statistical Data Visualization
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def setup_style():
    """Set up Seaborn style."""
    sns.set_theme(style="whitegrid")
    sns.set_palette("husl")


def distribution_plot():
    """Demonstrate distribution plots."""
    print("Creating distribution plot...")
    
    np.random.seed(42)
    data = np.random.randn(1000)
    
    plt.figure(figsize=(12, 5))
    
    # Histogram with KDE
    plt.subplot(1, 2, 1)
    sns.histplot(data, kde=True, color='skyblue', bins=30)
    plt.title('Histogram with KDE', fontsize=14, fontweight='bold')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    
    # KDE Plot
    plt.subplot(1, 2, 2)
    sns.kdeplot(data, fill=True, color='coral')
    plt.title('Kernel Density Estimate', fontsize=14, fontweight='bold')
    plt.xlabel('Value')
    plt.ylabel('Density')
    
    plt.tight_layout()
    plt.savefig('seaborn_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Distribution plot saved as 'seaborn_distribution.png'")


def scatter_plot_with_regression():
    """Demonstrate scatter plot with regression line."""
    print("Creating scatter plot with regression...")
    
    np.random.seed(42)
    x = np.random.randn(100)
    y = 2 * x + np.random.randn(100) * 0.5
    
    data = pd.DataFrame({'X': x, 'Y': y})
    
    plt.figure(figsize=(10, 6))
    sns.regplot(data=data, x='X', y='Y', scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})
    plt.title('Scatter Plot with Regression Line', fontsize=16, fontweight='bold')
    plt.xlabel('X values', fontsize=12)
    plt.ylabel('Y values', fontsize=12)
    
    plt.savefig('seaborn_regression.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Regression plot saved as 'seaborn_regression.png'")


def box_violin_plots():
    """Demonstrate box and violin plots."""
    print("Creating box and violin plots...")
    
    # Create sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'Category': np.repeat(['A', 'B', 'C', 'D'], 50),
        'Value': np.concatenate([
            np.random.normal(10, 2, 50),
            np.random.normal(15, 3, 50),
            np.random.normal(12, 2.5, 50),
            np.random.normal(18, 4, 50)
        ])
    })
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Box plot
    sns.boxplot(data=data, x='Category', y='Value', ax=axes[0], hue='Category', palette='Set2', legend=False)
    axes[0].set_title('Box Plot by Category', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Category', fontsize=12)
    axes[0].set_ylabel('Value', fontsize=12)
    
    # Violin plot
    sns.violinplot(data=data, x='Category', y='Value', ax=axes[1], hue='Category', palette='Set3', legend=False)
    axes[1].set_title('Violin Plot by Category', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Category', fontsize=12)
    axes[1].set_ylabel('Value', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('seaborn_box_violin.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Box and violin plots saved as 'seaborn_box_violin.png'")


def heatmap_correlation():
    """Demonstrate correlation heatmap."""
    print("Creating correlation heatmap...")
    
    # Create sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'A': np.random.randn(100),
        'B': np.random.randn(100),
        'C': np.random.randn(100),
        'D': np.random.randn(100)
    })
    
    # Add some correlation
    data['B'] = data['A'] + np.random.randn(100) * 0.5
    data['C'] = -data['A'] + np.random.randn(100) * 0.5
    
    # Calculate correlation matrix
    corr_matrix = data.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Heatmap', fontsize=16, fontweight='bold')
    
    plt.savefig('seaborn_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Correlation heatmap saved as 'seaborn_heatmap.png'")


def pair_plot():
    """Demonstrate pair plot."""
    print("Creating pair plot...")
    
    # Create sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'Feature1': np.random.randn(100),
        'Feature2': np.random.randn(100),
        'Feature3': np.random.randn(100),
        'Category': np.random.choice(['A', 'B', 'C'], 100)
    })
    
    # Add some relationship
    data['Feature2'] = data['Feature1'] * 0.5 + np.random.randn(100) * 0.5
    data['Feature3'] = -data['Feature1'] * 0.3 + np.random.randn(100) * 0.7
    
    pair_grid = sns.pairplot(data, hue='Category', diag_kind='kde', 
                             palette='husl', plot_kws={'alpha': 0.6})
    pair_grid.fig.suptitle('Pair Plot with Categories', y=1.02, fontsize=16, fontweight='bold')
    
    plt.savefig('seaborn_pairplot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Pair plot saved as 'seaborn_pairplot.png'")


def count_plot():
    """Demonstrate count plot."""
    print("Creating count plot...")
    
    # Create sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'Category': np.random.choice(['Type A', 'Type B', 'Type C', 'Type D'], 200),
        'Group': np.random.choice(['Group 1', 'Group 2'], 200)
    })
    
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Category', hue='Group', palette='Set2')
    plt.title('Count Plot by Category and Group', fontsize=16, fontweight='bold')
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.legend(title='Group')
    
    plt.savefig('seaborn_countplot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Count plot saved as 'seaborn_countplot.png'")


def line_plot():
    """Demonstrate line plot."""
    print("Creating line plot...")
    
    # Create time series data
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'Value1': np.cumsum(np.random.randn(100)) + 100,
        'Value2': np.cumsum(np.random.randn(100)) + 100
    })
    
    # Melt data for seaborn
    data_melted = data.melt(id_vars='Date', var_name='Series', value_name='Value')
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data_melted, x='Date', y='Value', hue='Series', linewidth=2)
    plt.title('Time Series Line Plot', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title='Series')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('seaborn_lineplot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Line plot saved as 'seaborn_lineplot.png'")


def categorical_plot():
    """Demonstrate categorical plots."""
    print("Creating categorical plots...")
    
    # Create sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'Category': np.repeat(['A', 'B', 'C'], 30),
        'Value': np.concatenate([
            np.random.normal(20, 5, 30),
            np.random.normal(30, 7, 30),
            np.random.normal(25, 6, 30)
        ]),
        'Type': np.tile(['Type 1', 'Type 2', 'Type 3'], 30)
    })
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    # Bar plot
    sns.barplot(data=data, x='Category', y='Value', ax=axes[0, 0], hue='Category', palette='pastel', errorbar=('ci', 95), legend=False)
    axes[0, 0].set_title('Bar Plot with Confidence Interval', fontsize=12, fontweight='bold')
    
    # Point plot
    sns.pointplot(data=data, x='Category', y='Value', hue='Type', ax=axes[0, 1], palette='dark')
    axes[0, 1].set_title('Point Plot with Categories', fontsize=12, fontweight='bold')
    
    # Strip plot
    sns.stripplot(data=data, x='Category', y='Value', ax=axes[1, 0], hue='Category', palette='muted', alpha=0.6, legend=False)
    axes[1, 0].set_title('Strip Plot', fontsize=12, fontweight='bold')
    
    # Swarm plot
    sns.swarmplot(data=data, x='Category', y='Value', ax=axes[1, 1], hue='Category', palette='bright', size=3, legend=False)
    axes[1, 1].set_title('Swarm Plot', fontsize=12, fontweight='bold')
    
    plt.suptitle('Categorical Plots Comparison', fontsize=16, fontweight='bold', y=1.00)
    plt.tight_layout()
    plt.savefig('seaborn_categorical.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Categorical plots saved as 'seaborn_categorical.png'")


if __name__ == "__main__":
    print("=" * 60)
    print("Seaborn Examples")
    print("=" * 60)
    print()
    
    setup_style()
    
    distribution_plot()
    scatter_plot_with_regression()
    box_violin_plots()
    heatmap_correlation()
    pair_plot()
    count_plot()
    line_plot()
    categorical_plot()
    
    print()
    print("=" * 60)
    print("All Seaborn examples completed successfully!")
    print("All plots saved as PNG files in the current directory.")
    print("=" * 60)
