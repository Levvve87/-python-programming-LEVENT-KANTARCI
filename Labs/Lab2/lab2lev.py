


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


def user_input_pokemon_data(nearest_points):
    
    pokemon_list = [] 
    
    while True:
        print("Wanna find out which of the pokemon you got?")
        user_choice  = input("input -> y <- for yes ")
        
        try: 
            if user_choice == "y":
               
                user_width = float(input("What is your pokemons testpoints, start with width? "))
                if user_width <= 0:
                    raise ValueError("Width has to be positiv number")
                user_height = float(input("What is your pokemons testpoints, start with height? "))
                if user_height <= 0:
                    raise ValueError("Height has to be positiv number")
                
                for step in range(len(widths)):
                    input_distance = euclidean_distance(user_width, widths[step],  user_height, heights[step])
                    pokemon_list.append((input_distance, labels[step]))

            else: 
                print("Your not a pokemon fan, Good Bye!")
            break 
            
        except ValueError as err:
                
                print(f"Input error: {err}. Please enter positiv numbers")


    sorted_list = sorted(pokemon_list)
    
    slice_list = sorted_list[:nearest_points]
   
    pichu_label_list = []
    pikachu_label_list = []
    pichu_distance_list = []
    pikachu_distance_list = []

    for slice in slice_list:
        print(f"{slice[0]}, {slice[1]}")
    
        if slice[1] == 0:
            pichu_label_list.append(slice[1])
            pichu_distance_list.append(slice[0])
        else:
            pikachu_label_list.append(slice[1])
            pikachu_distance_list.append(slice[0])
            
            
            
    if user_choice == "y":   
        if len(pichu_label_list) > len(pikachu_label_list):
            print(f" The user input with (width, height, nearest point(s)): ({user_width}, {user_height}, {nearest_points}) classified as Pokemon - Pichu")   
        elif len(pichu_label_list) == len(pikachu_label_list):   
            if sum(pichu_distance_list) > sum(pikachu_distance_list):
                print(f" The user input with (width, height, nearest point(s)): ({user_width}, {user_height}, {nearest_points}) classified as Pokemon - Pichu")   
            else:
                print(f" The user input with (width, height, nearest point(s)): ({user_width}, {user_height}, {nearest_points}) classified as Pokemon - Pichu")   
        else:
            print(f" The user input with (width, height, nearest point(s)): ({user_width}, {user_height}, {nearest_points}) classified as Pokemon - Pikachu")   
        
while True:
    try:
        nearest_point = int(input("User how many nearest point(s) do you wanna use? "))
        if nearest_point > 0:
            user_input_pokemon_data(nearest_point)
            break
        else:
            raise ValueError("You have to input positive integer")
    except ValueError as err:
            print(f"Input error: {err}. Please enter positiv integer")
