# Written with love and passion by Youssef El Gharably :)

# The square has a length of 2
# The circle has a radius of 1
# The circle is centered at the origin point, and so is the square
# if x^2 + y^2 >1, then outside circle. 
# if x^2 + y^2 >= 1, then inside circle

import numpy as np
from matplotlib import pyplot as plt
import random as rand
import math
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import ttk

def throw_darts(n):
    x_values = np.random.uniform(-1, 1, size=n)
    y_values = np.random.uniform(-1, 1, size=n)
    return np.column_stack((x_values, y_values))

def check_inside_outside(lst):
    x_values = lst[:, 0]
    y_values = lst[:, 1]
    distances_squared = x_values**2 + y_values**2
    checker = distances_squared <= 1
    return checker

def count_darts(lst):
    x_values = lst[:, 0]
    y_values = lst[:, 1]
    distances_squared = x_values**2 + y_values**2
    counter_inside = np.sum(distances_squared <= 1)
    counter_outside = np.sum(distances_squared > 1)
    return [counter_inside, counter_outside]

def residuals_pi(num):
    return(num-math.pi)

def estimate_pi(lst):
    return (4*(lst[0]/(lst[0]+lst[1])))

def plot(lst, checker):
    def circle_func(x):
        return np.sqrt(1 - np.square(x))

    plt.figure(figsize=(10, 10))
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    x = np.linspace(-1, 1, 1000)
    plt.plot(x, circle_func(x), color='black')
    plt.plot(x, -circle_func(x), color='black')

    plt.scatter(lst[checker, 0], lst[checker, 1], color='royalblue', s=0.1)
    plt.scatter(lst[~checker, 0], lst[~checker, 1], color='darkred', s=0.1)

    plt.show()


def darts():
    user_input = input("Type 1 if you want to estimate a number without a plot, 2 if you only want a plot, and 3 if you want both a number and a plot: ")
    n = int(input("How many darts do you feel like throwing today? "))
    thrown_darts_coordinates = throw_darts(n)
    checker_list = check_inside_outside(thrown_darts_coordinates)

    if user_input == '1' or user_input == '3':
        print(estimate_pi(count_darts(thrown_darts_coordinates)))
    if user_input == '2' or user_input == '3':
        plot(thrown_darts_coordinates, checker_list)

           
def func(x):
    return((5*x)+(-12*x**2)+(8*x**3))

def random_coordinates(n, a, b, c, d):
    x = np.random.uniform(a, b, size=n)
    y = np.random.uniform(c, d, size=n)
    return np.column_stack((x, y))

def check_less_more(lst):
    return [lst[i][1] > func(lst[i][0]) for i in range(len(lst))]

def check_gauss(lst):
    x_values = np.array(lst)[:, 0]
    y_values = np.array(lst)[:, 1]
    gauss_values = gaussian(x_values)
    checker = y_values <= gauss_values
    return checker

def ploter(lst, check):
    x_values = np.linspace(0, 1, 1000)
    plt.figure(figsize=(10, 10))
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.plot(x_values, func(x_values), color='black')
    plt.scatter(lst[check, 0], lst[check, 1], color='darkred', s=0.1)
    plt.scatter(lst[~check, 0], lst[~check, 1], color='royalblue', s=0.1)
    plt.show()
    
def gaussian(x):
    return (np.exp(-(x**2)))

def gauss_ploter(lst, check, a, b):
    x_values = np.linspace(a, b, 1000) 
    plt.figure(figsize=(10, 10))
    plt.xlim(a, b)
    plt.ylim(0, 1)
    plt.plot(x_values, gaussian(x_values), color='black')
    plt.scatter(lst[check, 0], lst[check, 1], color='royalblue', s=0.1) 
    plt.scatter(lst[~check, 0], lst[~check, 1], color='darkred', s=0.1) 
    plt.show()

def estimate_gauss(lst, check,xrange,yrange):
    inside_count = np.sum(check)
    total_points = len(lst)
    rectangle_area = xrange*yrange  # Width of x-axis interval * Height of y-axis interval
    return (rectangle_area * inside_count) / total_points

def cos_func(x):
    return np.cos(np.cos(np.pi*x/2))

def weird_cos_ploter(lst,check,a,b):
    x_values = np.linspace(a, b, 1000) 
    plt.figure(figsize=(10, 10))
    plt.xlim(a, b)
    plt.ylim(0, 1)
    plt.plot(x_values, cos_func(x_values), color='black')
    plt.scatter(lst[check, 0], lst[check, 1], color='royalblue', s=0.1) 
    plt.scatter(lst[~check, 0], lst[~check, 1], color='darkred', s=0.1) 
    plt.show()

def check_cos(lst):
    x_values = np.array(lst)[:, 0]
    y_values = np.array(lst)[:, 1]
    gauss_values = cos_func(x_values)
    checker = y_values <= gauss_values
    return checker

def estimate_cos(lst, check,xrange,yrange):
    inside_count = np.sum(check)
    total_points = len(lst)
    rectangle_area = xrange*yrange 
    return (rectangle_area * inside_count) / total_points

def f(x, y, z):
    return x**2 + y**2 + z**2 - 1  

def monte_carlo_volume(region, num_points):
    count_under_surface = 0
    for _ in range(num_points):
        x = np.random.uniform(region[0][0], region[0][1])
        y = np.random.uniform(region[1][0], region[1][1])
        z = np.random.uniform(region[2][0], region[2][1])
        
        if f(x, y, z) <= 0:
            count_under_surface += 1
            
    total_volume = (region[0][1] - region[0][0]) * (region[1][1] - region[1][0]) * (region[2][1] - region[2][0])
    return total_volume * (count_under_surface / num_points)

def volume_estimator_1_1_1(n):
    region = [(-1, 1), (-1, 1), (-1, 1)] 
    num_points = n
    estimated_volume = monte_carlo_volume(region, num_points)
    print("Estimated volume under the surface:", estimated_volume)
    
def cos_estimation(n):
    coordinates = random_coordinates(n,0,2,0,1)
    checker = check_cos(coordinates)
    print("Estimated Area:",estimate_cos(coordinates,checker,2,1))
    weird_cos_ploter(coordinates,checker,0,2)

def gauss_estimation_2_2(n):
    coordinates = random_coordinates(n,-2,2,0,1)
    print("Estimated Volume:",estimate_gauss(coordinates,check_gauss(coordinates),4,1))
    check_result = check_gauss(coordinates)
    print("Inside Count:", np.sum(check_result))
    print("Total Points:", len(coordinates))
    gauss_ploter(coordinates,check_gauss(coordinates),-2,2)

def darts_pi(n):
    coordinates = throw_darts(n)
    checker = check_inside_outside(coordinates)
    count = count_darts(coordinates)
    pi_estimate = estimate_pi(count)
    print("Pi Estimation:",pi_estimate)
    print("Pi Residual:",residuals_pi(pi_estimate))
    plot(coordinates,checker)

def execute_selected():
    choice = combo.get()
    n_value = int(n_entry.get())
    try:
        n = float(n_value)
        if choice == "Throw darts":
            darts_pi(n_value)
        elif choice == "Cos Function":
            cos_estimation(n_value)
        elif choice == "Gaussian Function":
            gauss_estimation_2_2(n_value)
        elif choice == "3D Function":
            volume_estimator_1_1_1(n_value)
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter a valid number for n.")

root = tk.Tk()
root.title("Function Options")

root.geometry("400x200")

label = ttk.Label(root, text="Choose an option:")
label.pack()

options = ["Throw darts", "Cos Function", "Gaussian Function", "3D Function"]
combo = ttk.Combobox(root, values=options,width=40)
combo.pack()

n_label = ttk.Label(root, text="Enter value for n:")
n_label.pack()

n_entry = ttk.Entry(root)
n_entry.pack()

execute_button = ttk.Button(root, text="Execute", command=execute_selected)
execute_button.pack()

root.mainloop()