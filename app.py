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

@app.get("/random_word")
def get_random_word() -> str:
    # Shuffle words if all are used
    if len(used_words) == len(words):
        used_words.clear()
    
    # Get a random word that hasn't been used
    while True:
        word = random.choice(words)
        if word not in used_words:
            used_words.add(word)
            break
    
    return word

@app.get("/random_number")
def get_random_number():
    while True:
        random_number = random.randint(1000000000, 9999999999)
        if random_number not in used_numbers:
            used_numbers.add(random_number)
            break
    return random_number
