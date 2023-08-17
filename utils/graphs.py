import numpy as np
from matplotlib import pyplot as plt


def plt_figure_show(x, height):
    plt.figure(1)
    plt.clf()
    plt.bar(x, height)
    plt.title("Feature uni-variate score")
    plt.xlabel("Feature number")
    plt.ylabel(r"Uni variate score ($-Log(p_{value})$)")
    plt.show()

def plt_figure_header_show(evaluation, evaluation_scores, header_names):
    temp_overlap_df = []
    for t in range(len(evaluation_scores)):
        overlap = np.where(evaluation == evaluation_scores[t])
        temp_overlap_df.append(overlap[0][0])

    plt.figure(figsize=(10, 5))
    plt.clf()
    index_list = []
    label_list = []
    print(temp_overlap_df)
    for i in temp_overlap_df:
        plt.bar(header_names[i], evaluation[i])
        index_list.append(header_names[i])
        label_list.append(evaluation[i])
        plt.title("Feature uni-variate")
        plt.xlabel("Feature number")
        plt.ylabel(r"Uni variate score ($-Log(p_{value})$)")
        plt.xticks(rotation=90)
        plt.subplots_adjust(bottom=0.37)
    plt.show()

