"""
Matplotlib Examples - Data Visualization
"""

import matplotlib.pyplot as plt
import numpy as np


def line_plot():
    """Demonstrate basic line plot."""
    print("Creating line plot...")
    
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='sin(x)', linewidth=2)
    plt.plot(x, y2, label='cos(x)', linewidth=2, linestyle='--')
    
    plt.title('Sine and Cosine Functions', fontsize=16, fontweight='bold')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    
    plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Line plot saved as 'line_plot.png'")


def scatter_plot():
    """Demonstrate scatter plot."""
    print("Creating scatter plot...")
    
    np.random.seed(42)
    x = np.random.randn(100)
    y = 2 * x + np.random.randn(100) * 0.5
    colors = np.random.rand(100)
    sizes = 1000 * np.random.rand(100)
    
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
    
    plt.title('Scatter Plot with Variable Colors and Sizes', fontsize=16, fontweight='bold')
    plt.xlabel('X values', fontsize=12)
    plt.ylabel('Y values', fontsize=12)
    plt.colorbar(scatter, label='Color Scale')
    plt.grid(True, alpha=0.3)
    
    plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Scatter plot saved as 'scatter_plot.png'")


def bar_chart():
    """Demonstrate bar chart."""
    print("Creating bar chart...")
    
    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    values = [23, 45, 56, 78, 32]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, values, color=colors, edgecolor='black', linewidth=1.2)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plt.title('Bar Chart Example', fontsize=16, fontweight='bold')
    plt.xlabel('Categories', fontsize=12)
    plt.ylabel('Values', fontsize=12)
    plt.ylim(0, max(values) * 1.1)
    plt.grid(axis='y', alpha=0.3)
    
    plt.savefig('bar_chart.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Bar chart saved as 'bar_chart.png'")


def histogram():
    """Demonstrate histogram."""
    print("Creating histogram...")
    
    np.random.seed(42)
    data = np.random.randn(1000)
    
    plt.figure(figsize=(10, 6))
    n, bins, patches = plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    
    plt.title('Histogram of Random Data', fontsize=16, fontweight='bold')
    plt.xlabel('Value', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    
    # Add mean line
    mean_val = np.mean(data)
    plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
    plt.legend()
    
    plt.savefig('histogram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Histogram saved as 'histogram.png'")


def pie_chart():
    """Demonstrate pie chart."""
    print("Creating pie chart...")
    
    labels = ['Python', 'JavaScript', 'Java', 'C++', 'Other']
    sizes = [35, 25, 20, 15, 5]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    explode = (0.1, 0, 0, 0, 0)  # Explode 1st slice
    
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    
    plt.title('Programming Language Distribution', fontsize=16, fontweight='bold')
    plt.axis('equal')
    
    plt.savefig('pie_chart.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Pie chart saved as 'pie_chart.png'")


def subplots_example():
    """Demonstrate subplots."""
    print("Creating subplots...")
    
    x = np.linspace(0, 10, 100)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Multiple Subplots Example', fontsize=16, fontweight='bold')
    
    # Plot 1: Sine
    axes[0, 0].plot(x, np.sin(x), 'b-', linewidth=2)
    axes[0, 0].set_title('Sine Function')
    axes[0, 0].set_xlabel('x')
    axes[0, 0].set_ylabel('sin(x)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Cosine
    axes[0, 1].plot(x, np.cos(x), 'r-', linewidth=2)
    axes[0, 1].set_title('Cosine Function')
    axes[0, 1].set_xlabel('x')
    axes[0, 1].set_ylabel('cos(x)')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Exponential
    axes[1, 0].plot(x, np.exp(-x/5), 'g-', linewidth=2)
    axes[1, 0].set_title('Exponential Decay')
    axes[1, 0].set_xlabel('x')
    axes[1, 0].set_ylabel('exp(-x/5)')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Scatter
    axes[1, 1].scatter(x, np.sin(x) + np.random.randn(100) * 0.1, alpha=0.5)
    axes[1, 1].set_title('Sine with Noise')
    axes[1, 1].set_xlabel('x')
    axes[1, 1].set_ylabel('sin(x) + noise')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('subplots.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Subplots saved as 'subplots.png'")


def heatmap():
    """Demonstrate heatmap."""
    print("Creating heatmap...")
    
    np.random.seed(42)
    data = np.random.rand(10, 10)
    
    plt.figure(figsize=(10, 8))
    im = plt.imshow(data, cmap='YlOrRd', aspect='auto')
    
    plt.colorbar(im, label='Intensity')
    plt.title('Heatmap Example', fontsize=16, fontweight='bold')
    plt.xlabel('X axis', fontsize=12)
    plt.ylabel('Y axis', fontsize=12)
    
    # Add grid
    plt.grid(False)
    
    plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Heatmap saved as 'heatmap.png'")


def box_plot():
    """Demonstrate box plot."""
    print("Creating box plot...")
    
    np.random.seed(42)
    data = [np.random.normal(0, std, 100) for std in range(1, 5)]
    labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
    
    plt.figure(figsize=(10, 6))
    box = plt.boxplot(data, tick_labels=labels, patch_artist=True,
                      notch=True, showmeans=True)
    
    # Color boxes
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    plt.title('Box Plot Example', fontsize=16, fontweight='bold')
    plt.xlabel('Groups', fontsize=12)
    plt.ylabel('Values', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    
    plt.savefig('box_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Box plot saved as 'box_plot.png'")


if __name__ == "__main__":
    print("=" * 60)
    print("Matplotlib Examples")
    print("=" * 60)
    print()
    
    line_plot()
    scatter_plot()
    bar_chart()
    histogram()
    pie_chart()
    subplots_example()
    heatmap()
    box_plot()
    
    print()
    print("=" * 60)
    print("All Matplotlib examples completed successfully!")
    print("All plots saved as PNG files in the current directory.")
    print("=" * 60)
