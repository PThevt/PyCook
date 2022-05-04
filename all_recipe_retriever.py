from Recipe import Recipe


def retrieve():
    recipe_1 = Recipe(0, "Fondant au chocolat", "La recette pour faire un fondant au chocolat")
    recipe_2 = Recipe(1, "La tarte aux citrons", "La recette pour faire une tarte aux citrons")
    recipe_3 = Recipe(2, "Les chouquettes", "La recette pour faire des chouquettes")
    all_recipe = [recipe_1, recipe_2, recipe_3]
    return all_recipe
