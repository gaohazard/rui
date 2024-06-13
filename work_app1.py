import streamlit as st
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d


def calculate_weight_balance(aircraft_model, fuel_density, empty_weight, cg_position, left_side_fuel_volume_new,center_side_fuel_volume_new, crew_weight, add_weight, additional_moment):
    
    if aircraft_model == '737-800':
        # 定义插值所需的数据
        left_side_fuel_volume = np.array(
            [0, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 3600, 4000, 4400, 4800, 5200, 5600, 6000, 6400, 6800,
             7200, 7600, 8000, 8400, 8800, 9200, 9600, 9751])
        additional_lever_arm_left = np.array(
            [656.7, 656.7, 656.7, 657.1, 657.9, 658.7, 659.4, 660.6, 661.4, 662.6, 663.4, 664.6, 666.1, 668.1, 670.1,
             672.0, 674.4, 676.8, 679.1, 681.9, 685.0, 688.2, 691.3, 694.9, 698.8, 700.2])

        center_fuel_volume = np.array(
            [0, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 3600, 4000, 4400, 4800, 5200, 5600, 6000, 6400, 6800,
             7200, 7600, 8000, 8400, 8800, 9200, 9600, 10000, 10400, 10800, 11200, 11600, 12000, 12400, 12800, 13200,
             13600, 14000, 14400, 14800, 15200, 15600, 16000, 16273])
        additional_lever_arm_center = np.array(
            [610.2, 610.2, 609.8, 608.3, 607.1, 606.3, 605.5, 605.1, 605.1, 604.7, 604.7, 604.7, 604.7, 604.7, 604.7,
             605.1, 605.1, 605.1, 605.5, 605.5, 605.5, 605.9, 605.9, 605.9, 606.3, 606.3, 606.3, 606.3, 606.7, 606.7,
             606.7, 606.7, 606.7, 606.7, 606.7, 606.7, 606.3, 606.3, 606.3, 605.9, 605.5, 605.4])
        crew_weight_moment = crew_weight * 32
    elif aircraft_model == '737-700':
        left_side_fuel_volume = np.array(
            [0, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 3600, 4000, 4400, 4800, 5200, 5600, 6000, 6400, 6800,
             7200, 7600, 8000, 8400, 8800, 9200, 9600, 9751])
        additional_lever_arm_left = np.array(
            [656.7, 656.7, 656.7, 657.1, 657.9, 658.7, 659.4, 660.6, 661.4, 662.6, 663.4, 664.6, 666.1, 668.1, 670.1,
             672.0, 674.4, 676.8, 679.1, 681.9, 685.0, 688.2, 691.3, 694.9, 698.8, 700.2])
        center_fuel_volume = np.array(
            [0, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 3600, 4000, 4400, 4800, 5200, 5600, 6000, 6400, 6800,
             7200, 7600, 8000, 8400, 8800, 9200, 9600, 10000, 10400, 10800, 11200, 11600, 12000, 12400, 12800, 13200,
             13600, 14000, 14400, 14800, 15200, 15600, 16000, 16273])
        additional_lever_arm_center = np.array(
            [610.2, 610.2, 609.8, 608.3, 607.1, 606.3, 605.5, 605.1, 605.1, 604.7, 604.7, 604.7, 604.7, 604.7, 604.7,
             605.1, 605.1, 605.1, 605.5, 605.5, 605.5, 605.9, 605.9, 605.9, 606.3, 606.3, 606.3, 606.3, 606.7, 606.7,
             606.7, 606.7, 606.7, 606.7, 606.7, 606.7, 606.3, 606.3, 606.3, 605.9, 605.5, 605.4])
        crew_weight_moment = crew_weight * 150
    elif aircraft_model == '737-8':
        left_side_fuel_volume = np.array(
            [0, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 3600, 4000, 4400, 4800, 5200, 5600, 6000, 6400, 6800,
             7200, 7600, 8000, 8400, 8800, 9200, 9600, 9751])
        additional_lever_arm_left = np.array(
            [659.9, 659.9, 657.6, 658.0, 658.9, 660.0, 661.0, 662.0, 663.0, 663.9, 664.9, 666.0, 667.4, 669.0, 670.8,
             672.8, 675.0, 677.2, 679.7, 682.4, 685.3, 688.3, 691.6, 695.1, 698.9, 699.2])

        center_fuel_volume = np.array(
            [0, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 3600, 4000, 4400, 4800, 5200, 5600, 6000, 6400, 6800,
             7200, 7600, 8000, 8400, 8800, 9200, 9600, 10000, 10400, 10800, 11200, 11600, 12000, 12400, 12800, 13200,
             13600, 14000, 14400, 14800, 15200, 15600, 16000, 16273])
        additional_lever_arm_center = np.array(
            [609.7, 609.7, 609.9, 608.3, 606.8, 606.1, 605.4, 605.1, 604.9, 604.8, 604.7, 604.8, 604.8, 604.9, 605,
             605.1, 605.2, 605.4, 605.6, 606.7, 605.9, 606.0, 606.2, 606.3, 606.4, 606.5, 606.6, 606.7, 606.8, 606.8,
             606.9, 606.9, 607.0, 607.0, 606.9, 606.8, 606.7, 606.5, 606.3, 606.0, 605.7, 605.6])
        crew_weight_moment = crew_weight * 32
    else:
        print("机型输入错误")
    # 定义插值函数
    left_interp_func = interp1d(left_side_fuel_volume, additional_lever_arm_left, kind='linear')
    center_interp_func = interp1d(center_fuel_volume, additional_lever_arm_center, kind='linear')

    # 使用插值函数计算左、右、中三个位置的附加力臂
    new_additional_lever_arm_left = left_interp_func(left_side_fuel_volume_new)
    new_additional_lever_arm_center = center_interp_func(center_side_fuel_volume_new )

    # 计算总燃料量、总重量、总力矩和总力臂
    lever_arm = cg_position * 155.8 / 100 + 627.1
    moment = lever_arm * empty_weight
    total_weight = empty_weight +left_side_fuel_volume_new*fuel_density + center_side_fuel_volume_new*fuel_density + crew_weight + add_weight

    total_moment = (moment+left_side_fuel_volume_new * fuel_density * new_additional_lever_arm_left +
                    center_side_fuel_volume_new * fuel_density * new_additional_lever_arm_center+additional_moment+crew_weight_moment)
    total_arm = total_moment / total_weight

    # 计算新的重心位置
    cg_position_new = (total_arm - 627.1) * 100 / 155.8

    return total_weight, cg_position_new

def estimate_ba(cg_new, gw_new, brake, friction_coefficient, aircraft_model):
    if aircraft_model == '737-800':

        cg = np.array([5, 10, 15, 20, 25, 30, 35])
        gw = np.array([80, 100, 120, 140, 160, 180, 200])

    # 定义不同磨擦系数对应的二维数据
        mw_no_brake_coefficient_1 = np.array([[17, 16, 15, 14, 13, 11, 10],
                                              [20, 18, 17, 16, 14, 13, 11],
                                              [21, 20, 19, 17, 16, 14, 12],
                                              [23, 22, 20, 19, 17, 15, 13],
                                              [25, 23, 22, 20, 18, 16, 14],
                                              [26, 25, 23, 21, 20, 17, 15],
                                              [28, 26, 24, 23, 21, 18, 16]])

        mw_no_brake_coefficient_2 = np.array([[24, 23, 21, 20, 18, 16, 14],
                                              [27, 26, 24, 22, 20, 18, 15],
                                              [30, 28, 26, 24, 22, 20, 17],
                                              [32, 30, 28, 26, 24, 21, 18],
                                              [34, 32, 30, 28, 26, 23, 20],
                                              [36, 34, 32, 30, 27, 24, 21],
                                              [38, 36, 34, 31, 29, 25, 22]])

        mw_no_brake_coefficient_3 = np.array([[29, 27, 25, 24, 21, 19, 16],
                                              [32, 31, 29, 26, 24, 21, 18],
                                              [35, 33, 31, 29, 26, 23, 20],
                                              [38, 36, 34, 31, 28, 25, 22],
                                              [41, 39, 36, 33, 30, 27, 23],
                                              [43, 41, 38, 35, 32, 29, 25],
                                              [46, 43, 40, 37, 34, 30, 26]])

        mw_no_brake_coefficient_4 = np.array([[33, 31, 29, 27, 24, 21, 18],
                                              [36, 34, 32, 30, 27, 24, 21],
                                              [40, 38, 35, 33, 30, 26, 23],
                                              [43, 41, 38, 35, 32, 29, 25],
                                              [46, 44, 41, 38, 34, 31, 26],
                                              [49, 46, 43, 40, 36, 33, 28],
                                              [52, 49, 46, 42, 38, 34, 30]])

        mw_no_brake_coefficient_5 = np.array([[36, 34, 31, 29, 26, 23, 20],
                                              [40, 38, 35, 32, 30, 26, 22],
                                              [44, 41, 38, 36, 32, 29, 25],
                                              [47, 44, 42, 38, 35, 31, 27],
                                              [50, 48, 44, 41, 37, 33, 29],
                                              [53, 50, 47, 44, 40, 35, 31],
                                              [56, 53, 50, 46, 42, 37, 32]])

        mw_no_brake_coefficient_6 = np.array([[38, 36, 34, 31, 28, 25, 21],
                                              [43, 40, 38, 35, 32, 28, 24],
                                              [47, 44, 41, 38, 35, 31, 26],
                                              [50, 48, 44, 41, 38, 33, 29],
                                              [54, 51, 48, 44, 40, 36, 31],
                                              [57, 54, 50, 47, 43, 38, 33],
                                              [60, 57, 53, 49, 45, 40, 35]])

        mw_no_brake_coefficient_7 = np.array([[40, 38, 35, 33, 30, 26, 23],
                                              [45, 42, 40, 37, 33, 30, 25],
                                              [49, 47, 44, 40, 37, 33, 28],
                                              [53, 50, 47, 43, 40, 35, 30],
                                              [57, 54, 50, 47, 42, 38, 32],
                                              [60, 57, 53, 49, 45, 40, 35],
                                              [64, 60, 56, 52, 47, 42, 36]])

        mw_no_brake_coefficient_8 = np.array([[42, 40, 37, 34, 31, 28, 24],
                                              [47, 44, 42, 38, 35, 31, 26],
                                              [52, 49, 46, 42, 38, 34, 29],
                                              [56, 53, 49, 46, 41, 37, 32],
                                              [60, 56, 53, 49, 44, 40, 34],
                                              [63, 60, 56, 52, 47, 42, 36],
                                              [67, 63, 59, 54, 50, 44, 38]])

        mw_with_brake_coefficient_1 = np.array([[27, 26, 25, 24, 23, 22, 22],
                                                [30, 29, 28, 27, 26, 25, 25],
                                                [33, 31, 30, 29, 28, 28, 27],
                                                [35, 34, 33, 32, 31, 30, 29],
                                                [38, 36, 35, 34, 33, 32, 31],
                                                [40, 39, 37, 36, 35, 34, 33],
                                                [42, 41, 39, 38, 37, 36, 35]])

        mw_with_brake_coefficient_2 = np.array([[36, 35, 33, 32, 31, 31, 30],
                                                [40, 39, 37, 36, 35, 34, 33],
                                                [44, 42, 41, 40, 39, 38, 37],
                                                [48, 46, 44, 43, 42, 41, 40],
                                                [51, 49, 47, 46, 45, 44, 43],
                                                [54, 52, 50, 49, 48, 46, 45],
                                                [57, 55, 53, 52, 50, 49, 48]])

        mw_with_brake_coefficient_3 = np.array([[42, 41, 39, 38, 37, 36, 35],
                                                [47, 45, 44, 43, 41, 40, 39],
                                                [52, 50, 48, 47, 46, 44, 43],
                                                [56, 54, 52, 51, 49, 48, 47],
                                                [60, 58, 56, 54, 53, 51, 50],
                                                [63, 61, 59, 57, 56, 55, 53],
                                                [67, 64, 62, 61, 59, 58, 56]])

        mw_with_brake_coefficient_4 = np.array([[47, 45, 43, 42, 41, 40, 37],
                                                [52, 50, 49, 47, 46, 45, 41],
                                                [57, 55, 53, 52, 51, 49, 44],
                                                [62, 60, 58, 56, 55, 53, 48],
                                                [66, 64, 62, 60, 59, 57, 51],
                                                [70, 68, 66, 64, 62, 61, 54],
                                                [74, 71, 69, 67, 66, 64, 57]])

        mw_with_brake_coefficient_5 = np.array([[50, 48, 47, 45, 44, 43, 37],
                                                [56, 54, 52, 51, 50, 48, 41],
                                                [61, 59, 57, 56, 55, 52, 44],
                                                [66, 64, 62, 61, 59, 56, 48],
                                                [71, 68, 66, 65, 63, 60, 51],
                                                [75, 73, 71, 69, 67, 64, 54],
                                                [79, 77, 74, 73, 71, 67, 57]])

        mw_with_brake_coefficient_6 = np.array([[52, 51, 49, 48, 47, 43, 37],
                                                [59, 57, 55, 54, 53, 48, 41],
                                                [64, 62, 61, 59, 58, 52, 44],
                                                [70, 67, 66, 64, 62, 56, 48],
                                                [74, 72, 70, 68, 67, 60, 51],
                                                [79, 77, 75, 73, 71, 64, 54],
                                                [83, 81, 79, 77, 75, 67, 57]])

        mw_with_brake_coefficient_7 = np.array([[52, 52, 51, 50, 48, 43, 37],
                                                [59, 59, 57, 56, 54, 48, 41],
                                                [65, 65, 63, 61, 59, 52, 44],
                                                [71, 71, 68, 66, 63, 56, 48],
                                                [76, 76, 73, 71, 68, 60, 51],
                                                [81, 81, 77, 75, 72, 64, 54],
                                                [86, 86, 82, 80, 76, 67, 57]])

        mw_with_brake_coefficient_8 = np.array([[52, 53, 52, 51, 48, 43, 37],
                                                [59, 60, 59, 57, 54, 48, 41],
                                                [65, 66, 65, 63, 59, 52, 44],
                                                [71, 72, 70, 68, 63, 56, 48],
                                                [76, 77, 75, 73, 68, 60, 51],
                                                [81, 82, 79, 78, 72, 64, 54],
                                                [86, 86, 84, 82, 76, 67, 57]])
    elif aircraft_model == '737-700':

        cg = np.array([5, 10, 15, 20, 25, 30, 35])
        gw = np.array([80, 100, 120, 140, 160, 180, 200])

    # 定义不同磨擦系数对应的二维数据
        mw_no_brake_coefficient_1 = np.array([[17, 16, 15, 14, 13, 11, 10],
                                              [20, 18, 17, 16, 14, 13, 11],
                                              [21, 20, 19, 17, 16, 14, 12],
                                              [23, 22, 20, 19, 17, 15, 13],
                                              [25, 23, 22, 20, 18, 16, 14],
                                              [26, 25, 23, 21, 20, 17, 15],
                                              [28, 26, 24, 23, 21, 18, 16]])

        mw_no_brake_coefficient_2 = np.array([[24, 23, 21, 20, 18, 16, 14],
                                              [27, 26, 24, 22, 20, 18, 15],
                                              [30, 28, 26, 24, 22, 20, 17],
                                              [32, 30, 28, 26, 24, 21, 18],
                                              [34, 32, 30, 28, 26, 23, 20],
                                              [36, 34, 32, 30, 27, 24, 21],
                                              [38, 36, 34, 31, 29, 25, 22]])

        mw_no_brake_coefficient_3 = np.array([[29, 27, 25, 24, 21, 19, 16],
                                              [32, 31, 29, 26, 24, 21, 18],
                                              [35, 33, 31, 29, 26, 23, 20],
                                              [38, 36, 34, 31, 28, 25, 22],
                                              [41, 39, 36, 33, 30, 27, 23],
                                              [43, 41, 38, 35, 32, 29, 25],
                                              [46, 43, 40, 37, 34, 30, 26]])

        mw_no_brake_coefficient_4 = np.array([[33, 31, 29, 27, 24, 21, 18],
                                              [36, 34, 32, 30, 27, 24, 21],
                                              [40, 38, 35, 33, 30, 26, 23],
                                              [43, 41, 38, 35, 32, 29, 25],
                                              [46, 44, 41, 38, 34, 31, 26],
                                              [49, 46, 43, 40, 36, 33, 28],
                                              [52, 49, 46, 42, 38, 34, 30]])

        mw_no_brake_coefficient_5 = np.array([[36, 34, 31, 29, 26, 23, 20],
                                              [40, 38, 35, 32, 30, 26, 22],
                                              [44, 41, 38, 36, 32, 29, 25],
                                              [47, 44, 42, 38, 35, 31, 27],
                                              [50, 48, 44, 41, 37, 33, 29],
                                              [53, 50, 47, 44, 40, 35, 31],
                                              [56, 53, 50, 46, 42, 37, 32]])

        mw_no_brake_coefficient_6 = np.array([[38, 36, 34, 31, 28, 25, 21],
                                              [43, 40, 38, 35, 32, 28, 24],
                                              [47, 44, 41, 38, 35, 31, 26],
                                              [50, 48, 44, 41, 38, 33, 29],
                                              [54, 51, 48, 44, 40, 36, 31],
                                              [57, 54, 50, 47, 43, 38, 33],
                                              [60, 57, 53, 49, 45, 40, 35]])

        mw_no_brake_coefficient_7 = np.array([[40, 38, 35, 33, 30, 26, 23],
                                              [45, 42, 40, 37, 33, 30, 25],
                                              [49, 47, 44, 40, 37, 33, 28],
                                              [53, 50, 47, 43, 40, 35, 30],
                                              [57, 54, 50, 47, 42, 38, 32],
                                              [60, 57, 53, 49, 45, 40, 35],
                                              [64, 60, 56, 52, 47, 42, 36]])

        mw_no_brake_coefficient_8 = np.array([[42, 40, 37, 34, 31, 28, 24],
                                              [47, 44, 42, 38, 35, 31, 26],
                                              [52, 49, 46, 42, 38, 34, 29],
                                              [56, 53, 49, 46, 41, 37, 32],
                                              [60, 56, 53, 49, 44, 40, 34],
                                              [63, 60, 56, 52, 47, 42, 36],
                                              [67, 63, 59, 54, 50, 44, 38]])

        mw_with_brake_coefficient_1 = np.array([[27, 26, 25, 24, 23, 22, 22],
                                                [30, 29, 28, 27, 26, 25, 25],
                                                [33, 31, 30, 29, 28, 28, 27],
                                                [35, 34, 33, 32, 31, 30, 29],
                                                [38, 36, 35, 34, 33, 32, 31],
                                                [40, 39, 37, 36, 35, 34, 33],
                                                [42, 41, 39, 38, 37, 36, 35]])

        mw_with_brake_coefficient_2 = np.array([[36, 35, 33, 32, 31, 31, 30],
                                                [40, 39, 37, 36, 35, 34, 33],
                                                [44, 42, 41, 40, 39, 38, 37],
                                                [48, 46, 44, 43, 42, 41, 40],
                                                [51, 49, 47, 46, 45, 44, 43],
                                                [54, 52, 50, 49, 48, 46, 45],
                                                [57, 55, 53, 52, 50, 49, 48]])

        mw_with_brake_coefficient_3 = np.array([[42, 41, 39, 38, 37, 36, 35],
                                                [47, 45, 44, 43, 41, 40, 39],
                                                [52, 50, 48, 47, 46, 44, 43],
                                                [56, 54, 52, 51, 49, 48, 47],
                                                [60, 58, 56, 54, 53, 51, 50],
                                                [63, 61, 59, 57, 56, 55, 53],
                                                [67, 64, 62, 61, 59, 58, 56]])

        mw_with_brake_coefficient_4 = np.array([[47, 45, 43, 42, 41, 40, 37],
                                                [52, 50, 49, 47, 46, 45, 41],
                                                [57, 55, 53, 52, 51, 49, 44],
                                                [62, 60, 58, 56, 55, 53, 48],
                                                [66, 64, 62, 60, 59, 57, 51],
                                                [70, 68, 66, 64, 62, 61, 54],
                                                [74, 71, 69, 67, 66, 64, 57]])

        mw_with_brake_coefficient_5 = np.array([[50, 48, 47, 45, 44, 43, 37],
                                                [56, 54, 52, 51, 50, 48, 41],
                                                [61, 59, 57, 56, 55, 52, 44],
                                                [66, 64, 62, 61, 59, 56, 48],
                                                [71, 68, 66, 65, 63, 60, 51],
                                                [75, 73, 71, 69, 67, 64, 54],
                                                [79, 77, 74, 73, 71, 67, 57]])

        mw_with_brake_coefficient_6 = np.array([[52, 51, 49, 48, 47, 43, 37],
                                                [59, 57, 55, 54, 53, 48, 41],
                                                [64, 62, 61, 59, 58, 52, 44],
                                                [70, 67, 66, 64, 62, 56, 48],
                                                [74, 72, 70, 68, 67, 60, 51],
                                                [79, 77, 75, 73, 71, 64, 54],
                                                [83, 81, 79, 77, 75, 67, 57]])

        mw_with_brake_coefficient_7 = np.array([[52, 52, 51, 50, 48, 43, 37],
                                                [59, 59, 57, 56, 54, 48, 41],
                                                [65, 65, 63, 61, 59, 52, 44],
                                                [71, 70, 68, 66, 63, 56, 48],
                                                [76, 75, 73, 71, 68, 60, 51],
                                                [81, 79, 77, 75, 72, 64, 54],
                                                [86, 84, 82, 80, 76, 67, 57]])

        mw_with_brake_coefficient_8 = np.array([[52, 53, 52, 51, 48, 43, 37],
                                                [59, 60, 59, 57, 54, 48, 41],
                                                [65, 66, 65, 63, 59, 52, 44],
                                                [71, 72, 70, 68, 63, 56, 48],
                                                [76, 77, 75, 73, 68, 60, 51],
                                                [81, 82, 79, 78, 72, 64, 54],
                                                [86, 86, 84, 82, 76, 67, 57]])
    elif aircraft_model == '737-8':
        cg = np.array([5, 10, 15, 20, 25, 30, 35])
        gw = np.array([80, 100, 120, 140, 160, 180, 200])

        mw_no_brake_coefficient_1 = np.array([[17, 16, 15, 14, 13, 11, 9],
                                              [19, 18, 17, 16, 14, 12, 11],
                                              [21, 20, 19, 17, 16, 14, 12],
                                              [23, 21, 20, 18, 17, 15, 13],
                                              [24, 23, 21, 20, 18, 16, 14],
                                              [26, 24, 23, 21, 19, 17, 14],
                                              [27, 26, 24, 22, 20, 18, 15]])

        mw_no_brake_coefficient_2 = np.array([[24, 22, 21, 19, 17, 15, 13],
                                              [27, 25, 23, 22, 20, 17, 15],
                                              [29, 27, 26, 24, 21, 19, 16],
                                              [32, 30, 28, 26, 23, 21, 18],
                                              [34, 32, 30, 27, 25, 22, 19],
                                              [36, 34, 31, 29, 26, 23, 20],
                                              [38, 36, 33, 31, 28, 25, 21]])

        mw_no_brake_coefficient_3 = np.array([[28, 27, 25, 23, 21, 18, 16],
                                            [32, 30, 28, 26, 23, 21, 18],
                                            [35, 33, 31, 28, 26, 23, 19],
                                            [38, 35, 33, 31, 28, 25, 21],
                                            [40, 38, 35, 33, 30, 26, 22],
                                            [43, 40, 38, 35, 32, 28, 24],
                                            [45, 42, 40, 37, 33, 30, 25]])

        mw_no_brake_coefficient_4 = np.array([[32, 30, 28, 26, 24, 21, 18],
                                              [36, 34, 31, 29, 26, 23, 20],
                                              [39, 37, 35, 32, 29, 26, 22],
                                              [42, 40, 37, 34, 31, 28, 24],
                                              [45, 43, 40, 37, 33, 30, 25],
                                              [48, 45, 42, 39, 36, 32, 27],
                                              [51, 48, 45, 41, 37, 33, 28]])

        mw_no_brake_coefficient_5 = np.array([[35, 33, 31, 28, 26, 23, 19],
                                              [39, 37, 34, 32, 29, 25, 22],
                                              [43, 40, 38, 35, 32, 28, 24],
                                              [46, 44, 41, 38, 34, 30, 26],
                                              [50, 47, 44, 40, 37, 32, 28],
                                              [53, 49, 46, 43, 39, 34, 29],
                                              [55, 52, 49, 45, 41, 36, 31]])

        mw_no_brake_coefficient_6 = np.array([[37, 35, 33, 30, 27, 24, 20],
                                            [42, 39, 37, 34, 31, 27, 23],
                                            [46, 43, 40, 37, 34, 30, 25],
                                            [50, 47, 44, 40, 37, 32, 28],
                                            [53, 50, 47, 43, 39, 35, 30],
                                            [56, 53, 49, 46, 41, 37, 31],
                                            [59, 56, 52, 48, 44, 39, 33]])

        mw_no_brake_coefficient_7 = np.array([[40, 37, 35, 32, 29, 26, 22],
                                            [44, 42, 39, 36, 33, 29, 24],
                                            [49, 46, 43, 39, 36, 32, 27],
                                            [52, 49, 46, 43, 39, 34, 29],
                                            [56, 53, 49, 45, 41, 37, 31],
                                            [59, 56, 52, 48, 44, 39, 33],
                                            [63, 59, 55, 51, 46, 41, 35]])

        mw_no_brake_coefficient_8 = np.array([[41, 39, 36, 34, 30, 27, 23],
                                            [46, 44, 41, 38, 34, 30, 25],
                                            [51, 48, 45, 41, 37, 33, 28],
                                            [55, 52, 48, 44, 40, 36, 30],
                                            [59, 55, 52, 48, 43, 38, 33],
                                            [62, 59, 55, 50, 46, 41, 35],
                                            [66, 62, 58, 53, 48, 43, 37]])

        mw_with_brake_coefficient_1 = np.array([[26, 25, 24, 24, 23, 22, 22],
                                                [30, 28, 27, 26, 26, 25, 24],
                                                [32, 31, 30, 29, 28, 27, 27],
                                                [35, 34, 32, 31, 31, 30, 29],
                                                [37, 36, 35, 34, 33, 32, 31],
                                                [40, 38, 37, 36, 35, 34, 33],
                                                [42, 40, 39, 38, 37, 36, 35]])

        mw_with_brake_coefficient_2 = np.array([[36, 34, 33, 32, 31, 30, 30],
                                                [40, 38, 37, 36, 35, 34, 33],
                                                [44, 42, 41, 39, 38, 37, 36],
                                                [47, 45, 44, 43, 41, 40, 39],
                                                [50, 49, 47, 46, 44, 43, 42],
                                                [54, 52, 50, 48, 47, 46, 45],
                                                [56, 54, 53, 51, 50, 48, 47]])

        mw_with_brake_coefficient_3 = np.array([[42, 40, 39, 38, 37, 36, 35],
                                                [47, 45, 43, 42, 41, 40, 39],
                                                [51, 49, 48, 46, 45, 44, 42],
                                                [55, 53, 51, 50, 49, 47, 46],
                                                [59, 57, 55, 54, 52, 51, 49],
                                                [63, 60, 58, 57, 55, 54, 52],
                                                [66, 64, 62, 60, 58, 57, 55]])

        mw_with_brake_coefficient_4 = np.array([[46, 44, 43, 42, 41, 40, 35],
                                                [51, 50, 48, 47, 46, 44, 39],
                                                [56, 54, 53, 51, 50, 49, 42],
                                                [61, 59, 57, 56, 54, 53, 46],
                                                [65, 63, 61, 59, 58, 57, 49],
                                                [69, 67, 65, 63, 62, 60, 52],
                                                [73, 70, 68, 67, 65, 63, 55]])

        mw_with_brake_coefficient_5 = np.array([[49, 48, 46, 45, 44, 41, 35],
                                                [55, 53, 52, 50, 49, 46, 39],
                                                [61, 59, 57, 55, 54, 50, 42],
                                                [65, 63, 61, 60, 58, 54, 46],
                                                [70, 68, 66, 64, 63, 58, 49],
                                                [74, 72, 70, 68, 66, 61, 52],
                                                [78, 76, 74, 72, 70, 65, 55]])

        mw_with_brake_coefficient_6 = np.array([[51, 50, 49, 48, 46, 41, 35],
                                                [58, 56, 55, 53, 52, 46, 39],
                                                [64, 62, 60, 59, 57, 50, 42],
                                                [69, 67, 65, 63, 62, 54, 46],
                                                [74, 71, 70, 68, 66, 58, 49],
                                                [78, 76, 74, 72, 70, 61, 52],
                                                [82, 80, 78, 76, 74, 65, 55]])

        mw_with_brake_coefficient_7 = np.array([[52, 52, 50, 49, 47, 41, 35],
                                                [58, 58, 57, 55, 52, 46, 39],
                                                [64, 64, 62, 61, 57, 50, 42],
                                                [70, 69, 67, 66, 62, 54, 46],
                                                [75, 74, 72, 70, 66, 58, 49],
                                                [80, 79, 77, 75, 70, 61, 52],
                                                [85, 83, 81, 79, 74, 65, 55]])

        mw_with_brake_coefficient_8 = np.array([[52, 53, 52, 51, 47, 41, 35],
                                                [58, 59, 58, 57, 52, 46, 39],
                                                [64, 66, 64, 63, 57, 50, 42],
                                                [70, 71, 69, 68, 62, 54, 46],
                                                [75, 76, 74, 72, 66, 58, 49],
                                                [80, 81, 79, 77, 70, 61, 52],
                                                [85, 85, 83, 81, 74, 65, 55]])
    else:
        print('机型输入错误')
    if brake:
        if friction_coefficient == 0.1:
            mw = mw_with_brake_coefficient_1
        elif friction_coefficient == 0.2:
            mw = mw_with_brake_coefficient_2
        elif friction_coefficient == 0.3:
            mw = mw_with_brake_coefficient_3
        elif friction_coefficient == 0.4:
            mw = mw_with_brake_coefficient_4
        elif friction_coefficient == 0.5:
            mw = mw_with_brake_coefficient_5
        elif friction_coefficient == 0.6:
            mw = mw_with_brake_coefficient_6
        elif friction_coefficient == 0.7:
            mw = mw_with_brake_coefficient_7
        elif friction_coefficient == 0.8:
            mw = mw_with_brake_coefficient_8
        else:
            print("摩擦系数输入错误")
    else:
        if friction_coefficient == 0.1:
            mw = mw_no_brake_coefficient_1
        elif friction_coefficient == 0.2:
            mw = mw_no_brake_coefficient_2
        elif friction_coefficient == 0.3:
            mw = mw_no_brake_coefficient_3
        elif friction_coefficient == 0.4:
            mw = mw_no_brake_coefficient_4
        elif friction_coefficient == 0.5:
            mw = mw_no_brake_coefficient_5
        elif friction_coefficient == 0.6:
            mw = mw_no_brake_coefficient_6
        elif friction_coefficient == 0.7:
            mw = mw_no_brake_coefficient_7
        elif friction_coefficient == 0.8:
            mw = mw_no_brake_coefficient_8
        else:
            print("摩擦系数输入错误")

    interpolation_function = interpolate.interp2d(cg, gw, mw, kind='linear')
    return interpolation_function(cg_new, gw_new)

class EstimateBaApp:
    def __init__(self):
        st.title('737飞机重量重心及停放中抗风能力测算工具')
        self.aircraft_model = st.selectbox('飞机型号', ['737-700', '737-800', '737-8'])
        self.fuel_density = st.number_input('燃油密度(Kg/l)')
        self.index = st.number_input('新运行网中空机指数')
        self.gw_new = st.number_input('新运行网空机重量(lb)')
        self.left_side_fuel_volume_new = st.number_input('左和右主油箱总油量(lb)')
        self.center_side_fuel_volume_new = st.number_input('中央油箱油量(lb)')
        self.crew_weight = st.number_input('试车人员总重量(kg)（如试车）')
        self.add_weight = st.number_input('其他需要加减重量(lb)')
        self.additional_moment = st.number_input('其他需要加减重量对应的力矩值(lb.in)')
        self.brake = st.number_input('是否设置停留刹车（是/否）')
        self.friction_coefficient = st.number_input('请输入摩擦系数（0.1-0.8）')

        self.calculate_button = st.button('计算')
        if self.calculate_button:
            self.calculate()

    def calculate(self):
        aircraft_model=(self.aircraft_model_entry.get())
        if aircraft_model == '737-800':
            fuel_density = float(self.fuel_density_entry.get()) * 2.20462262185

            index=float(self.index_entry.get())
            gw_new = float(self.gw_new_entry.get())
            left_side_fuel_volume_new = float(self.left_side_fuel_volume_new_entry.get()) / fuel_density
            center_side_fuel_volume_new = float(self.center_side_fuel_volume_new_entry.get()) / fuel_density  # 根据需要设置默认值
            crew_weight = float(self.crew_weight_entry.get()) * 2.20462262185  # 根据需要设置默认值
            add_weight = float(self.add_weight_entry.get())  # 根据需要设置默认值
            additional_moment = float(self.additional_moment_entry.get())  # 根据需要设置默认值
            brake = str(self.brake_entry.get())
            cg_new=((index-45)*77162/gw_new+658.3-627.1)/1.558
            friction_coefficient = float(self.friction_coefficient_entry.get())
            total_weight, cg_position_new = calculate_weight_balance(aircraft_model, fuel_density, gw_new,
                                                                     cg_new, left_side_fuel_volume_new,
                                                                     center_side_fuel_volume_new, crew_weight,
                                                                     add_weight, additional_moment)
            print(gw_new,cg_new,total_weight, cg_position_new)
            mw_new = estimate_ba(cg_position_new, total_weight/1000, brake, friction_coefficient,aircraft_model)
            result_text = f"最大抗风值(节)：{mw_new}\n飞机重量（lb）：{total_weight}\n飞机重心位置（%）：{cg_position_new}"
            self.result_label.config(text=result_text)

        elif aircraft_model =='737-8':
            fuel_density = float(self.fuel_density_entry.get()) * 2.20462262185

            index = float(self.index_entry.get())
            gw_new = float(self.gw_new_entry.get())
            left_side_fuel_volume_new = float(self.left_side_fuel_volume_new_entry.get()) / fuel_density
            center_side_fuel_volume_new = float(
                self.center_side_fuel_volume_new_entry.get()) / fuel_density  # 根据需要设置默认值
            crew_weight = float(self.crew_weight_entry.get()) * 2.20462262185  # 根据需要设置默认值
            add_weight = float(self.add_weight_entry.get())  # 根据需要设置默认值
            additional_moment = float(self.additional_moment_entry.get())  # 根据需要设置默认值
            brake = str(self.brake_entry.get())
            cg_new = ((index - 45) * 77162 / gw_new + 658.3 - 627.1) / 1.558
            friction_coefficient = float(self.friction_coefficient_entry.get())
            total_weight, cg_position_new = calculate_weight_balance(aircraft_model, fuel_density, gw_new,
                                                                     cg_new, left_side_fuel_volume_new,
                                                                     center_side_fuel_volume_new, crew_weight,
                                                                     add_weight, additional_moment)
            print(gw_new, cg_new, total_weight, cg_position_new)
            mw_new = estimate_ba(cg_position_new, total_weight/1000, brake, friction_coefficient, aircraft_model)
            result_text = f"最大抗风值(节)：{mw_new}\n飞机重量（lb）：{total_weight}\n飞机重心位置（%）：{cg_position_new}"
            self.result_label.config(text=result_text)
        elif aircraft_model == '737-700':
            fuel_density = float(self.fuel_density_entry.get()) * 2.20462262185

            index = float(self.index_entry.get())
            gw_new = float(self.gw_new_entry.get())
            left_side_fuel_volume_new = float(self.left_side_fuel_volume_new_entry.get()) / fuel_density
            center_side_fuel_volume_new = float(
                self.center_side_fuel_volume_new_entry.get()) / fuel_density  # 根据需要设置默认值
            crew_weight = float(self.crew_weight_entry.get()) * 2.20462262185  # 根据需要设置默认值
            add_weight = float(self.add_weight_entry.get())  # 根据需要设置默认值
            additional_moment = float(self.additional_moment_entry.get())  # 根据需要设置默认值
            brake = str(self.brake_entry.get())
            cg_new = ((index - 45) * 66139 / gw_new + 658.3 - 627.1) / 1.558
            friction_coefficient = float(self.friction_coefficient_entry.get())
            total_weight, cg_position_new = calculate_weight_balance(aircraft_model, fuel_density, gw_new,
                                                                     cg_new, left_side_fuel_volume_new,
                                                                     center_side_fuel_volume_new, crew_weight,
                                                                     add_weight, additional_moment)
            print(gw_new, cg_new, total_weight, cg_position_new)
            mw_new = estimate_ba(cg_position_new, total_weight/1000, brake, friction_coefficient, aircraft_model)
            result_text = f"最大抗风值(节)：{mw_new}\n飞机重量（lb）：{total_weight}\n飞机重心位置（%）：{cg_position_new}"
            self.result_label.config(text=result_text)

# 创建Streamlit应用
app1 = EstimateBaApp()

