# facetgrid.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터셋 로드
# tips : 다양한 상황에서 식사금액과 팁의 관계
tips = sns.load_dataset("tips")

# 2. 기본 스타일 설정
sns.set_theme(style="dark",
              palette="pastel")

# 3. 그래프 표시
g = sns.FacetGrid(tips,
                  col="sex", row='time',
                  height=3.5,
                  aspect=0.95)

g.map_dataframe(sns.scatterplot,
                x="total_bill",y="tip")

plt.show()