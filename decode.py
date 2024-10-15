
from PIL import Image
import numpy as np

def data_from_image(image, row, col, key):
    data = []
    for r in range(row - 1):
        for c in range(col):
            num = int(image[r][c])
            data.append(num)

    k = 0
    for i in range(col):
        if k < key:
            num = int(image[row - 1][i])
            data.append(num)
            k += 1
        else:
            break

    return data

def create_new_zip(binary_vector, output_filename):
    try:
        with open(output_filename, 'wb') as output_zip:
            output_zip.write(binary_vector)
        print("Decrypted zip created successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

def decode(image_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)
    row, col = image_array.shape

    """
    This place has a bug below.
    It will allow illegal access if: the key input for downloading is in between actual key and no. of cols in image

    """
    if(key>col):
        int_values = data_from_image(image_array, row-2, col, key)
    else :
        int_values = data_from_image(image_array, row, col, key)
    # attempt was made to handle bug till here


    
    reconstructed_binary_vector = bytes(int_values)

    output_filename = 'static/decrypted.zip'
    create_new_zip(reconstructed_binary_vector, output_filename)


"""
import cv2

def data_from_image(image, row, col, key):
    data = []
    for r in range(row - 1):
        for c in range(col):
            num = int(image[r][c])
            data.append(num)

    k = 0
    for i in range(col):
        if k < key:
            num = int(image[row - 1][i])
            data.append(num)
            k += 1
        else:
            break

    return data

def create_new_zip(binary_vector, output_filename):
    try:
        with open(output_filename, 'wb') as output_zip:
            output_zip.write(binary_vector)
        print("Decrypted zip created successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

def decode(image_path, key):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    row, col = len(image), len(image[0])

    int_values = data_from_image(image, row, col, key)
    reconstructed_binary_vector = bytes(int_values)

    output_filename = 'static/decrypted.zip'
    create_new_zip(reconstructed_binary_vector, output_filename)

"""