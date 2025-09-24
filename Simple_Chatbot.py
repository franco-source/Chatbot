# Simple chatbot program

# Step 1: Ask for the user's name
name = input("What is your name?")

# Step 2: Greet them using their name
print("Hello", name+ "! nice to meet you.")

# Step 3: Ask how they are feeling today
feeling =input("How are you feeling today?")

# Step 4: Respond differently based on their answer
if feeling.lower()== "Good":
    print("That's great to hear! keep smiling," + name+ "!")
    
elif feeling.lower() == "bad":
    print("I'm sorry to hear that," + name+". i hope things get better soon.")
else:
    print("Thank you for sharing," + name+".")    