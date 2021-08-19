import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Country = pd.read_excel('IMVA.xls')

Countries = Country['Periods'].str.split(' ',n = 1,expand = True)
Country = Country.assign(Year=Countries[1])
Country.index = Country['Year']
print(Country)