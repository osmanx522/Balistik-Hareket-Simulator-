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
    Velocity0_y = Velocity0 * np.sin(radian)
    as_time = Velocity0_y / gravity
    max_height = (Velocity0_y * as_time) - ((gravity*(as_time**2))/2)
    return (as_time, max_height)

def deascent_time(Velocity0:float, radian:float, height_deascent:float):
    Velocity0_y = Velocity0 * np.sin(radian)
    deas_time = np.sqrt((2*height_deascent)/(gravity+2*Velocity0_y))
    return deas_time

def instant_y_position(time:float, radian:float, v0:float, y0:float):
    v0_y = v0 * np.sin(radian)
    y_position = y0 + (v0_y*time) - ((gravity * (time**2))/2)
    return y_position

def instant_x_position(time:float, radian:float, v0:float, x0:float):
    '''
    Sabit Hızlı Hareket Üzerine Kurulmuştur
    '''
    v0_x = v0 * np.cos(radian)
    x_position = x0 +(v0_x*time)
    return x_position
def x_y_position(time_list, radian, v0, y0, x0):
    x_y_coordinates = [(instant_x_position(time, radian, v0, x0), instant_y_position(time, radian, v0, y0)) for time in time_list]
    return x_y_coordinates

def x_list_y_list(velocity, degree):
    radian = np.radians(degree)
    ascent_time_and_max_height = ascent_time(velocity, radian)
    flight_time = float(ascent_time_and_max_height[0]) * 2
    time_list = np.linspace(0, flight_time, num=100)
    x_list = instant_x_position(time_list, radian, velocity, 0)
    y_list = instant_y_position(time_list, radian, velocity, 0)
    return (x_list, y_list)

def main():
    # --- GRAFİK ÇİZİMİ ---
    plt.figure(figsize=(20, 10))
    velocity = float(input("İlk hızı giriniz: "))
    degree = float(input("Yatayla yaptığı dereceyi giriniz: "))
    x_y_axislist = x_list_y_list(velocity, degree)
    
    plt.plot(x_y_axislist[0], x_y_axislist[1], label="Mühimmat Yolu")
    plt.axis('equal')
    
    # Süslemeler
    plt.title(f"Atış Simülasyonu (V={velocity} m/s, Açı={degree}°)")
    plt.xlabel("Mesafe (m)")
    plt.ylabel("Yükseklik (m)")
    plt.grid(True)
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()