# from google import genai

# client = genai.Client()


# prompt = input("your prompt")

# result = client.models.generate_content(
#     model = "gemini-pro-latest",
#     contents = prompt,
# )
# print(result.text)

import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
client = InferenceClient(
    provider="nscale",
    api_key=os.environ["HF_TOKEN"],
)

# output is a PIL.Image object
image = client.text_to_image(
    "Astronaut riding a horse",
    model="stabilityai/stable-diffusion-xl-base-1.0",
)
image.save("output.png")

