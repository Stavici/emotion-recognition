import string

import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectKBest, SelectPercentile

from utils import graphs, tools


def variate_statistics(in_path: string, filename: string, method):
    df = pd.read_csv(f'{in_path}/{filename}.csv',
                     delimiter=',',
                     header=None,
                     index_col=False)

    data = df.iloc[1:, :-1]
    labels_data = df.iloc[1:, -1]
    header_names = df.iloc[0, :-1]

    normed_data = tools.min_max_scaler(data)

    best_features = SelectKBest(method, k='all')
    best_features.fit(normed_data, labels_data)
    evaluation = -np.log10(best_features.pvalues_)
    evaluation_scores = evaluation[evaluation[:].argsort()[::-1]]

    indices = np.arange(data.shape[-1])
    graphs.plt_figure_show(indices, evaluation_scores)
    graphs.plt_figure_header_show(evaluation, evaluation_scores, header_names)
    select = SelectPercentile(percentile=50)
    select.fit(evaluation, evaluation_scores)