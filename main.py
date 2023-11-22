import pandas as pd
from tkinter import filedialog
import tkinter as tk
import time
# import matplotlib.pyplot as plt
# import numpy as np


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

def print_data(file_path):
    print("Original Data : ")
    print(file_path)

def count_missing_data(file_path):
    count_null = file_path.isnull().sum()
    print("menghitung missing data....")
    time.sleep(2)
    
    print("Hasil Count Missing Data : ")
    print(count_null)

def cleaning_data(file_path):
    print("Mencari Missing Data")
    data = file_path.isnull().sum()
    time.sleep(2)
    if data.any():
        cleaning = file_path.dropna()
        print("Berhasil Menghapus null data")
        time.sleep(1)
        print("Menampilkan hasil cleaning : ")
        print(cleaning)
    else:
        print("Tidak ada data yang null")


def reduction_data(file_path):
    load_data = file_path
    print("Load Data...")
    time.sleep(1)
    print("Data Berhasil di Load")
    time.sleep(1)

    col1 = input("Masukkan Kolom 1 : ")
    col2 = input("Masukkan Kolom 2 : ")

    x = input("Masukan batas terendah : ")
    y = input("Masukan batas tertinggi : ")

    
    if x.isnumeric():
        filtered_data = load_data[(load_data[col1] >= int(x)) > (load_data[col2] >= int(y))]
        print(filtered_data)
    else:
        filtered_data = load_data[(load_data[col1] >= x) > (load_data[col2] >= y)]
        print(filtered_data)


    # filtered_data = load_data[(load_data[col1] >= int(x)) > (load_data[col2] >= int(y))]

    print("Filter Data Berhasil")
    time.sleep(1)
    print("Hasil Filter Data : ")
    print(filtered_data)
    

def main():
    if '.csv' in file_path:
        data = pd.read_csv(file_path)
        print("------CSV File-----")
    elif '.xlsx' in file_path:
        data = pd.read_excel(file_path)
        print("------Excel File-----")
    
    while True:
        print("Pilih Menu : ")
        print("1. Print Data")
        print("2. Hitung Missing Data")
        print("3. Cleaning Data")
        print("4. Reduction Data")
        print("5. Exit")

        selected = input("Pilih Menu : ")
        if selected == '1':
            print_data(data)
        elif selected == '2':
            count_missing_data(data)
        elif selected == '3':
            cleaning_data(data)
        elif selected == '4':
            reduction_data(data)
        elif selected == '5':
            print("Keluar....")
            break

if __name__:
    main()