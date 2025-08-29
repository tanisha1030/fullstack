from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ User details (edit with your info)
FULL_NAME = "john_doe"         # lowercase only
DOB = "17091999"               # ddmmyyyy
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"


def make_alternating_caps(s: str) -> str:
    """Convert a string into alternating caps (starting with uppercase)."""
    result = []
    for idx, ch in enumerate(s):
        if idx % 2 == 0:
            result.append(ch.upper())
        else:
            result.append(ch.lower())
    return "".join(result)


@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        payload = request.get_json()
        if not payload or "data" not in payload:
            return jsonify({"is_success": False, "message": "Invalid input"}), 400

        data = payload["data"]

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0

        for item in data:
            item_str = str(item)

            # Numbers
            if item_str.isdigit():
                num = int(item_str)
                if num % 2 == 0:
                    even_numbers.append(item_str)
                else:
                    odd_numbers.append(item_str)
                total_sum += num

            # Alphabets (multi-letter allowed)
            elif item_str.isalpha():
                alphabets.append(item_str.upper())

            # Special characters
            else:
                special_characters.append(item_str)

        # Build concatenated string (reverse of all alphabets joined)
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

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500


# For Vercel: expose "app" object
app = app
