from together import Together

client = Together()
model = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"

class Task:
    def __init__(self, description, user_input):
        self.description = description
        self.user_input = user_input

# List of chef personalities
chef_personalities = [
    "A young, enthusiastic Indian chef specializing in Biryani",
    "A seasoned Italian chef with a passion for pasta-making",
    "An old Brazilian grandma who loves to cook classic dishes"
]

# List of tasks the chatbot can perform
tasks = [
    Task("Suggest a dish based on ingredients", "Please provide the ingredients you have"),
    Task("Provide a detailed recipe based on dish name", "Please provide the name of the dish you want a recipe for"),
    Task("Offer a constructive critique with suggested improvements based on the recipe", "Please provide the recipe you want a critique for")
]

# Main loop to interact with the user
retry = True
while retry:
    print("Welcome to the Chef Chatbot!")

    # Select chef personality
    print("\nWhich chef personality would you like to talk to?")
    for i, personality in enumerate(chef_personalities):
        print(f"{i + 1}. {personality}")
    
    chef_personality_index = int(input("Enter the number of the chef personality you want to talk to: "))
    chef_personality = chef_personalities[chef_personality_index - 1]
    
    print(f"Great! You are now talking to {chef_personality}")
    
    # Select task
    print("\nWhat would you like me to do for you?")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task.description}")
    
    task_type_index = int(input("Enter the number of the task you want to do: "))
    task_type = tasks[task_type_index - 1]
    
    print(f"Great! I will {task_type.description}")
    
    # Get user input for the selected task
    user_input = input(f"\n{task_type.user_input}: \n")
    
    print("\nLet me think about it...\n")
    
    # Prepare messages for the OpenAI API
    messages = [
        {
            "role": "system",
            "content": f'''You are {chef_personality}. 
                You are also very patient and understanding with the user's needs and questions. 
                You can:  
                1. Suggest a dish based on ingredients the user provides, but only give the dish name without a full recipe. 
                2. Provide a detailed recipe based on the dish name the user provides.
                3. Offer a constructive critique with suggested improvements based on the recipe the user provides.
                
                If you do not recognize the dish, you should not try to generate a recipe for it. 
                Do not answer a recipe if you do not understand the name of the dish. 
                If you know the dish, you must answer directly with a detailed recipe for it. 
                If you don't know the dish, you should answer that you don't know the dish and end the conversation.
                
                The user wants you to perform the {task_type.description} task.
                
                Here is the user input: {user_input}
                ''',
        }
    ]
    
    # Call the OpenAI API to get the response
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    
    # Print the response from the OpenAI API
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
    
    # Ask the user if they want to continue
    user_input = input("\n\nDo you want to continue / retry? (Y/N): ")
    retry = user_input.lower() == "y"
