import streamlit as st
from st_pages import hide_pages
import controller.authenticate as auth
from controller import transact as t

st.set_page_config(page_title="Inbox", page_icon=":envelope:", layout="wide")


authenticator = auth.authenticate()

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    # # ---- SIDEBAR ----
    st.sidebar.title(f"Welcome {name}")
    # hide_pages(["main"])
    authenticator.logout("Logout", "sidebar")



def send_mail():
    # Define a checkbox to show/hide the "Send Mail" section
    show_send_mail = st.checkbox("Send Mail")

    # Define the "Send Mail" section
    if show_send_mail:
        with st.form(key="send_mail_form"):
            # Define the input fields for the email
            to_email = st.text_input("To")
            subject = st.text_input("Subject")
            message = st.text_area("Message")

            # Define the submit button
            submit_button = st.form_submit_button(label="Send")

        # Handle form submission
        if submit_button:
            # Display a confirmation message
             # Insert the new user into the database
            t.insert_mail_content(from_email=name, subject=subject, message=message, to_email=to_email)

       

send_mail()

def custom_expander(label, content):
    # Define a checkbox to show/hide the content
    show_content = st.checkbox(label)
    # Define a markdown element to display the content
    if show_content :
        st.markdown(content)

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
hide_pages(["main"])


emails = t.get_all_mails(name)
print(emails)
if emails != None:
    parsed_emails = []

    for email in emails:
        mail_id, _, login, mail_content, _, _, subject = email  # extract the relevant fields from each email
        parsed_email = {"mail_id": mail_id, "login": login,"mail_content": mail_content, "subject": subject}
        parsed_emails.append(parsed_email)


    emails = parsed_emails
    # Define the UI layout using Streamlit's columns
    col1, col2, col3 = st.columns([1, 1, 6])

    # Display the email IDs in the first column
    with col1:
        st.write("Mail ID")
        for email in emails:
            st.write(email["mail_id"])

    with col2:
        st.write("From")
        for email in emails:
            st.write(email["login"])
    # Display the email content in the second column
    with col3:
        st.write("Subject")
        for email in emails:
            if "mail_content" in email:
                # Define the email content as a collapsible section
                custom_expander(f"{email['subject']}", email["mail_content"])

            else:
                st.write(f"Email {email['mail_id']} is missing mail content.")





    