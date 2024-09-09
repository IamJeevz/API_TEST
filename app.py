from fastapi import FastAPI
from typing import List
import random

app = FastAPI()

# Example dictionary of words
words = [
    "elephant", "giraffe", "rhinoceros", "octopus", "penguin",
    "alligator", "cheetah", "kangaroo", "porcupine",
    "apple", "banana", "cherry", "date", "elderberry", 
    "fig", "grape", "honeydew", "jackfruit", "kiwi"
]

used_words = set()
used_numbers = set()

@app.get("/random_data")
def get_random_data():
    # Shuffle words if all are used
    if len(used_words) == len(words):
        used_words.clear()
    
    # Get a random word that hasn't been used
    while True:
        random_word = random.choice(words)
        if random_word not in used_words:
            used_words.add(random_word)
            break
    
    # Generate a unique random number
    while True:
        random_number = random.randint(1000000000, 9999999999)
        if random_number not in used_numbers:
            used_numbers.add(random_number)
            break
    
        # Print to console
    print(f">>>>> Word: {random_word},     Number: {random_number}")
    
    return {"word": random_word, "number": str(random_number)}
