from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Union
import uvicorn

app = FastAPI(title="BFHL API", description="VIT Full Stack Question API", version="1.0")

# Input model
class InputData(BaseModel):
    full_name: str
    dob: str   # format: ddmmyyyy
    email: str
    college_roll: str
    array: List[Union[str, int]]

# Helper functions
def split_array(arr):
    even_numbers = []
    odd_numbers = []
    alphabets = []
    special_chars = []
    sum_numbers = 0
    alpha_chars = []

    for item in arr:
        if isinstance(item, int):
            sum_numbers += item
            if item % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
        elif isinstance(item, str):
            if item.isalpha():
                alphabets.append(item.upper())
                alpha_chars.append(item)
            else:
                special_chars.append(item)

    # Reverse concatenation with alternating caps
    reversed_alpha = ''.join(alpha_chars[::-1])
    alt_caps = ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(reversed_alpha)])
    
    return even_numbers, odd_numbers, alphabets, special_chars, sum_numbers, alt_caps

# Route
@app.post("/bfhl")
def process_data(data: InputData):
    try:
        user_id = f"{data.full_name.lower().replace(' ', '_')}_{data.dob}"
        even_numbers, odd_numbers, alphabets, special_chars, sum_numbers, alt_caps = split_array(data.array)
        
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": data.email,
            "college_roll": data.college_roll,
            "even_numbers": even_numbers,
            "odd_numbers": odd_numbers,
            "alphabets": alphabets,
            "special_chars": special_chars,
            "sum_of_numbers": sum_numbers,
            "concat_alpha_reverse_alt_caps": alt_caps
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# For local testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
