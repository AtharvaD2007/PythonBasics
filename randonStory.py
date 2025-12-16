import random

characters = ["cat", "dog", "robot"]
actions = ["runs", "jumps", "flies"]
places = ["park", "city", "moon"]

story = random.choice(characters) + " " + random.choice(actions) + " in the " + random.choice(places)
print(story)