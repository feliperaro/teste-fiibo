"""
gvars.py - Module for managing global variables.
"""
import os

API_URL = "http://127.0.0.1:8000/api/"
PROJECT_DIR = os.getcwd()
INPUT_DIR = fr"{PROJECT_DIR}\input"
OUTPUT_DIR = fr"{PROJECT_DIR}\output"
TESTS_DIR = fr"{PROJECT_DIR}\tests"
EXCEL_FILENAME_TEST = "test.xlsx"
EXCEL_FILEPATH_TEST = fr"{TESTS_DIR}\{EXCEL_FILENAME_TEST}"
EXCEL_FILENAME = "Modelo_Dados.xlsx"
EXCEL_FILEPATH = fr"{INPUT_DIR}\{EXCEL_FILENAME}"
