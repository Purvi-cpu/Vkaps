from transformers import pipeline
generator = pipeline(
    "text-generation",
    model="gpt2", 
    device=0,
    truncation = True,
    num_return_sequences = 5
)
print(generator("Python is great programing language")[0]["generated_text"])