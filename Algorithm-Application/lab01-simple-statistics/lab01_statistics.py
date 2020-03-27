import numpy as np
from matplotlib import pyplot as plt

''' 데이터 가공하기 '''
processed_data = dict()
data = open('.\seoul.txt', 'r', encoding='utf-8').read()
data = data.replace('\t', ' ') # tab to space
data = data.split('\n') # split by new-line : {depart} {gender} [0 1 2 3 ... 100]

# data processing
for i in data:
    dataline = i.replace('  ', ' ')
    dataline = dataline.split(' ')
    if (len(dataline) > 1) and (dataline[0] != '행정구역별'): # Exception Handling
        gender = '' # male / female / sum
        if dataline[1] == '남자':
            gender = 'male'
        elif dataline[1] == '여자':
            gender = 'female'
        elif dataline[1] == '계':
            processed_data[dataline[0]] = dict() # gender
            gender = 'sum'
        else:
            break
        
        processed_data[dataline[0]][gender] = list() # age
        processed_data[dataline[0]][gender] = dataline[2:len(dataline) - 1] # 0세 ~ 100세 이상



goal = dict() # 계, 남자, 여자

# 리스트 초기화
goal['sum'] = [0 for i in range(101)] # 계
goal['male'] = [0 for i in range(101)] # 남자
goal['female'] = [0 for i in range(101)] # 여자


# 합산
for i in processed_data:
    for j in range(101):
        goal['sum'][j] += int(processed_data[i]['sum'][j]) # 계
        goal['male'][j] += int(processed_data[i]['male'][j]) # 남자
        goal['female'][j] += int(processed_data[i]['female'][j]) # 여자
    

''' goal 2 : 취합된 데이터의 총합, 평균, 분산 구하기 '''
for gender in goal:
    print_gender = ''

    if gender == 'sum':
        print_gender = '계'

    elif gender == 'male':
        print_gender = '남자'

    elif gender == 'female':
        print_gender = '여자'

    print(print_gender + ' : ', end='')

    # Raw Data
    for iter in goal[gender]:
        print(str(iter) + ' ', end='')
    
    print()

    # 총합
    print(print_gender + ' 총합 : ' + str(np.sum(goal[gender])))

    # 평균
    print(print_gender + ' 평균 : ' + str(np.mean(goal[gender])))

    # 분산
    print(print_gender + ' 분산 : ' + str(np.var(goal[gender])))

    print('\n')


''' goal 1 : 행정구역 별 데이터 취합하여 그래프 그리기 '''
# 합산된 데이터를 그래프로 그리기
plt.figure(figsize=(15,4))

ax1 = plt.subplot(1, 3, 1)
ax1.set_title('SUM')
graph1 = plt.bar(np.arange(101), goal['sum'])


ax2 = plt.subplot(1, 3, 2)
ax2.set_title('MALE')
graph2 = plt.bar(np.arange(101), goal['male'])

ax3 = plt.subplot(1, 3, 3)
ax3.set_title('FEMALE')
graph3 = plt.bar(np.arange(101), goal['female'])


plt.tight_layout()
plt.show()
