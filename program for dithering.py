#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:20:50 2022
practical course applied microbio 2022 
Slope of dithering of growth curves

@author: joy
"""

import numpy as np
import matplotlib.pyplot as plt 

file_to_look_at = 'M0 dat file ln'

data_from_file = np.genfromtxt(file_to_look_at, skip_header=100)
time_points = data_from_file[:, 0]
OD_value = data_from_file[:, 1]

# plt.plot(time_points, OD_value, color='black')
plt.title(file_to_look_at)
plt.title('Change in growth rate over time: M0')
plt.xlabel('Time (hour)')
plt.ylabel('OD')

def find_periods(data, target_line):
    '''
    data = array (2, x)
    target_line = float
    Returns time points where graph crosses target_line, going upwards (list)
    '''
    time_up_thr_targetline = []
    length = int(data.size / 2)
    for x in range(length - 1):
        if data[x, 1] < target_line and data[x+1, 1] > target_line:
            time_up_thr_targetline.append(data[x, 0])
    return time_up_thr_targetline 

# test_time_up = (find_periods(data_from_file, -0.5))
# print('test_time_up is', test_time_up)

def measurement_number(data, list_of_time):
    '''
    Takes list of time points, returns at which measurement the time 
    was that time. 
    '''
    num_of_measure = []
    for timepoint in list_of_time:
        place = np.where(data == timepoint)
        num_of_measure.append(place)
    return num_of_measure 

# test_numbers_of_measure = measurement_number(data_from_file, test_time_up)
# print('test_numbers_of_measure is', test_numbers_of_measure)

def find_low_and_high(data, target_line):
    '''
    Finds the highest OD point and lowest OD point of each period.
    period = all the values between two points where the graph 
    crossed the target line, going upwards. (think of a sine function).
    data = array (2, ?)
    target_line = float
    
    Returns list with coordinates of highest en lowest values.
    '''
    max_and_min_list = []
    time_up_thr_targetline = find_periods(data, target_line)
    num_of_measure = measurement_number(data, time_up_thr_targetline)
    for elem in range(len(num_of_measure)-1):
        start = num_of_measure[elem]
        finish = num_of_measure[elem + 1]
        part_of_data = data[int(start[0]):int(finish[0])]
        print('part_of_data_is', part_of_data)
        if len(part_of_data) > 6:
            maxx = part_of_data.max(axis=0)[1]
            position_of_max = int(np.where(data == maxx)[0])
            coo_to_app_max = list(data[position_of_max, :])
            max_and_min_list.append(coo_to_app_max)
            
            minn = part_of_data.min(axis=0)[1]
            position_of_min = int(np.where(data == minn)[0])
            coo_to_app = list(data[position_of_min, :])
            max_and_min_list.append(coo_to_app)
            # print('part of data is', part_of_data)
            print('max and min coo is', coo_to_app_max, coo_to_app)
    return max_and_min_list
    
# test_lows_and_highs = find_low_and_high(data_from_file, -0.5)
# print('lows and highs are', test_lows_and_highs)  

def slope(x1, y1, x2, y2):
    '''
    takes two coordinates (x1, y1) and (x2, y2) and returns slope if you
    go from first point to second point in graph. 

    '''
    slope = (y2 - y1) / (x2 - x1)
    return slope


def slope_over_time (data, target_line):
    '''
    Returns slopes of all periods and the first time point that was part 
    of the calculation.
    '''
    max_and_min_list = find_low_and_high(data, target_line)
    new_slope_list = []
    new_time_list = []
    for num in range(1, int(len(max_and_min_list))-2, 2):
        x1, y1 = max_and_min_list[num]
        x2, y2 = max_and_min_list[num+1]
        slope_of_period = slope(x1, y1, x2, y2)
        new_time_list.append(x1)
        new_slope_list.append(slope_of_period)
        print('x1 and y1 and x2 and y2', x1, y1, x2, y2)
        print('tijd vs slope', slope_of_period)
    return new_time_list, new_slope_list
     
test_slopes = slope_over_time(data_from_file, -0.5)
print('the test slopes are', test_slopes)
plt.plot(test_slopes[0], test_slopes[1], color='blue')

# =============================================================================
# poging tot derivative werk
# =============================================================================
# def deriv(x,f):
#      h = 0.1                 #step-size 
#      return (f(x+h) - f(x))/h

# for elem in range(len(time_points)): 
#     time = time_points[elem]
#     OD = OD_value[elem]
#     print(time, OD)
#     dero = deriv(time, OD)
#     if dero > -0.1 and dero < 0.1:
#         print(time)


# derivative = [0.001, -0.01, 0.05, 1]

# for elem in derivative: 
#     if elem > -0.1 and elem < 0.1:
#         print(elem)
    

# test_membrane_protein = new_z_chol_tov[10]

# =============================================================================
# prullebak
# =============================================================================
# high_y_value = tet[:, 1].max()
# high_x_value = np.where(tet == high_y_value)
# print(data_from_file.shape)

# def find_high_and_low (time_vs_od_part):
#     high_y_value = time_vs_od_part[:, 1].max()
#     high_x_value = time_vs_od_part.find()
#     pass


