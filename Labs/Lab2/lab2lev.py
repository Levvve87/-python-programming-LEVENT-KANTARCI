


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

def euclidean_distance(x2, x1, y2, y1):
    
    return mt.sqrt((x2-x1)**2 + (y2-y1)**2)


testpokemon = "testpoints.txt"

with open(testpokemon, "r") as testpokemons:
  
    for testdata in testpokemons:
        
        if testdata.startswith("T"):
            continue
        
        cleaned_testdata = testdata.strip().replace("(", "").replace(")", "").replace(",", "")
        
        more_cleaned_testdata = cleaned_testdata.split()
       
        test_width = float(more_cleaned_testdata[1])
        test_height = float(more_cleaned_testdata[2])
        
        nearest_distance = float("inf")
        nearest_label = None 
       
        for i in range(len(widths)):
       
            distance = euclidean_distance(test_width, widths[i], test_height, heights[i])
           
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_label = labels[i]
        
        if nearest_label == 0:
            print(f"Sample with (width, height): ({test_width}, {test_height}) classified as Pokemon - Pichu")
        else:
            print(f"Sample with (width, height): ({test_width}, {test_height}) classified as Pokemon - Pikachu")


