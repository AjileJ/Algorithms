#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  if (set(recipe.keys()) == set(ingredients.keys())):
    recipeList = []
    ingredientsList = []
    for key in recipe:
      recipeList.append(recipe[key])
      ingredientsList.append(ingredients[key])
    batches = math.floor(ingredientsList[0] / recipeList[0])  
    for i in range(0, len(recipeList)):
      if recipeList[i] > ingredientsList[i]: 
       return 0
      current = math.floor (ingredientsList[i] / recipeList[i])
      
      if current < batches:
        batches = current
    return batches     
  return 0  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))