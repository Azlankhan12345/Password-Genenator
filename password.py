import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):  # "lenght" ko "length" kar diya
    character = string.ascii_letters

    if use_digits:
        character += string.digits  # "string.use_digits" ki jagah "string.digits" correct hai

    if use_special:
        character += string.punctuation  # Yeh line sahi hai

    return ''.join(random.choice(character) for _ in range(length))  # "lenght" ka spelling sahi kiya

st.title("Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)  # "lenght" ko "length" kiya
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)  # "Password" ka "P" chhota kiya
    st.success(f"Generated Password: '{password}'")

    st.write("--------------------------------")

st.write('Build with ❤️ by [Azlan Khan](https://github.com/Azlankhan12345)')


