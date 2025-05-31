🔐 Password Strength Meter with Generator
A Streamlit-based web app that allows users to:

Check the strength and entropy of any password

Detect common weaknesses and patterns

Generate secure passwords instantly

🚀 Features
Password Strength Analysis
Calculates a score (0–10) based on:

1)Length
2)Character variety (lowercase, uppercase, digits, symbols)
3)Entropy (measured in bits)
4)Common pattern detection (e.g., repeated characters, years, keyboard sequences)
5)Entropy Calculation
Uses Shannon entropy formula to estimate how unpredictable your password is.
6)Pattern Detection
Flags common weak patterns like:
7)Repeated characters (e.g., aaa, 111)
Sequences like 123, abc, qwe
Common years like 1998, 2020

Password Generator
Instantly create a strong password using a combination of letters, numbers, and symbols.

🖥️ Interface Preview
Input a custom password or generate a new one

Visual score and entropy metrics

Alerts for patterns and blacklisted passwords

Progress bar for visualizing strength

🧠 How It Works
Entropy Calculation
python
Copy
Edit
entropy = len(password) * log2(charset_size)
Where charset_size dynamically adapts based on what character types are used (a-z, A-Z, 0-9, symbols).

Strength Scoring
Length ≥ 8 → +2 points

Mix of character types → +1 each

High entropy (>60 bits) → +2 points

Pattern detected → -1 point

Score capped between 0–10

🛠️ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/password-strength-meter.git
cd password-strength-meter
Install dependencies

bash
Copy
Edit
pip install streamlit
Run the app

bash
Copy
Edit
streamlit run app.py
📂 Project Structure
bash
Copy
Edit
📦 password-strength-meter/
├── app.py         # Main Streamlit app
├── README.md      # Project documentation
└── requirements.txt (optional)
✅ Example Blacklisted Passwords
password

password123

12345678

🧪 Sample Output
makefile
Copy
Edit
Password: Pass@123
Entropy: 51.7 bits
Score: 7/10
Strength: Strong
Patterns: None
📌 TODO / Improvements
Add copy-to-clipboard for generated passwords

Enable user-defined password length

Support dictionary-based attack simulation

Add dark mode theme toggle

💡 Inspiration
Weak passwords are a major cause of security breaches. This tool helps users better understand what makes a password strong and how to avoid common pitfalls when creating one.

📃 License
MIT License — feel free to use and modify this project.

👨‍💻 Author
Developed with ❤️ using Python and Streamlit.
Before contributing, do take consent from me. I can be approached at through email: mqasim111786111@gmail.com

