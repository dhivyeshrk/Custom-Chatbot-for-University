import streamlit as st

# Define a dictionary of rules for the chatbot
rules = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a computer program, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that."
}

def chatbot_response(input_text):
    input_text = input_text.lower()
    response = rules.get(input_text, rules["default"])
    return response

# Streamlit UI
def main():
    st.title("Simple Rule-Based Chatbot")

    st.markdown(
        """
        Welcome to the simple rule-based chatbot! 
        Enter your message in the textbox below.
        """
    )

    # Create a text input box
    user_input = st.text_input("You:", key='user_input')

    if st.button("Send"):
        # Get user input and generate response
        if user_input:
            response = chatbot_response(user_input)
            st.write("Bot:", response)
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
