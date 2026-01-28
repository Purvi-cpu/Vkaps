from transformers import pipeline
gen = pipeline(
    "text-generation",
    model="microsoft/DialoGPT-medium" 
)
conversation_history = ""

while True:
    user_input = input("you ")

    if user_input.lower() == "exit":
        print("Game over!!")
        break

    conversation_history +=f"User: {user_input}\nBot:"

    result = gen(
        conversation_history,
        truncation = True,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,
        max_new_tokens=60
    )

    bot_reply = result[0]["generated_text"].split("Bot:")[-1].strip()

    print("Bot:", bot_reply, "\n")

    conversation_history += f" {bot_reply}\n"
    conversation_history = conversation_history[-1000:]