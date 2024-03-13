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

    # now plot the data, first the SOV
    # make the x axis show the curr windowsize
    # make the outlines bold
    # the lines shouldnt be too slim
    # add a legend

    # plot the SOV and make small points of the sov mean at the windowsize
    # also plot the Q3 and make small points of the q3 mean at the windowsize

    # plot the SOV
    sns.set_style(style="whitegrid")
    sns.lineplot(x="windowsize", y="value", hue="gorModel", data=data[data["score"] == "SOV mean"], marker="o")
    plt.title("SOV mean", fontsize=17)
    plt.xlabel("Windowsize", fontsize=17)
    plt.xlabel("Score", fontsize=17)
    plt.show()

    # plot the Q3
    sns.set_style(style="whitegrid")
    sns.lineplot(x="windowsize", y="value", hue="gorModel", data=data[data["score"] == "Q3 mean"], marker="o")
    plt.title("Q3 mean", fontsize=17)
    plt.xlabel("Windowsize", fontsize=17)
    plt.xlabel("Score", fontsize=17)
    plt.show()







    
