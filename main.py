class FoodItem:
    def __init__(self, name, carbs, protein, fats):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fats = fats

class EffectOnGut:
    def __init__(self, increases_bacteria, decreases_inflammation):
        self.increases_bacteria = increases_bacteria
        self.decreases_inflammation = decreases_inflammation

class EffectOnBrain:
    def __init__(self, improves_mood, increases_focus):
        self.improves_mood = improves_mood
        self.increases_focus = increases_focus

database = {
    "apple": {
        "food": FoodItem(name="apple", carbs=25, protein=0.5, fats=0.5),
        "effects_on_gut": EffectOnGut(True, True),
        "effects_on_brain": EffectOnBrain(True, False)
    },

    "beef": {
        "food": FoodItem(name="beef", carbs=0, protein=30, fats=15), 
        "effects_on_gut": EffectOnGut(False, True),
        "effects_on_brain": EffectOnBrain(False, True)
    }
}

def search_by_name(name):
    if name in database:
        return database[name]
    else:
        return "Food not found!"

fruit_name = input("Enter a food name (apple/beef): ")

try:
    fruit = database[fruit_name]
except KeyError:
    print("Fruit not found in database!")
else:
    print(f"Name: {fruit['food'].name}")
    print(f"Carbs: {fruit['food'].carbs}")
    print(f"Protein: {fruit['food'].protein}")
    print(f"Fats: {fruit['food'].fats}")

    print(f"Increases Gut Bacteria: {fruit['effects_on_gut'].increases_bacteria}")
    print(f"Decreases Inflammation: {fruit['effects_on_gut'].decreases_inflammation}")

    print(f"Improves Mood: {fruit['effects_on_brain'].improves_mood}")
    print(f"Increases Focus: {fruit['effects_on_brain'].increases_focus}")

def filter_by_effect_on_gut(increases_bacteria, decreases_inflammation):
    results = {}
    for food_name in database:
        food_data = database[food_name]
        food_item = food_data["food"]
        gut_effect = food_data["effects_on_gut"]

        if (gut_effect.increases_bacteria == increases_bacteria and
            gut_effect.decreases_inflammation == decreases_inflammation):

            results[food_name] = food_data

    return results

def search_multiple_keywords(keywords):
    results = {}
    for food_name in database:
        food_data = database[food_name]
        food_item = food_data["food"]

        if all(keyword.lower() in food_item.name.lower() for keyword in keywords):
            results[food_name] = food_data

    return results