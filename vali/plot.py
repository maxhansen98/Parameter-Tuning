import pandas as pd
import matplotlib.pyplot as plt
import sys


def plot_summary_per_fold(path_to_summary: str, name_of_db: str):
    # Load the data
    data = pd.read_csv(path_to_summary, sep='\t', header=None)
    plot_title = path_to_summary.split(".")[0].split("/")[-1].replace("_SUMMARY_plot_ALL", "")
    plot_path = path_to_summary.split(".")[0] + ".png"

    # Calculate mean and standard deviation for each column
    means = data.mean()
    std_devs = data.std()
    labels = ['Q3', 'SOV', 'Q_H', 'Q_E', 'Q_C', 'SOV_H', 'SOV_E', 'SOV_C']

    # Scatter plot of means
    plt.scatter(range(len(means)), means, s=200, c='r', marker='_')

    # Error bars
    plt.errorbar(range(len(means)), means, yerr=std_devs, fmt='none', capsize=5, color='black')

    # X-axis ticks and labels
    plt.xticks(range(len(means)), labels, rotation=45)
    plt.ylim(0,100)
    plt.grid(axis='y',)

    plt.ylabel('Mean + Standard Deviation')
    plt.title(plot_title + " on " + name_of_db)
    plt.tight_layout()
    plt.savefig(plot_path)
    
if __name__ == "__main__":
    path = sys.argv[1]
    name = sys.argv[2]
    
    plot_summary_per_fold(path, name)

