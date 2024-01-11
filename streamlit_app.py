import streamlit as st

def register():
   st.title("Registration")

   name = st.text_input("Enter your name")
   email = st.text_input("Enter your email")

   if st.button("Register"):
       st.success("Successfully registered!")
       # Here you would typically save the user's information to a database
       # For now, we'll just print it out
       st.write(f"Name: {name}")
       st.write(f"Email: {email}")

register()