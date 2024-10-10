


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


plt.scatter(pichu_widths, pichu_heights, color="orange", label="Pichu")

plt.scatter(pikachu_widths, pikachu_heights, color="yellow", label="Pikachu")

plt.xlabel("Width (cm)")        
plt.ylabel("Height (cm)")   

x_values = list(range(16, 29))
y_values = list(range(28, 43))

plt.xticks(x_values)
plt.yticks(y_values)

plt.legend()

plt.grid()

plt.show()     