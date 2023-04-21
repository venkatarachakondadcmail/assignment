### Generate keys
import psycopg2
import re

import pickle
from pathlib import Path

import streamlit_authenticator as stauth
from . import connection
from . import hasher as h
import pandas as pd



def authenticate():
    cur = connection.conn.cursor()
    cur.execute("SELECT login, password FROM TB_USERS")
    results = cur.fetchall()
    cur.close()
    # Extract the usernames and passwords from the results
    usernames = []
    passwords = []
    for row in results:
        usernames.append(row[0])
        passwords.append(h.decrypt_password(row[1]))
    hashed_passwords = stauth.Hasher(passwords).generate()
    authenticator = stauth.Authenticate(usernames, usernames, hashed_passwords,
    "SIPL_dashboard", "abcdef")
    return authenticator
