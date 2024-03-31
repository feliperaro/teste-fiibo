"""
gvars.py - Module for managing global variables.
"""
import os

API_URL = "http://127.0.0.1:8000/api/"
PROJECT_DIR = os.getcwd()
RESOURCES_DIR = fr"{PROJECT_DIR}\resources"
TESTS_DIR = fr"{RESOURCES_DIR}\tests"
EXCEL_FILENAME_TEST = "test.xlsx"
EXCEL_FILEPATH_TEST = fr"{TESTS_DIR}\{EXCEL_FILENAME_TEST}"
EXCEL_FILENAME = "Modelo_Dados.xlsx"
EXCEL_FILEPATH = fr"{RESOURCES_DIR}\{EXCEL_FILENAME}"
