from fastapi import FastAPI
import random
import logging

# Initialize the FastAPI app
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.get("/random-boolean")
async def get_random_boolean():
    # Generate a random boolean value
    result = random.choice([True, False])
    
    # Log the result to the console
    logging.info(f">>>>>>>>>Random Boolean Result: {result}")
    
    # Return the result
    return {"result": result}



