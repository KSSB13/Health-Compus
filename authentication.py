import streamlit as st
import pandas as pd
import subprocess
import bcrypt

def hash_password(password):
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def handle_signup(username, password):
    # Create a DataFrame with the new user's data
    new_user_data = pd.DataFrame({'Username': [username], 'Password': [hash_password(password)]})
    
    # Append the new user's data to the CSV file
    try:
        existing_data = pd.read_csv('user_credentials.csv')
        updated_data = pd.concat([existing_data, new_user_data], ignore_index=True)
        updated_data.to_csv('user_credentials.csv', index=False)
        st.success("Sign up successful. Please log in.")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        # If the CSV file doesn't exist or is empty, create it and store the new user data
        new_user_data.to_csv('user_credentials.csv', index=False)
        st.success("Sign up successful. Please log in.")

def authenticate_user(username, password):
    try:
        user_credentials = pd.read_csv('user_credentials.csv')
        if not user_credentials.empty:
            if 'Username' in user_credentials.columns:
                if (user_credentials['Username'] == username).any():
                    # Check password only if username exists
                    hashed_password = user_credentials.loc[user_credentials['Username'] == username, 'Password'].values[0]
                    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    except FileNotFoundError:
        return False


def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            st.experimental_set_query_params(logged_in=True)  # Set query parameter to indicate successful login
        else:
            st.error("Invalid username or password. Please try again.")

def signup_page():
    st.title("Sign Up")
    new_username = st.text_input("Enter a new username")
    new_password = st.text_input("Enter a new password", type="password")
    if st.button("Sign Up"):
        if new_username and new_password:
            handle_signup(new_username, new_password)
        else:
            st.warning("Please enter both username and password.")

def main():
    st.title("User Authentication")
    # st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Login", "Sign Up"])
    
    if page == "Login":
        login_page()
    elif page == "Sign Up":
        signup_page()

    # Check if user is logged in
    if st.experimental_get_query_params().get("logged_in", [False])[0]:
        # Run another Streamlit app
        st.success("Redirecting to another Streamlit app after successful login...")
        subprocess.run(["streamlit", "run", "APP2.py"])

if __name__ == "__main__":
    main()
