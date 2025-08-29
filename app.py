from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union
from utils import process_input
from datetime import datetime

app = FastAPI(title="BFHL API")

# ------------------------
# Input Model
# ------------------------
class InputModel(BaseModel):
    full_name: str
    college_roll_no: str
    email_id: str
    array: List[Union[int, str]]

# ------------------------
# POST Endpoint
# ------------------------
@app.post("/bfhl")
def bfhl_endpoint(input_data: InputModel):
    try:
        result = process_input(input_data.array)

        # Generate user_id
        dob_str = datetime.now().strftime("%d%m%Y")
        user_id = f"{input_data.full_name.lower()}_{dob_str}"

        response = {
            "is_success": True,
            "user_id": user_id,
            "email_id": input_data.email_id,
            "college_roll_no": input_data.college_roll_no,
            "even_numbers": result["even_numbers"],
            "odd_numbers": result["odd_numbers"],
            "alphabets": result["alphabets"],
            "special_chars": result["special_chars"],
            "sum_of_numbers": result["sum_of_numbers"],
            "concat_alternating_caps": result["concat_alternating_caps"]
        }

        return response

    except Exception as e:
        return {"is_success": False, "error": str(e)}
