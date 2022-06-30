from selenium import webdriver
import bs4 import BeautifulSoup
import time 
import csv

url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("")