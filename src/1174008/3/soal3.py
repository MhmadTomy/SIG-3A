# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:17:10 2019

@author: Arjun
"""

# In[] Soal No 3
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal3.shp") #Digunakan untuk melakukan membaca file shp
sb = sf.bbox #Berfungsi untuk mengetahui garis tepi pada file shp tersebut
print(sb)