import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# from scipy import linalg
# help(linalg)
# help(linalg.inv)

# from scipy import source    # позволяет заглянуть в код
# source(linalg.inv)
# ====================================================================================================================

# from scipy import special
#
# sinus = special.sindg(90)   # синус 90 градусов
# print(sinus)
# ====================================================================================================================


# from scipy import integrate
#
#
# def target_f(x):
#     return 3.0 * x ** 2
#
#
# result = integrate.quad(target_f, 0.0, 4.0)  # прикольно, где я был раньше
# print(result)  # (64.0, 7.105427357601002e-13) - это (ответ, точность вычислений)
# ====================================================================================================================


# def target_func(y, x):
#     return -2.0 * y
#
# xi = np.linspace(0,1,10)
# y0 = 1.0
# result1 = integrate.odeint(target_func, y0, xi)
# print(result1)  # столбец, в котором хранятся значения искомой ф-ии, начиная с y0
# # [[1.        ]
# #  [0.80073742]
# #  [0.64118042]
# #  [0.51341714]
# #  [0.41111231]
# #  [0.329193  ]
# #  [0.26359714]
# #  [0.21107209]
# #  [0.16901331]
# #  [0.13533527]]
# ====================================================================================================================


# from scipy import interpolate
#
# x = np.arange(5, 20)
# y = np.exp(x / 3.0)
#
# f = interpolate.interp1d(x, y)
#
# x1 = np.arange(6, 20)
# y1 = f(x1)
#
# plt.plot(x, y, 'o', x1, y1, '--')
# plt.show()
# ====================================================================================================================


# from scipy.interpolate import interp1d
#
# def f_exact(x):
#     return np.sin(x) ** 2
#
# x = np.linspace(0, 2.0 * np.pi, 10)
# y = f_exact(x)
#
# f1 = interp1d(x, y)
# f2 = interp1d(x, y, 'cubic')
#
# xi = np.linspace(0, 2.0 * np.pi, 25)
# y1 = f1(xi)
# y2 = f2(xi)
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.ylim(0.0, 1.5)
#
# plt.plot(x, y, 'o', label='исходные данные')
# plt.plot(xi, f_exact(xi), '-', color='grey', label='точная ф-ия')
# plt.plot(xi, y1, '--', label='линейная')
# plt.plot(xi, y2, 'k:', label='кубическая')
# plt.legend(loc='upper center')
# plt.show()
# ====================================================================================================================

#
# from scipy import optimize
#
#
# def target_f(x):
#     return x ** 2 + 10 * np.sin(x)
#
# plt.figure(figsize=(10, 5))
# x = np.arange(-10, 10, 0.1)
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('optimize')
# plt.plot(x, target_f(x), 'r-', label='$x^2+10sin(x)$')
# # a = f(-1.3)
#
# plt.annotate('min', xy=(-1.3, a), xytext=(3, 40), arrowprops=dict(facecolor='black', shrink=0.5))
# plt.legend()
# plt.show()

# ====================================================================================================================