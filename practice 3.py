# %%practice1

import math
print(math.pi)
print(math.e)

# %%practice2
x = 11
y = -1.11
z = 3+12j

print(type(x))
print(type(y))
print(type(z))


# %%practice3
str1 = 'i am gay'
print(str1.upper())

str2 = 'he is gay'
print(str2.title())
print(str2.capitalize())
print(str2.swapcase())
print(str2.replace('gay', 'straight'))
print(str2.find('gay'))
print(str2.count('gay'))


# %%practice4_索引
greeting_str = 'Het, James'
print(len(greeting_str))
print(greeting_str[0])
print(greeting_str[1])  

# %%practice5_
my_list = ['apple', 'banana', 'cherry']


# %% 考題一
colors = ["紅", "橙", "黃", "綠"]
for i, color in enumerate(colors, start = 1)://告訴此函數 第一個取為零 但是題目要一
    print('第[{i}]的顏色是:{colors[i]}')
# %% 考題二
nums = [3, 8, 2, 9, 4]
for i, num in enumerate(nums):
    if i % 2 == 0:
        print(f'第[{i}]個數字是:{nums[i]}')

# %% 考題三

words = ["cat", "dog", "cat", "bird", "cat"]
positions = []//用來存放所有出現的索引位置
for i, word in enumerate(words):
    if word == 'cat':
        positions.append(i)
        print(positions)

# %% 考題四
prices = [100, 250, 80, 300]
for i,n in enumerate(prices):
    prices[i] = n * 0.8
print(prices)

# %% 挑戰題目
scores = [72, 95, 63, 88, 95]
//我的思路:我這邊想到在箱子裡面有五個數 但是現在是陣列 有順序 可以有迴圈 
氣泡排序法去一個個比較+ enumerate去同時求出 最大值還有其位置
//先暫時讓第一個人當擂台主 讓他最大 後面的樹一個個上來比大小 
biggest_score = scores[0]
biggest_index = 0
for i, s in enumerate(scores):
    if s > biggest_score:
        biggest_score = s
        biggest_index = i
        print(f'目前最大分數是:{biggest_score}，位置是:{biggest_index}')





