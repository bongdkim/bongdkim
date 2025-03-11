import pandas as pd
import matplotlib.pyplot as plt
training_data = pd.read_csv('training_data.csv')
# training_data = pd.read_csv('training_data.csv', encoding='ISO-8859-1') # 1400만개짜리 셀
# print(training_data)
# print(training_data['wl_county_code'].value_counts())
print(training_data.columns)
print(training_data.head())
print(training_data.info())
print(training_data.describe())
# 여기서부터 안됨
training_data.hist(bins=20, figsize=(8,8))
plt.show()