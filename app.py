from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Union
import uvicorn

app = FastAPI(title="BFHL API - Optimized", version="1.1")

class InputData(BaseModel):
    full_name: str
    dob: str
    email: str
    college_roll: str
    array: List[Union[str, int]]

@app.post("/bfhl")
def process_data(data: InputData):
    try:
        # Create user_id
        user_id = f"{data.full_name.lower().replace(' ', '_')}_{data.dob}"

        # Separate values in one pass
        even_numbers = [x for x in data.array if isinstance(x, int) and x % 2 == 0]
        odd_numbers = [x for x in data.array if isinstance(x, int) and x % 2 != 0]
        sum_numbers = sum(x for x in data.array if isinstance(x, int))
        alphabets = [x.upper() for x in data.array if isinstance(x, str) and x.isalpha()]
        alpha_chars = [x for x in data.array if isinstance(x, str) and x.isalpha()]
        special_chars = [x for x in data.array if isinstance(x, str) and not x.isalpha()]

        # Reverse concatenation with alternating caps
        reversed_alpha = ''.join(alpha_chars[::-1])
        alt_caps = ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(reversed_alpha)])

        return {
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
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
