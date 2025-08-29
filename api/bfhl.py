from typing import List
from vercel_python import VercelResponse
import json

# User details (change as needed)
FULL_NAME = "john_doe"
DOB = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"


def make_alternating_caps(s: str) -> str:
    result = []
    for idx, ch in enumerate(s):
        if idx % 2 == 0:
            result.append(ch.upper())
        else:
            result.append(ch.lower())
    return "".join(result)


def handler(request):
    try:
        # Parse JSON body
        body_bytes = request.body
        body_str = body_bytes.decode("utf-8")
        payload = json.loads(body_str)

        if "data" not in payload:
            return VercelResponse(json={"is_success": False, "message": "Invalid input"}, status=400)

        data: List = payload["data"]

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0

        for item in data:
            item_str = str(item)
            if item_str.isdigit():
                num = int(item_str)
                if num % 2 == 0:
                    even_numbers.append(item_str)
                else:
                    odd_numbers.append(item_str)
                total_sum += num
            elif item_str.isalpha():
                alphabets.append(item_str.upper())
            else:
                special_characters.append(item_str)

        # Reverse concatenated alphabets
        concat_raw = "".join(alphabets)[::-1]
        concat_string = make_alternating_caps(concat_raw)

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }

        return VercelResponse(json=response, status=200)

    except Exception as e:
        return VercelResponse(json={"is_success": False, "message": str(e)}, status=500)
