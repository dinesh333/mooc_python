# This exercise is about creating a program which allows the user to search for recipes based on their names, preparation times, or ingredients used. The program should read the recipes from a file submitted by the user.

# Each recipe consists of three or more lines. The first line has the name of the recipe, the second line contains an integer number representing the preparation time in minutes, and the remaining line or lines contain the ingredients used, one on each line. The recipe ends with an empty line, with the exception of the final recipe in the file which just ends with the end of the file. So, there can be more than one recipe in a single file, like in the example below.

# Part 1: Search for recipes based on the name of the recipe
# Please write a function named search_by_name(filename: str, word: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose name contains the given search string. The names of these recipes are then returned in a list.
# As you can see in the example above, the case of the letters is irrelevant. The search term cake returns both Pancakes and Cake pops, even though the latter is capitalized.

# Part 2: Search for recipes based on the preparation time
# Please write a function named search_by_time(filename: str, prep_time: int), which takes a filename and an integer as its arguments. The function should go through the file and select all recipes whose preparation time is at most the number given.

# The names of these recipes are again returned in a list, but the preparation time should be appended to each name. Please have a look at the example below.

# Part 3: Search for recipes based on the ingredients
# A word of caution: this third part of the exercise is considerably more demanding than the previous two. If you feel like you aren't making headway, it may be worth your while to move on, complete the other exercises in this part of the material, and then come back to this exercise if you have time later. Remember, you can submit and receive points for the first two parts of this exercise even if you haven't completed the third part.

# Please write a function named search_by_ingredient(filename: str, ingredient: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose ingredients contain the given search string.

# The names of these recipes are returned in a list just like in the second part, with the preparation time appended. Please have a look at the example below.


# Write your solution here
def read_file(filename: str):
    file_lines = []
    with open(filename) as file:
        for line in file:
            line = line.replace('\n', '')
            file_lines.append(line)
    return file_lines

def create_recipes_from_file(filename: str):
    recipes = []
    file_lines = read_file(filename)
    total_recipes = file_lines.count('')+1
    start_index = 0
    for i in range(total_recipes):
        dict = {}
        dict['name'] = file_lines[start_index]
        dict['prep_time'] = file_lines[start_index+1]
        try:
            end_index = file_lines.index('', start_index)
        except:
            end_index = len(file_lines)
        dict['ingredients'] = file_lines[start_index+2:end_index]
        start_index = end_index+1
        recipes.append(dict)
    return recipes

def search_by_name(filename: str, word: str):
    recipes = create_recipes_from_file(filename)
    found_recipes = []
    for i in range(len(recipes)):
        name = recipes[i]['name']
        if word.lower() in name.lower():
            found_recipes.append(name)

    return found_recipes

def search_by_time(filename: str, prep_time: int):
    recipes = create_recipes_from_file(filename)
    found_recipes = []
    for i in range(len(recipes)):
        time = int(recipes[i]['prep_time'])
        if time <= prep_time:
            recipe = recipes[i]['name'] + ', ' + 'preparation time ' + str(time) + ' min'
            found_recipes.append(recipe)
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipes = create_recipes_from_file(filename)
    found_recipes = []
    for i in range(len(recipes)):
        for ingr in recipes[i]['ingredients']:
            if ingr == ingredient:
                time = int(recipes[i]['prep_time'])
                recipe = recipes[i]['name'] + ', ' + 'preparation time ' + str(time) + ' min'
                found_recipes.append(recipe)
    return found_recipes