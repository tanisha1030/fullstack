const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

function isNumber(char) { return !isNaN(char); }
function isAlphabet(char) { return /^[A-Za-z]$/.test(char); }
function isSpecialChar(char) { return !isNumber(char) && !isAlphabet(char); }

function alternatingCaps(str) {
    let result = '', makeUpper = true;
    for (let ch of str) {
        result += makeUpper ? ch.toUpperCase() : ch.toLowerCase();
        makeUpper = !makeUpper;
    }
    return result;
}

app.post('/bfhl', (req, res) => {
    try {
        const { full_name, email, college_roll_number, array } = req.body;
        if (!full_name || !email || !college_roll_number || !Array.isArray(array)) {
            return res.status(400).json({ is_success: false, message: "Invalid input" });
        }

        const evenNumbers = [], oddNumbers = [], alphabets = [], specialChars = [];
        let sumNumbers = 0, alphaConcat = '';

        array.forEach(item => {
            const strItem = String(item);
            for (let char of strItem) {
                if (isNumber(char)) {
                    const num = parseInt(char);
                    sumNumbers += num;
                    if (num % 2 === 0) evenNumbers.push(num);
                    else oddNumbers.push(num);
                } else if (isAlphabet(char)) {
                    alphabets.push(char.toUpperCase());
                    alphaConcat += char;
                } else if (isSpecialChar(char)) {
                    specialChars.push(char);
                }
            }
        });

        const reversedAlphaConcat = alternatingCaps(alphaConcat.split('').reverse().join(''));

        const response = {
            is_success: true,
            user_id: `${full_name.toLowerCase().replace(/\s+/g, '_')}_${new Date().toISOString().slice(0,10).replace(/-/g,'')}`,
            email_id: email,
            college_roll_number: college_roll_number,
            even_numbers: evenNumbers,
            odd_numbers: oddNumbers,
            alphabets: alphabets,
            special_characters: specialChars,
            sum_of_numbers: sumNumbers,
            reversed_alternating_alphabets: reversedAlphaConcat
        };

        res.status(200).json(response);

    } catch (error) {
        res.status(500).json({ is_success: false, message: "Internal server error", error: error.message });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
