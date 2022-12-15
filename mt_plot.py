import numpy as np
import pandas as pd
# import matplotlib as mt
import matplotlib.pyplot as plt

plt.style.use('ggplot')
# https://matplotlib.org/stable/tutorials/introductory/customizing.html стили


# fig, ax = plt.subplots()    # создается fig и в него помещается 1 график ax
#
#
# # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html  готовые оформленые примеры графиков
#
# fig, axes = plt.subplots(2, 2)  # создается fig и в него помещается объект axes из 4х графиков; сетка 2х2
# plt.show()
# # ================================================================================================================


# # добавление графиков по отдельности:
# figure = plt.figure()
# ax1 = figure.add_subplot(2, 2, 1)   # сетка 2х2 номер графика 1
# ax2 = figure.add_subplot(2, 2, 2)   # сетка 2х2 номер графика 2
# ax3 = figure.add_subplot(2, 2, 3)   # сетка 2х2 номер графика 3
# plt.show()
# ================================================================================================================


# fig, ax = plt.subplots()
#
# x = [-3, -2, -1, 0, 1, 2, 3]
# y = [9, 4, 1, 0, 1, 4, 9]
# ax.plot(x, y)  # если график 1 то plt.plot(x,y)
# plt.show()      # в одном Axes
# # ================================================================================================================


# fig, ax = plt.subplots()
#
# x = [-3, -2, -1, 0, 1, 2, 3]
# y = [9, 4, 1, 0, 1, 4, 9]
# x_abs = [3, 2, 1, 0, 1, 2, 3]
# ax.plot(x, y)
# ax.plot(x, x_abs)   # два графика в одном окошке
# plt.show()      # в одном Axes
# # ================================================================================================================


# # есди Axes несколько (окошек):
# fig, axes = plt.subplots(2, 2)  # указали, что сетка будет 2х2, иначе ошибка
# x = [-3, -2, -1, 0, 1, 2, 3]
# y = [9, 4, 1, 0, 1, 4, 9]
#
# axes[1, 0].plot(x, y)  # указали в каком окошке построить график axes[1,0]
# plt.show()
# # ================================================================================================================


# figure = plt.figure()
# ax1 = figure.add_subplot(2, 2, 1)
# ax2 = figure.add_subplot(2, 2, 2)
# ax3 = figure.add_subplot(2, 2, 3)
#
# x = [-3, -2, -1, 0, 1, 2, 3]
# y = [9, 4, 1, 0, 1, 4, 9]
# x_abs = [3, 2, 1, 0, 1, 2, 3]
#
# ax3.plot(x, y)
# ax1.plot(x, x_abs)
#
# plt.show()
# # ================================================================================================================


# fig, ax = plt.subplots()
#
# x = np.array([-3, -2, -1, 0, 1, 2, 3])
# y = np.array([9, 4, 1, 0, 1, 4, 9])
#
# ax.plot(x,y)
# ax.plot(x, np.sin(x), color=(1.0,0.2,0.3), linestyle='-')
# ax.plot(x, x+5, color='blue', linestyle='--')
# ax.plot(x,x+3, color='g', linestyle=':')
# ax.plot(x, np.cos(x), color='0.75', linestyle='-.')
# ax.plot(x,x,color='#FFDD44', linestyle='solid')
# plt.show()
# ================================================================================================================


# fig, ax = plt.subplots()
#
# x = np.array([-3, -2, -1, 0, 1, 2, 3])
# y = np.array([9, 4, 1, 0, 1, 4, 9])
#
# ax.plot(x, y, marker='o')
# ax.plot(0.5 * x, y, marker='^', linewidth=3.4)  # linewidth=3.4 толщина линии
# ax.plot(2 * x, y, marker='*', alpha=0.2)  # lpha=0.2 прозрачность от 0 до 1
# ax.plot(0.2 * x, y, '*--g')  # '*--g' сокращение, означает то маркер = *, тип линии = --, а цвет зеленый = g
#
# ax.set_xlim(0, 11)  # ограничение оси х
# ax.set_ylim(-5, 10)     # ограничение оси y
#
# plt.show()
# ================================================================================================================


# Подписи:
# fig, ax = plt.subplots()
#
# x = np.array([-3, -2, -1, 0, 1, 2, 3])
# y = np.array([9, 4, 1, 0, 1, 4, 9])
#
# ax.plot(x, x**2, marker='o', label='y=x**2')    # подпись линии, но она не отобразиться пока не ax.legend(loc='lower left')
#
# ax.set_title('Заголовок нашего графика', fontsize=20)
# ax.set_xlabel('Ось х')
# ax.set_ylabel('Ось y')
# ax.legend(loc='lower left')     # вывод подписи линии
#
# plt.show()
# ================================================================================================================


# Добавление сетки и дробных координатных подписей
# fig, ax = plt.subplots()
#
# x = np.array([-3, -2, -1, 0, 1, 2, 3])
# y = np.array([9, 4, 1, 0, 1, 4, 9])
#
# ax.plot(x, x**2, marker='o')
#
# ax.set_xticks(np.arange(-3,3.5,0.5))      # дробные координатные подписи
# ax.set_yticks(np.arange(0,10,3))
#
# # ax.spines['bottom'].set_visible(True)   # непонятно что делает; разницы нет никакой? это типа граници сетки grid
# ax.spines['bottom'].set_color('black')    # скорее это граница не сетки, а графика ax внутри рисунка fig
#
# ax.grid(color='blue', linewidth=2, linestyle='--')  # цвет сетки, толщина, стиль
#
# plt.show()

# help(ax.spines)
# ================================================================================================================


# сохраненяем в картинку и открываем картинку
# fig.savefig('./figure1.png')

# import matplotlib.image as mpimg
#
# img = mpimg.imread('./figure1.png')
# imgplot = plt.imshow(img)
#
# # plt.grid()
# plt.show()
# ================================================================================================================


# fig, ax = plt.subplots()
# N = 60
# x = np.random.rand(N)
# y = np.random.rand(N)
#
# colors = np.random.rand(N)
# area = (30 * np.random.rand(N)) ** 2  # размер звездочек
# ax.scatter(x, y, s=area, c=colors, alpha=0.9, marker='*', cmap='Blues')
#
# plt.show()
# ================================================================================================================


# # 3d plot
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure(figsize=(10,6))
# ax = fig.add_subplot(111, projection='3d')
#
# N = 60
# x = np.random.rand(N)
# y = np.random.rand(N)
#
# colors = np.random.rand(N)
# area = (30 * np.random.rand(N)) ** 2  # размер звездочек
# ax.scatter(x, y, s=area, c=colors, alpha=0.9, marker='*', cmap='Blues')
#
# plt.show()
# ================================================================================================================


# Бары (столбчатые диаграммы)
# fig, axes = plt.subplots(1, 2)
# axes[0].bar(
#     [1, 2, 3],
#     [4, 5, 6],
#     color='red', label='vertical bar', alpha=0.8
# )
# axes[1].barh(
#     [0.5, 1, 2.5],
#     [0, 1, 2]
# )
# axes[0].legend
# plt.show()
# ================================================================================================================


# Stacked bar chart наслаивающиеся бары
fig = plt.figure(figsize=(14, 10))
rect1 = plt.bar(np.arange(5), np.arange(5) ** 2, width=0.5, color='red')
rect2 = plt.bar(np.arange(5), np.arange(5) * 2, width=0.5, color='blue')
plt.legend(
    (rect1[0], rect2[0]),
    ('Support', 'надпись')
)
plt.show()
# ================================================================================================================


