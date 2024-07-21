# Function to greet the user
def greet():
    return ('Hello\n'
            '         How Can I Help You')


# Function to give responses to the user
def responses(user):

    user_input = user.lower()  # convert the input into lowercase

    if "what is your name" in user_input:
        return "I am a ChatBot you can call me alexa"

    elif "who created you" in user_input:
        return "I was created by chithra"

    elif "tell me a joke" in user_input:
        return '''Certainly! Here’s a light-hearted joke for you:
            Why did the scarecrow win an award? Because he was outstanding in his field!'''

    elif "how are you" in user_input:
        return '''I am just a ChatBot, I don’t experience emotions or have personal well-being, 
            but I’m here and ready to assist you with any questions '''

    elif "what is ai" in user_input:
        return '''Artificial intelligence (AI) refers to technology that enables computers and machines to simulate 
        human intelligence and problem-solving capabilities. Essentially, AI allows machines to perform tasks that 
        would otherwise require human intervention or intelligence.'''

    elif 'thank you' in user_input:
        return 'You are welcome! If you have any more questions feel free to ask'

    else:
        return "I am sorry , I don't understand that , please rephrase your statement"


# Main loop
greet = greet()
print("ChatBot: " + greet)
while True:
    user = input("You:")
    response = responses(user)
    print("ChatBot:", response)

    if 'exit' in user.lower():
        print("ChatBot: Goodbye have nice day!")
        break
