world_directions_list = ["north", "south"]
world_directions_list = world_directions_list + ["west"]
world_directions_list.append("east")
print(world_directions_list)

world_directions_list = ["north", "west", "south", "east"]
del world_directions_list[0]
del world_directions_list[1] #dlaczego [1] to south?
print(world_directions_list)
world_directions_list.remove("west")
print(world_directions_list)

list = [3, 6, 17, 4, 0, -20, 20, 100]
list.sort()
print(f"Lista po sortowaniu {list}")

my_set = {'pon', 'wto', 'sro', 'pia', 'sob', 'nie'}
print(f"przed zmianami zbiór to {my_set}")
my_set.update({'czw'})
print(f"po zmianach zbiór to {my_set}") #dlaczego po uruchomieniu kodu zmieniona jest kolejność dni tygodnia?

salads = {
    "owocowa": ["ananas", "truskawka", "jagody"],
    "moja_buraczana": ["buraki", "ser kozi", "rukola"],
    "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"],
    "mięsna" : ["szynka", "kurczak", "ryż", "ogórek"]
}
print("Składniki sałatki mięsnej:", salads["mięsna"])
salads["owocowa"].append("cukier")
print(salads["owocowa"])

print(salads.keys())
del salads["mamina"]
print(salads.keys())
print()
print("Hello")
print("Hello")