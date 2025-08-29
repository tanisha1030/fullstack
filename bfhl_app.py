import streamlit as st

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

st.title("BFHL Array Processor API (Streamlit)")

input_text = st.text_area(
    "Enter your array (comma-separated):",
    "1, 2, a, B, @, #, 3, 4"
)

if st.button("Process Array"):
    try:
        # Convert input to Python list
        arr = [x.strip() for x in input_text.split(",")]
        processed_array = []
        for x in arr:
            if x.isdigit():
                processed_array.append(int(x))
            else:
                processed_array.append(x)

        even_numbers, odd_numbers, alphabets, special_chars = [], [], [], []
        sum_numbers = 0
        alpha_concat = ""

        for item in processed_array:
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

        st.subheader("Response")
        st.json(response)

    except Exception as e:
        st.error(f"Error: {e}")
