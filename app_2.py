from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# Function to determine the response based on the emotion
def determine_emotion_response(emotion):
    sad_words = ["sad", "unhappy", "depressed", "down"]
    happy_words = ["happy", "joyful", "cheerful", "glad","qwerty"]
    anger_word=["indignation","outrage","rage", "fury", "wrath"]
    
    if any(word in emotion.lower() for word in sad_words):
        return "I am sad"
    elif any(word in emotion.lower() for word in happy_words):
        return "I am happy"
    elif any(word in emotion.lower() for word in anger_word):
        return "I am angry"
    else:
        return "Emotion not recognized"

@app.get("/emotion")
async def emotion(emotion: str = None):
    if not emotion:
        raise HTTPException(status_code=400, detail="No emotion provided")
    
    response = determine_emotion_response(emotion)
    return JSONResponse(content={"response": response})

# Run with: uvicorn main:app --reload
