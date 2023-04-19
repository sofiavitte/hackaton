# -*- coding: utf-8 -*-
"""subclinical_cvd_dataset.csv

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sahKvtlAFnp_52t3ZJUTbcYuvkzNF5ip
"""

import pandas as pd
target = ['yes', 'no', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes']
data = {'age': [25, 30, 40, 50, 60, 70, 80, 90, 100, 110],
        'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
        'income': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]}


df = pd.DataFrame(data)


df['subclinical_cvd'] = target


train_df = df.sample(frac=0.8, random_state=42)
test_df = df.drop(train_df.index)


train_df.to_csv('train_dataset.csv', index=False)
test_df.to_csv('test_dataset.csv', index=False)