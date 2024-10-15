# DataKraft : Zip Hiding Application

This Flask application allows users to hide ZIP files within images using encoding techniques and then retrieve the original ZIP file by decoding the image. 

## Features
- Upload a ZIP file to hide data within an image.
- Decode an image to retrieve the original ZIP file using a key.

## Table of Contents
1. [Clone the Repository](#clone-the-repository)
2. [Setup the Virtual Environment](#setup-the-virtual-environment)
3. [Install Requirements](#install-requirements)
4. [Running the Flask Application](#running-the-flask-application)
5. [Deployment on Azure](#deployment-on-azure)

## Clone the Repository

To get a copy of this repository on your local machine, use the following command:

```bash
git clone https://github.com/your_username/your_repository_name.git
```

##Setup the Virtual Environment
It is recommended to use a virtual environment to manage dependencies. You can create a virtual environment using venv:

## 1. Navigate to the project directory:
```bash
cd your_repository_name
```

## 2. Create a virtual environment:
```bash
python -m venv venv
```

## 3. Activate the virtual environment:

- on Windows
  ```bash
  venv\Scripts\activate
  ```
- on macOS/Linux
  ```bash
  source venv/bin/activate
  ```

# Install Requirements
After activating the virtual environment, install the necessary packages using requirements.txt:
```bash
pip install -r requirements.txt
```

# Running the Flask Application
```bash
python app.py
```
The application will start, and you can access it at http://127.0.0.1:5000/ in your web browser.

# Deployment on Azure
This application has been successfully deployed on Azure using Azure Web App services. To get started with deploying your own Flask applications on Azure, refer to the official documentation. 👉 https://learn.microsoft.com/en-us/azure/app-service/


# Acknowledgments
Flask: A micro web framework for Python.
NumPy and PIL: Libraries used for handling images and numerical operations.

















