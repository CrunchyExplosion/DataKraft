
# PIL wala
from zipfile import ZipFile
import math as m
from PIL import Image
import numpy as np

def get_data(zip_filename):
    try:
        with open(zip_filename, 'rb') as zip_file:
            binary_data = zip_file.read()
        int_values = [int(byte) for byte in binary_data]
        return int_values
    except Exception as e:
        print("An Exception occurred:", str(e))
        return []

def optimize_size(size):
    base_number = m.floor(m.sqrt(size))
    diff = (size - (base_number*base_number))
    to_displace = m.floor(m.sqrt(diff)) 
    to_displace -= 1

    new_dim_x = base_number + to_displace
    new_dim_y = base_number - to_displace
    extra = int(m.fabs(size - (new_dim_x * new_dim_y)))

    biggest = max(new_dim_x, new_dim_y)
    times = 0
    if biggest < extra:
        times = int(extra / biggest)

        x_big = False
        y_big = False
        if new_dim_x > new_dim_y:
            x_big = True
        else:
            y_big = True

        if y_big == True:
            new_dim_x += times
        else:
            new_dim_y += times

        extra -= (times * biggest)

    row = min(new_dim_x, new_dim_y)
    col = max(new_dim_x, new_dim_y)

    return row, col, extra

def create_n_save_image(row, col, data):
    image_raw = [[0 for _ in range(col)] for _ in range(row +1 )]
    data_pointer = 0

    for l in range(row):
        for b in range(col):
            image_raw[l][b] = data[data_pointer]
            data_pointer += 1

    for a in range(col):
        image_raw[row][a] = data[data_pointer]
        data_pointer += 1
        if data_pointer == len(data):
            break

    image_array = np.array(image_raw, dtype=np.uint8)
    image = Image.fromarray(image_array)

    image.save("static/output_image.png")

def encode(zip_filename):
    data = get_data(zip_filename)
    size = len(data)

    row, col, extra = optimize_size(size)

    create_n_save_image(row, col, data)

    return 'output_image.png', extra



"""
from zipfile import ZipFile
import math as m
import cv2
import numpy as np

def get_data(zip_filename):
    try:
        with open(zip_filename, 'rb') as zip_file:
            binary_data = zip_file.read()
        int_values = [int(byte) for byte in binary_data]
        return int_values
    except Exception as e:
        print("An Exception occurred:", str(e))
        return []

def optimize_size(size):
    base_number = m.floor(m.sqrt(size))
    diff = (size - (base_number*base_number))
    to_displace = m.floor(m.sqrt(diff)) 
    to_displace -= 1

    new_dim_x = base_number + to_displace
    new_dim_y = base_number - to_displace
    extra = int(m.fabs(size - (new_dim_x * new_dim_y)))

    biggest = max(new_dim_x, new_dim_y)
    times = 0
    if biggest < extra:
        times = int(extra / biggest)

        x_big = False
        y_big = False
        if new_dim_x > new_dim_y:
            x_big = True
        else:
            y_big = True

        if y_big == True:
            new_dim_x += times
        else:
            new_dim_y += times

        extra -= (times * biggest)

    row = min(new_dim_x, new_dim_y)
    col = max(new_dim_x, new_dim_y)

    return row, col, extra

def create_n_save_image(row, col, data):
    image_raw = [[0 for _ in range(col)] for _ in range(row + 1)]
    data_pointer = 0

    for l in range(row):
        for b in range(col):
            image_raw[l][b] = data[data_pointer]
            data_pointer += 1

    for a in range(col):
        image_raw[row][a] = data[data_pointer]
        data_pointer += 1
        if data_pointer == len(data):
            break

    image = np.array(image_raw)

    cv2.imwrite("static/output_image.png", image)

def encode(zip_filename):
    data = get_data(zip_filename)
    size = len(data)

    row, col, extra = optimize_size(size)

    create_n_save_image(row, col, data)

    return 'output_image.png', extra
"""