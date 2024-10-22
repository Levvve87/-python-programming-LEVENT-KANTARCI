


import math as mt
import matplotlib.pyplot as plt

# Raphael says: en mer kompakt lösning hade varit att spara dem i samma lista, dvs
# en lista av tupler. Det hade förenklat alla koden.

# Namnge variabeln för datapunkterna i textfilen
datapokemon = "datapoints.txt"
#Lagra som listor angående bredd, höjd på Pokémonen och även lagra etiketterna för de två Pokémon-typerna (0 för Pichu och 1 för Pikachu)
widths = []
heights = [] 
labels = []
# Loopar igenom från början till slut på varje rad av data i filen som nu kallas datapokemons
with open(datapokemon, "r") as datapokemons:

    for data in datapokemons:
        
        if data.startswith("("):
            continue
        # Delar upp datan med kommatecken så att den separerar listor i bredd, höjd och etiketter
    
        dataparts = data.split(",")
        # Konvertera strängarna till flyttal. Heltal för etiketter, de har inga decimaler. Indexen för listorna följer den specifika ordningen
        width = float(dataparts[0])
        height = float(dataparts[1])
        label = int(dataparts[2]) 
    #Lägger till dataparts för att lagra i Pokémonens listor
        widths.append(width)
        heights.append(height)
        labels.append(label) 

# Skapar listorna för att lagra Pichu-data
pichu_widths = []
pichu_heights = []
# Skapar listorna för att lagra Pikachu-data
pikachu_widths = []
pikachu_heights = []       

#Loopar igenom all data för etiketterna
for label in range(len(labels)):
    if labels[label] == 0:
    # Om etiketten är 0, är det Pokémonen Pichu (Den följer indexen från listorna Etiketter och lägger till bredd och höjd i samma ordning)
        pichu_widths.append(widths[label])
        pichu_heights.append(heights[label])
    else:
    # Om etiketten är något annat är det Pikachu (datapokemons hade inga andra etiketter förutom 0 eller 1)
        pikachu_widths.append(widths[label])
        pikachu_heights.append(heights[label]) 

# Skapar ett spridningsdiagram för Pichu
plt.scatter(pichu_widths, pichu_heights, color="orange", label="Pichu")
# Skapa ett spridningsdiagram för Pikachu
plt.scatter(pikachu_widths, pikachu_heights, color="yellow", label="Pikachu")
# Märker axlarna
plt.xlabel("Width (cm)")        
plt.ylabel("Height (cm)")   
# Axelvärden med en ökning av 1
x_values = list(range(16, 29))
y_values = list(range(28, 43))
# Axelmarkeringar för att visa värderna
plt.xticks(x_values)
plt.yticks(y_values)
# Lägger till legender för att visa vilka punkter, dvs. spridning, som representerar Pichu och Pikachu
plt.legend()
# Lägger till ett rutnät för att lättare se var punkterna ligger på axlarna
plt.grid()
# Visar diagrammet
plt.show()

# Skapar en funktion genom att återskapa formeln för euklidiskt avstånd
def euclidean_distance(x2, x1, y2, y1):
    
    return mt.sqrt((x2-x1)**2 + (y2-y1)**2)

# Namnger variabeln för textfilen testpunkter
testpokemon = "testpoints.txt"
# Öppnar testfilen i läsläge
with open(testpokemon, "r") as testpokemons:
  # Loopar igenom varje rad i testfilen
  # Raphael says: detta blev lite onödigt komplicerat
  # första raden kan hoppas över med testpokemons[1:]
  # Enklare att sedan göra testdata.split(",") or rensa resultatet
    for testdata in testpokemons:
        
# Hoppar över raden som börjar med strängen T
        if testdata.startswith("T"):
            continue
        
        # Skapar en ny variabel med den rensade importerade testfilen genom att ta bort kommatecken och parenteser
        cleaned_testdata = testdata.strip().replace("(", "").replace(")", "").replace(",", "")
        # Skapar en ny variabel för att dela upp strängen i separata element baserat på mellanslag i en lista
        more_cleaned_testdata = cleaned_testdata.split()
       # Variabeln skapad i flyttalsformat. Indexen i listan följer den ordningen eftersom index 0 bara är ett nummer i ordning av testpunkten utan någon annan betydelse.
        test_width = float(more_cleaned_testdata[1])
        test_height = float(more_cleaned_testdata[2])
        # Skapar variabler för att hitta närmaste avstånd för förutsägning av Pokémon. nearest_distance som oändlig flyttal för att göra det större än något naturligt tal som ett första steg och nearest_label som ingen för att fungera som platshållare.
        nearest_distance = float("inf")
        nearest_label = None 
       
        for i in range(len(widths)):
       # Raphael says: Bättre att använda den inbyggda funktionen min() på resultatet. Eller sortera som du gör senare.
            distance = euclidean_distance(test_width, widths[i], test_height, heights[i])
           # Beräknar det euklidiska avståndet mellan testpunkten och den aktuella datan i den lagrade listan av Pokémon
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_label = labels[i]
        # Uppdaterar det närmaste avståndet och etiketten till den aktuella datapunkten

        # Skriver ut testpunkterna baserat på etiketten för dess närmaste etikett.
        if nearest_label == 0:
            print(f"Sample with (width, height): ({test_width}, {test_height}) classified as Pokemon - Pichu")
        else:
            print(f"Sample with (width, height): ({test_width}, {test_height}) classified as Pokemon - Pikachu")




# Raphael says: Det här har blivit knasigt. Du borde använda samma funktion för båda uppgifterna, 
# det verkar som du implementerat nedastående utan riktigt förstå vad du gjort. Du borde ha en 
# classify(test_point, data_points, k_neighbours) funktion som gör förfarandet med att sortera listan
# som nedan. Den fungerar för alla k.
# Genom att dela upp variablerna i separata listor blir koden onödigt komplicerad.

# Definiera en funktion för att kunna ange hur många närmaste punkter den kommer att jämföras med.
def user_input_pokemon_data(nearest_points):
   # Skapar en tom lista för att lagra avstånd och etiketter som tupler. 
    pokemon_list = [] 
    # Skapar en loop som ger användaren möjlighet att mata in datan
    while True:
        print("Wanna find out which of the pokemon you got?")
        user_choice  = input("input -> y <- for yes ")
        # Skapar try, except ValueError för att hantera felaktig inmatning
        try: 
            if user_choice == "y":
               # Frågar användaren att mata in bredd och höjd och ger ett felmeddelande om inmatningen är något annat än positiva tal.
                user_width = float(input("What is your pokemons testpoints, start with width? "))
                if user_width <= 0:
                    raise ValueError("Width has to be positiv number") # Loopa igenom den lagrade listan med Pokémon-data för att beräkna avstånden med varje bredd- och höjddata och lagra de beräknade avstånden med varje etikett som en tuppel.
                user_height = float(input("What is your pokemons testpoints, start with height? "))
                if user_height <= 0:
                    raise ValueError("Height has to be positiv number")
                
                for step in range(len(widths)):
                    input_distance = euclidean_distance(user_width, widths[step],  user_height, heights[step])
                    pokemon_list.append((input_distance, labels[step]))
# Loopen bröts på grund av annan inmatning än y
            else: 
                print("Your not a pokemon fan, Good Bye!")
            break 
            
        except ValueError as err:
         # Fånga och visa fel relaterade till felaktig inmatning       
                print(f"Input error: {err}. Please enter positiv numbers")

# Sorterar listan med beräknade avstånd och etiketter
    sorted_list = sorted(pokemon_list)
    # Skär listan för att få ett område av närmaste punkter. Tack vare sorteringen tidigare är det möjligt att plocka upp dem. 
    slice_list = sorted_list[:nearest_points]
   # Skapar en tom lista för att lagra etiketter och närmaste avstånd för Pokémon
    pichu_label_list = []
    pikachu_label_list = []
    pichu_distance_list = []
    pikachu_distance_list = []
# Gå igenom de närmaste punkterna, separera dem och lägg till dem i sina respektive listor baserat på etiketter
    for slice in slice_list:
        print(f"{slice[0]}, {slice[1]}")
    
        if slice[1] == 0:
            pichu_label_list.append(slice[1])
            pichu_distance_list.append(slice[0])
        else:
            pikachu_label_list.append(slice[1])
            pikachu_distance_list.append(slice[0])
            
            
    # För att inte skriva ut Pokémon om användaren väljer att inte mata in. Pokémon avslöjas av majoriteten av en specifik typ i sina etiketter om de inte är i lika antal; annars väljs det närmaste avståndet.        
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
  # Loop för att få antal närmaste punkter från användaren, där du också har möjlighet att mata in heltal 1, 10 eller andra positiva heltal      
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
