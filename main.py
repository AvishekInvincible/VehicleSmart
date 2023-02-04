import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import tkinter as tk
from PIL import ImageTk, Image
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from tkinter import *
root= tk.Tk()

canvas1 = tk.Canvas(root, width=1000, height=500)
canvas1.pack()

entry1 = tk.Entry(root) 
canvas1.create_window(500, 240, window=entry1)
root.title('Vehicle Dumb😣')
def get_square_root():  
    x1 = entry1.get()
    try:
        platenum = x1
        url = f'https://www.vehiclesmart.com/vehicle-smart-check.jsp?asc=18F0F1F18F2045F3_rhW46RAiHffddRykvAa7LAilFGrNpuG1FMblircqHwmhjHdsqSiComy40D070uVab9jgE1fS4e8DHoDlvqMN7A%3D%3D&reg={platenum}'
        options = Options()
        options.headless = False
        chrome_path = 'chromedriver'
        driver = webdriver.Chrome(chrome_path, chrome_options=options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(2)
        driver.find_element('xpath','//*[@id="cookie_accept"]/a').click()
        time.sleep(1)
        driver.find_element('xpath','//*[@id="wrapper"]/section[1]/div/div/div/div[2]/form/div[2]/button').click()
        time.sleep(4)
        driver.execute_script("document.body.style.zoom='70%'")
        time.sleep(1)
        driver.get_screenshot_as_file("tax.png")
        driver.execute_script("document.body.style.zoom='100%'")
        try:
            time.sleep(2)
            ele = driver.find_element('xpath','//*[@id="wrapper"]/div[1]/div/div/div[2]/div[2]/a[1]/div')
            ele.click()
            time.sleep(2)
            # driver.execute_script("document.body.style.zoom='90%'")
            driver.get_screenshot_as_file("mot.png")
            img = ImageTk.PhotoImage(Image.open("mot.png"))
            canvas1.create_image(0, 200, image=img, anchor=NW)
        except:
            pass

    except:
        root.title('Please Change the Plate number')
def ulez():
    pass
button1 = tk.Button(text='MOT - TAX Details', command=get_square_root)
canvas1.create_window(500, 300, window=button1)
button2 = tk.Button(text='ULEZ Details', command=ulez)
canvas1.create_window(500, 400, window=button2)


root.mainloop()


# def run():
    
    # time.sleep(30000)
    # driver.quit()
