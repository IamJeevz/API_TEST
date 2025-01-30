from fastapi import FastAPI
from pydantic import BaseModel
import random
from fastapi.responses import JSONResponse

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

class RandomDataResponse(BaseModel):
    word: str
    number: str  # Ensuring that 'number' is returned as a string

@app.get("/random_data", response_model=RandomDataResponse)
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
    
    # Return the response with the number as a string
    return {"word": random_word, "number": str(random_number)}

# Create a GET endpoint that accepts URL-encoded query parameters
@app.get("/urlencoded/")
async def handle_query_params(name: str, age: int):
    # You can access the query parameters directly in the function
    response_data = {"name": name, "age": age}
    return JSONResponse(content=response_data)