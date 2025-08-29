from flask import Flask, request, jsonify

app = Flask(__name__)  # Must be named `app` for Vercel

FULL_NAME = "tanisha_sharma"
DOB = "29082005"

def is_number(value):
    return isinstance(value, (int, float))

def is_alphabet(value):
    return isinstance(value, str) and value.isalpha() and len(value) == 1

def is_special_char(value):
    return isinstance(value, str) and not value.isalnum()

def alternating_caps(s):
    result = ""
    upper = True
    for c in s:
        result += c.upper() if upper else c.lower()
        upper = not upper
    return result

@app.route("/bfhl", methods=["POST"])
def bfhl():
    data = request.get_json()
    input_array = data.get("array", [])

    if not isinstance(input_array, list):
        return jsonify({"is_success": False, "message": "Input must be an array."}), 400

    even_numbers, odd_numbers, alphabets, special_chars = [], [], [], []
    sum_numbers = 0
    alpha_concat = ""

    for item in input_array:
        if is_number(item):
            sum_numbers += item
            if item % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
        elif is_alphabet(item):
            alphabets.append(item.upper())
            alpha_concat += item
        elif is_special_char(item):
            special_chars.append(item)

    reversed_alpha = alpha_concat[::-1]
    alternating_alpha = alternating_caps(reversed_alpha)

    response = {
        "is_success": True,
        "user_id": f"{FULL_NAME}_{DOB}",
        "email_id": "example@example.com",
        "college_roll_number": "123456",
        "even_numbers": even_numbers,
        "odd_numbers": odd_numbers,
        "alphabets": alphabets,
        "special_characters": special_chars,
        "sum_of_numbers": sum_numbers,
        "reverse_alternating_alpha": alternating_alpha
    }
    return jsonify(response)
