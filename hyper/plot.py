import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# content of results_s_q.csv
# gorModel; score; value; windowsize
# gor1; SOV mean; 57.1; 13
# gor1; Q3 mean; 60.4; 13
# gor1; SOV mean; 57.2; 15
# gor1; Q3 mean; 60.5; 15
# gor1; SOV mean; 55.1; 21
# gor1; Q3 mean; 57.1; 21
# gor1; SOV mean; 53.5; 23
# gor1; Q3 mean; 55.3; 23
# gor1; SOV mean; 47.7; 31
# gor1; Q3 mean; 49.2; 31
# gor3; SOV mean; 42.6; 13
# gor3; Q3 mean; 57.1; 13
# gor3; SOV mean; 42.2; 15
# gor3; Q3 mean; 57.2; 15
# gor3; SOV mean; 41.0; 21
# gor3; Q3 mean; 54.4; 21
# gor3; SOV mean; 40.1; 23
# gor3; Q3 mean; 52.8; 23
# gor3; SOV mean; 36.3; 31
# gor3; Q3 mean; 47.0; 31
# gor4; SOV mean; 34.7; 13
# gor4; Q3 mean; 46.3; 13
# gor4; SOV mean; 34.2; 15
# gor4; Q3 mean; 45.8; 15
# gor4; SOV mean; 32.2; 21
# gor4; Q3 mean; 41.9; 21
# gor4; SOV mean; 31.3; 23
# gor4; Q3 mean; 40.4; 23
# gor4; SOV mean; 27.6; 31
# gor4; Q3 mean; 35.2; 31
# gor5_1; SOV mean; 61.7; 13
# gor5_1; Q3 mean; 65.1; 13
# gor5_1; SOV mean; 61.6; 15
# gor5_1; Q3 mean; 65.2; 15
# gor5_1; SOV mean; 58.5; 21
# gor5_1; Q3 mean; 61.1; 21
# gor5_1; SOV mean; 57.1; 23
# gor5_1; Q3 mean; 59.3; 23
# gor5_1; SOV mean; 50.7; 31
# gor5_1; Q3 mean; 52.7; 31
# gor5_3; SOV mean; 48.9; 13
# gor5_3; Q3 mean; 62.2; 13
# gor5_3; SOV mean; 48.9; 15
# gor5_3; Q3 mean; 62.3; 15
# gor5_3; SOV mean; 47.3; 21
# gor5_3; Q3 mean; 59.2; 21
# gor5_3; SOV mean; 46.3; 23
# gor5_3; Q3 mean; 57.3; 23
# gor5_3; SOV mean; 41.5; 31
# gor5_3; Q3 mean; 51.1; 31
# gor5_4; SOV mean; 30.9; 13
# gor5_4; Q3 mean; 43.7; 13
# gor5_4; SOV mean; 30.4; 15
# gor5_4; Q3 mean; 43.3; 15
# gor5_4; SOV mean; 28.9; 21
# gor5_4; Q3 mean; 39.9; 21
# gor5_4; SOV mean; 28.1; 23
# gor5_4; Q3 mean; 38.5; 23
# gor5_4; SOV mean; 24.9; 31
# gor5_4; Q3 mean; 33.7; 31

    
if __name__ == "__main__":
    data = pd.read_csv("results_s_q.csv", delimiter=";")


    # plot the SOV
    sns.set_palette("colorblind")
    sns.set_theme("poster")
    sns.set_style("ticks")
    # Create the bar plot with custom error bars and hue="Model"
    plt.figure(figsize=(12, 8))

    sns.lineplot(x="windowsize", y="value", hue="gorModel", data=data[data["score"] == "SOV mean"], marker="o")
    plt.title("SOV mean", fontsize=17)
    plt.xlabel("Windowsize", fontsize=17)
    plt.ylabel("Score", fontsize=17)

    # make x ticks bigger
    plt.xticks(fontsize=14)
    # make y ticks bigger
    plt.yticks(fontsize=14)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.grid(True)  # Enable grid lines
    plt.show()

    # plot the Q3
    sns.set_palette("colorblind")
    sns.set_theme("poster")
    sns.set_style("ticks")
    # Create the bar plot with custom error bars and hue="Model"
    plt.figure(figsize=(12, 8))

    sns.lineplot(x="windowsize", y="value", hue="gorModel", data=data[data["score"] == "Q3 mean"], marker="o")
    plt.title("SOV mean", fontsize=17)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel("Windowsize", fontsize=17)
    plt.ylabel("Score", fontsize=17)

    # make x ticks bigger
    plt.xticks(fontsize=14)
    # make y ticks bigger
    plt.yticks(fontsize=14)
    plt.grid(True)  # Enable grid lines
    plt.show()


    data = pd.read_csv("results_sov_only.csv", delimiter=";")
    # plot the SOV_E mean
    sns.set_palette("colorblind")
    sns.set_theme("poster")
    sns.set_style("ticks")
    sns.lineplot(x="windowsize", y="value", hue="gorModel", data=data[data["score"] == "SOV_E mean"], marker="o")
    plt.title("SOV_E mean", fontsize=17)
    plt.xlabel("Windowsize", fontsize=17)
    plt.ylabel("Score", fontsize=17)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.grid(True)  # Enable grid lines
    # make x ticks bigger
    plt.xticks(fontsize=14)
    # make y ticks bigger
    plt.yticks(fontsize=14)
    plt.show()


    sns.set_palette("colorblind")
    sns.set_theme("poster")
    sns.set_style("ticks")
    sns.lineplot(x="windowsize", y="value", hue="gorModel", data=data[data["score"] == "SOV_H mean"], marker="o")
    plt.title("SOV_H mean", fontsize=17)
    plt.xlabel("Windowsize", fontsize=17)
    plt.ylabel("Score", fontsize=17)
    plt.grid(True)  # Enable grid lines

    # position the legend to the right outer side
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # make x ticks bigger
    plt.xticks(fontsize=14)
    # make y ticks bigger
    plt.yticks(fontsize=14)
    plt.show()









    
