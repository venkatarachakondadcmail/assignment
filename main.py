import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
import controller.authenticate as auth
import create_user as c

st.set_page_config(page_title="Outlook Login",
                   page_icon=":envelope:",layout='centered')


from st_pages import hide_pages, show_pages



def outlook():
    st.markdown(
        f"""
        <style>
            
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{{
                width: 20rem;
                background-color: rgb(0 120 212) !important;
            }}
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{{
                width: 20rem;
                margin-left: -20rem;
            }}

            [data-testid="stSidebar"] img {{
                    width: 60%;
                }}

            [data-testid="stSidebar"] h1{{color:white;}}
            [data-testid="stImage"]  {{align-items: center;}}
            [data-testid="stSidebar"] h1 {{ color: white; writing-mode: vertical-rl; }}

            div.row-widget.stRadio > div{{flex-direction:row;justify-content: center;}}
            div.st-bf{{flex-direction:column;}} div.st-ag{{font-weight:bold;padding-left:2px;}}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.image("outlook-logo.png")
    st.sidebar.title("Welcome to MAILBOX")


# Create radio buttons to switch between login and new user pages
page = st.radio(".", ["Login", "New User"])


        
if page == "Login":
    authenticator = auth.authenticate()

    name, authentication_status, username = authenticator.login("Login", "main")
    st.session_state['name'] = name
    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")

    if not authentication_status:
        hide_pages(["main", "inbox", "spam"])

    if not username:
        outlook()

    if authentication_status:
        # # ---- SIDEBAR ----
        st.sidebar.title(f"Welcome {name}")
        # st.sidebar.header("select page here :")
        st.write("# Welcome to Streamlit!..")
        hide_pages(["main"])


        ###---- HIDE STREAMLIT STYLE ----
        hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_st_style, unsafe_allow_html=True)


        authenticator.logout("Logout", location="sidebar")
elif page == "New User":
    hide_pages(["main", "inbox", "spam"])
    outlook()
    c.new_user()


