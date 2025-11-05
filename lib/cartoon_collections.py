def roll_call_dwarves(dwarves):
    for i, name in enumerate(dwarves):
        print(f"{i + 1}. {name}")

def summon_captain_planet(calls):
    return [call.capitalize() + "!" for call in calls]

def long_planeteer_calls(calls):
    if any(len(call) > 4 for call in calls):
        return True
    else:
        return False

def find_the_cheese(food_items):
    cheese_list = ["cheddar", "gouda", "camembert"]
    for item in food_items:
            if item in cheese_list:
                return item
    return None
