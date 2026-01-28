from transformers import pipeline
generator = pipeline(
    "text-generation",
    model="gpt2", 
    device=0,
    truncation = True,
    num_return_sequences = 5
)
prompt = "Python is great programming languge"
result = generator(
    prompt,
    max_length = 100,
    truncation = True
)
print(result[0]["generated_text"])