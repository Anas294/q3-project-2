import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔐password strength checker🔐")
st.markdown("""
## Welcome to the ultimate pasword strength checker!
This app will help you to check the strength of your password and give you some tips to make it stronger.
""")

password = st.text_input("Enter your password:", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("✔Password is too short. It should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("✔Password should contain both uppercase and lowercase characters.")

        if re.search(r'\d', password):
            score += 1
        else:
                feedback.append("✔Password should contain at least one digit.")

                if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                    score += 1
                else:
                    feedback.append("✔Password should contain at least one special character.")
                    if score == 4:
                        st.success("Your password is strong!")
                    elif score == 3:
                        st.append("Your password is medium strength.")
                    else:
                        st.warning("Your password is weak. Please consider changing it.")

                    if feedback:
                            st.write("### improve your password:")
                            for tip in feedback:
                                st.write(tip)
else:
    st.info("Please enter a password to get started.")
            

