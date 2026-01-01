# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 19:57:17 2025

@author: osman

~ Y Ekseni Referans Noktası yer seviyesi seçilmiştir
~ X Ekseni Referans Noktası atışın başlangıç noktası seçilmiştir
"""

import numpy as np
import matplotlib.pyplot as plt

gravity = 9.81

def ascent_time(Velocity0:float, radian:float):
    '''
    Atışın Çıkış Süresini ve max Yüksekliğini Döndürür
    '''
    Velocity0_y = Velocity0 * np.sin(radian)
    as_time = Velocity0_y / gravity
    max_height = (Velocity0_y * as_time) - ((gravity*(as_time**2))/2)
    return (as_time, max_height)

def deascent_time(Velocity0:float, radian:float, height_deascent:float):
    '''
    Atışın iniş süresini döndürür
    '''
    Velocity0_y = Velocity0 * np.sin(radian)
    deas_time = np.sqrt((2*height_deascent)/(gravity+2*Velocity0_y))
    return deas_time

def instant_y_position(time:float, radian:float, v0:float, y0:float):
    '''
    Anlık Y eksenindeki pozisyonunu verir
    '''
    v0_y = v0 * np.sin(radian)
    y_position = y0 + (v0_y*time) - ((gravity * (time**2))/2)
    return y_position

def instant_x_position(time:float, radian:float, v0:float, x0:float):
    '''
    Sabit Hızlı Hareket Üzerine Kurulmuştur
    Anlık X eksenindeki pozisyonunu verir
    '''
    v0_x = v0 * np.cos(radian)
    x_position = x0 +(v0_x*time)
    return x_position

def x_list_y_list(velocity, degree):
    '''
    Belirli bir zaman aralığındaki,
    X eksenindeki ve Y eksenindeki konumlarını anlık olarak bir anda return eder
    '''
    radian = np.radians(degree)
    ascent_time_and_max_height = ascent_time(velocity, radian)
    flight_time = float(ascent_time_and_max_height[0]) * 2
    time_list = np.linspace(0, flight_time, num=100)
    x_positon_list = instant_x_position(time_list, radian, velocity, 0)
    y_position_list = instant_y_position(time_list, radian, velocity, 0)
    return (x_positon_list, y_position_list)

def plotting(velocity:float, degree:float):
    '''
    Grafik Çizdirme
    '''
    x_y_axislist = x_list_y_list(velocity, degree)
    plt.plot(x_y_axislist[0], x_y_axislist[1], label=f"Mühimmat Yolu {velocity}m/s-{degree}°")

def plotting_privatization():
    '''
    Grafik Özelleştirme kısmı
    '''
    plt.title("Atış Hareketi")
    plt.xlabel("Mesafe (m)")
    plt.ylabel("Yükseklik (m)")
    plt.axhline(0, color='black')
    plt.legend()
    plt.grid(True)
    plt.axis('equal') 
    plt.show()

def main():
    plt.figure(figsize=(30, 20))
    vote = input("1-)Hız Aralığı Girme (Derece Sabit)\n2-)Derece Aralığı Girme (Hız Sabit)\n3-)Düz Grafik\nSeciminiz: ")
    if vote == "1":
        velocity_1 = int(input("Aralıktaki İlk Hız Değerini Girin: "))
        velocity_2 = int(input("Aralıktaki Son Hız Değerini Girin: "))
        degree = float(input("Dereceyi Girin: "))
        for velo in range(velocity_1, velocity_2+1):
            plotting(velo, degree)
        plotting_privatization()
        
    elif vote == "2":
        degree_1 = int(input("Aralıktaki İlk Dereceyi Girin: "))
        degree_2 = int(input("Aralıktaki Son Dereceyi Girin: "))
        degree_increase = int(input("Derece Artışı Girin (Default İçin ->1): "))
        velocity = float(input("Hızı Girin: "))
        for degree in range(degree_1, degree_2+1, degree_increase):
            plotting(velocity, degree)
        plotting_privatization()
        
    elif vote == "3":
        velocity = float(input("İlk Hızı Girin: "))
        degree = float(input("Dereceyi Girin: "))
        plotting(velocity, degree)
        plotting_privatization()
        
if __name__ == "__main__":
    main()