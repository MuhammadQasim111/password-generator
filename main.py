
import streamlit as st
import string
import random
import math
import re

# -------- Utility Functions --------
def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[^a-zA-Z0-9]", password): charset += 32
    entropy = len(password) * math.log2(charset) if charset else 0
    return round(entropy, 2)

def detect_patterns(password):
    patterns = []
    if re.search(r'(.)\1{2,}', password):
        patterns.append("Repeated characters")
    if re.search(r'(123|321|abc|cba|qwe|asd)', password.lower()):
        patterns.append("Sequential or keyboard patterns")
    if re.search(r'(19[0-9]{2}|20[0-2][0-9])', password):
        patterns.append("Year/date detected")
    return patterns

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def password_strength_score(password):
    score = 0
    length = len(password)
    
    # Length points
    if length >= 8: score += 2
    elif length >= 5: score += 1

    # Variety
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    # Entropy
    entropy = calculate_entropy(password)
    if entropy > 60: score += 2
    elif entropy > 40: score += 1

    # Pattern penalty
    if detect_patterns(password): score -= 1

    return max(0, min(10, score)), entropy

def strength_label(score):
    if score <= 3: return "Weak"
    elif score <= 6: return "Moderate"
    else: return "Strong"

# -------- Streamlit UI --------
st.title("🔐 Password Strength Meter with Generator")

st.write("Enter a password to analyze or generate a strong one below.")

password = st.text_input("Enter Password", type="password")

if st.button("Check Password"):
    if not password:
        st.warning("Please enter a password.")
    elif password.lower() in ["password", "password123", "12345678"]:
        st.error("This password is blacklisted. Choose a more secure one.")
    else:
        score, entropy = password_strength_score(password)
        patterns = detect_patterns(password)
        st.metric("Entropy", f"{entropy} bits")
        st.metric("Score", f"{score}/10")
        st.success(f"Strength: {strength_label(score)}")

        if patterns:
            st.warning("Detected Patterns: " + ", ".join(patterns))
        else:
            st.info("No common patterns detected. Good job!")

        st.progress(score / 10)

if st.button("Generate Strong Password"):
    new_password = generate_password()
    st.code(new_password, language='text')
