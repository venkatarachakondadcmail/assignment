import pandas as pd
def encrypt_password(password: str):
    password = password.upper()
    cypher = pd.read_excel('Rubrics/chyper-code.xlsx')
    cypher= cypher[['USER TYPE', 'SYSTEM CONVERT']].astype(str)
    conversion_system = dict(zip(cypher['USER TYPE'], cypher['SYSTEM CONVERT']))
    encrypted_password = ''
    for char in password:
        if char.upper() in conversion_system:
            encrypted_password += conversion_system[char.upper()]
        else:
            encrypted_password += char
    return encrypted_password


def decrypt_password(encrypted_password:str):
    cypher = pd.read_excel('Rubrics/chyper-code.xlsx')
    cypher = cypher[['USER TYPE', 'SYSTEM CONVERT']].astype(str)
    conversion_system = dict(zip(cypher['USER TYPE'], cypher['SYSTEM CONVERT']))
    decryption_system = {v: k for k, v in conversion_system.items()}
    decrypted_password = ''
    for char in encrypted_password:
        if char.upper() in decryption_system:
            decrypted_password += decryption_system[char.upper()]
        else:
            decrypted_password += char
    return decrypted_password
