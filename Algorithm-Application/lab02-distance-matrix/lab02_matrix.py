import math as ma
import numpy as np
import sklearn.metrics as sk
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

def euclidean_distance(va, vb):
    ret = 0
    for i in range(np.size(va, 0)):
        ret += (va[i] - vb[i]) ** 2
    ret = ma.sqrt(ret)
    return ret

def manhattan_distance(va, vb):
    ret = 0
    for i in range(np.size(va, 0)):
        ret += abs(va[i] - vb[i])
    return ret

''' 데이터 가공하기 '''
processed_data = list()
matrix = list()
data_matrix = np.empty((0, 13), int)
data = open('.\seoul_tax.txt', 'r', encoding='utf-8').read()
data = data.replace('\t', ' ') # tab to space
data = data.replace('\n', ' ').replace('  ', ' ').split(' ') # split by new-line : {depart} {gender} [0 1 2 3 ... 100]
del data[len(data) - 1]

for i in range(len(data)):
    if data[i].isdigit():
        processed_data.append(float(data[i]))

for i in range(0, len(processed_data), 13):
    matrix.append(processed_data[i:i+13])

for i in range(len(matrix)):
    data_matrix = np.append(data_matrix, np.array([matrix[i]]), axis=0)

print(type(data_matrix[1][1]))

''' scaled data '''
scaler = MinMaxScaler()
scaled_data_matrix = scaler.fit_transform(data_matrix)

''' raw-distance '''
# cosine distance
cosine_raw = sk.pairwise.cosine_distances(data_matrix)

# eculidean distance
euclidean_raw = [[0 for i in range(25)] for j in range(25)]
for i in range(len(data_matrix)):
    for j in range(len(data_matrix)):
        euclidean_raw[i][j] = euclidean_distance(data_matrix[i], data_matrix[j])

# manharran distance
manhattan_raw = [[0 for i in range(25)] for j in range(25)]
for i in range(len(data_matrix)):
    for j in range(len(data_matrix)):
        manhattan_raw[i][j] = manhattan_distance(data_matrix[i], data_matrix[j])

''' normalized-distance '''
# cosine distance
cosine_scale = sk.pairwise.cosine_distances(scaled_data_matrix)

# eculidean distance
euclidean_scale = [[0 for i in range(25)] for j in range(25)]
for i in range(len(scaled_data_matrix)):
    for j in range(len(scaled_data_matrix)):
        euclidean_scale[i][j] = euclidean_distance(scaled_data_matrix[i], scaled_data_matrix[j])

# manharran distance
manhattan_scale = [[0 for i in range(25)] for j in range(25)]
for i in range(len(scaled_data_matrix)):
    for j in range(len(scaled_data_matrix)):
        manhattan_scale[i][j] = manhattan_distance(scaled_data_matrix[i], scaled_data_matrix[j])

# 합산된 데이터를 그래프로 그리기
plt.figure(figsize=(15, 8))

''' raw data '''
ax1 = plt.subplot(2, 3, 1)
graph1 = plt.pcolor(cosine_raw)
plt.title('cosine-raw')
plt.colorbar()

ax2 = plt.subplot(2, 3, 2)
graph2 = plt.pcolor(euclidean_raw)
plt.title('eculidean-raw')
plt.colorbar()

ax3 = plt.subplot(2, 3, 3)
graph3 = plt.pcolor(manhattan_raw)
plt.title('manhattan-raw')
plt.colorbar()

''' scaled data '''
ax4 = plt.subplot(2, 3, 4)
graph4 = plt.pcolor(cosine_scale)
plt.title('cosine-scale')
plt.colorbar()

ax5 = plt.subplot(2, 3, 5)
graph5 = plt.pcolor(euclidean_scale)
plt.title('eculidean-scale')
plt.colorbar()

ax6 = plt.subplot(2, 3, 6)
graph6 = plt.pcolor(manhattan_scale)
plt.title('manhattan-scale')
plt.colorbar()


plt.tight_layout()
plt.show()