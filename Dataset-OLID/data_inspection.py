# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import sklearn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/home/dorotea/Documents/FER/APT/TARProject/Dataset-OLID/OLIDv1.0/olid-training-v1.0.tsv', sep='\t')
data.head(10)

data.shape

dataA = data.drop(["subtask_b", "subtask_c"], axis=1)
dataB = data.drop(["subtask_a", "subtask_c"], axis=1)
dataC = data.drop(["subtask_a", "subtask_b"], axis=1)

print("A not nan:", 1-data.subtask_a.isna().sum()/13240.)
print("B not nan:", 1-data.subtask_b.isna().sum()/13240.)
print("C not nan:", 1-data.subtask_c.isna().sum()/13240.)

dataA_info = dataA.groupby(["subtask_a"]).count()
dataA_info.columns = ["Total", "Percentage"]
dataA_info.Percentage = dataA_info.Percentage/dataA_info.Percentage.sum()
dataA_info

p.apply(np.sum, axis=0)

df['ln_A'] = df['A'].apply(np...)

dataB_info = dataB.groupby(["subtask_b"]).count()
dataB_info.columns = ["Total", "Percentage"]
dataB_info.Percentage = dataB_info.Percentage/dataB_info.Percentage.sum()
dataB_info

dataC_info = dataC.groupby(["subtask_c"]).count()
dataC_info.columns = ["Total", "Percentage"]
dataC_info.Percentage = dataC_info.Percentage/dataC_info.Percentage.sum()
dataC_info
