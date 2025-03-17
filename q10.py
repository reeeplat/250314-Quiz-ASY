# Seaborn 라이브러리 import 하기 
import seaborn as sns 
import matplotlib.pyplot as plt 

# seaborn의 load_dataset을 사용하여 'tips' 데이터 불러오기
df = sns.load_dataset('tip') 

# 전체 데이터에서 처음 5개의 row 데이터 표시 (내용 확인)
# 데이터에 대한 정보를 알고 싶은 경우, 주석을 풀어 확인
# print(df.head())

# x축에 해당되는 데이터로 df의 'total_bill' 컬럼을 x_data으로 저장 
x_data = df('total_bill')
# y축에 해당되는 데이터로 df의 'tip' 컬럼을 y_data으로 저장 
y_data = df['tip']

# regplot함수의 출력물을 sns_plot으로 저장
# line의 색은 'red' 로 설정
sns_plot = sns.regplot(x_data,y_data,linecolor = 'red')

# 엘리스 플랫폼 내의 출력을 위한 함수
fig = sns_plot.get_figure()
fig.savefig("plot.png")
plt.show()