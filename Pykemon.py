import urllib.request
import json
import pandas
import os
import time

os.system("cls")
pkmn = input("Insert Pokemon name: ").lower()
# Get Species Data
url = "https://pokeapi.co/api/v2/pokemon-species/"+str(pkmn)
# print(url)
request = urllib.request.Request(url)
request.add_header('User-Agent',"cheese")
data = urllib.request.urlopen(request)
pkmn_data = json.load(data)
# print(pkmn_data)
# Get PKDX data
url_pkdx = "https://pokeapi.co/api/v2/pokedex/31/"
request = urllib.request.Request(url_pkdx)
request.add_header('User-Agent',"cheese")
data_pkdx = urllib.request.urlopen(request)
pkdx_data = json.load(data_pkdx)
# Get PKMN Data
url_pkdt = "https://pokeapi.co/api/v2/pokemon/"+str(pkmn)
request = urllib.request.Request(url_pkdt)
request.add_header('User-Agent',"cheese")
data_pkdt = urllib.request.urlopen(request)
pkdt_data = json.load(data_pkdt)

os.system("cls")

# Print species data
print("Species: "+pkmn_data["name"].capitalize())
for x in pkmn_data["genera"]:
    if x["language"]["name"] == "en":
        print(x["genus"])
if pkmn_data["gender_rate"] != -1:
    print("Ratio: " + str((pkmn_data["gender_rate"]/8)*100) + " Female, " + str(100-(pkmn_data["gender_rate"]/8)*100) + " Male")
else: print("Ratio: Genderless | Single Gender")
if pkmn_data["evolves_from_species"] != None:
    print("Evolve from " + pkmn_data["evolves_from_species"]["name"].capitalize())

# Print Types
if len(pkdt_data["types"]) == 1:
    print("Types: "+pkdt_data["types"][0]["type"]["name"].capitalize())
if len(pkdt_data["types"]) == 2:
    print("Types: "+pkdt_data["types"][0]["type"]["name"].capitalize()+" - "+pkdt_data["types"][1]["type"]["name"].capitalize())
# Print Abilities
if len(pkdt_data["abilities"]) == 1:
    print("Abilities: "+pkdt_data["abilities"][0]["ability"]["name"].capitalize())
if len(pkdt_data["abilities"]) == 2:
    print("Abilities: "+pkdt_data["abilities"][0]["ability"]["name"].capitalize()+", "+pkdt_data["abilities"][1]["ability"]["name"].capitalize())
if len(pkdt_data["abilities"]) == 3:
    print("Abilities: "+pkdt_data["abilities"][0]["ability"]["name"].capitalize()+", "+pkdt_data["abilities"][1]["ability"]["name"].capitalize()+", "+pkdt_data["abilities"][2]["ability"]["name"].capitalize())
# Print Stats
print("Stats:")
print("HP: "+str(pkdt_data["stats"][0]["base_stat"]))
print("ATK: "+str(pkdt_data["stats"][1]["base_stat"]))
print("DEF: "+str(pkdt_data["stats"][2]["base_stat"]))
print("SP. ATK: "+str(pkdt_data["stats"][3]["base_stat"]))
print("SP. DEF: "+str(pkdt_data["stats"][4]["base_stat"]))
print("SPEED: "+str(pkdt_data["stats"][5]["base_stat"]))
