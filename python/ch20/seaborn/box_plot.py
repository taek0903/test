# box_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터셋 로드
iris = sns.load_dataset("iris")

sns.boxplot(data=iris,
            x="species",
            y="sepal_length")
plt.title("Box Pliot Example")
plt.show()