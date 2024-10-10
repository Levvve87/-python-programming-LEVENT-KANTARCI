


import math as mt
import matplotlib.pyplot as plt

datapokemon = "datapoints.txt"

widths = []
heights = [] 
labels = []

with open(datapokemon, "r") as datapokemons:

    for data in datapokemons:
        
        if data.startswith("("):
            continue
        
    
        dataparts = data.split(",")
        
        width = float(dataparts[0])
        height = float(dataparts[1])
        label = int(dataparts[2]) 
    
        widths.append(width)
        heights.append(height)
        labels.append(label) 


pichu_widths = []
pichu_heights = []

pikachu_widths = []
pikachu_heights = []       

for label in range(len(labels)):
    if labels[label] == 0:
        
        pichu_widths.append(widths[label])
        pichu_heights.append(heights[label])
    else:
       
        pikachu_widths.append(widths[label])
        pikachu_heights.append(heights[label])  