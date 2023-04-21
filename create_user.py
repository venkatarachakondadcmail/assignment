
import streamlit as st
import re
from controller import transact as t

def is_valid_email(email):
    """
    Returns True if the email address is valid, False otherwise.
    """
    # A regular expression pattern for matching email addresses
    pattern = r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"
    
    # Use the re module to match the pattern with the email address
    match = re.match(pattern, email)
    # If there is a match, the email address is valid
    return match is not None

def new_user():
    # Streamlit form to get user input
    st.write("Create a new user")
    form = st.form(key="new_user_form")
    mail_id = form.text_input("Mail ID")
    password = form.text_input("Password", type="password")
    confirm_password = form.text_input("Confirm Password", type="password")
    submit = form.form_submit_button("Create User")

    if submit:
        # Check if the mail ID is valid
        if not is_valid_email(mail_id):
            st.error("Please enter a valid email address")
            return

        # Check if the mail ID is not empty
        if not mail_id:
            st.error("Please enter a mail ID")
            return
        # Check if the password is not empty
        if not password:
            st.error("Please enter a password")
            return
        # Check if the confirm password is not empty
        if not confirm_password:
            st.error("Please confirm your password")
            return
        # Check if the password and confirm password match
        if password != confirm_password:
            st.error("The passwords do not match")
            return
        t.insert_user(mail_id, password)
        st.success("New user created successfully!")
        st.write(f"Mail ID: {mail_id}")