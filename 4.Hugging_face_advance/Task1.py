from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier("I loved Star Wars so much!")

pipeline(task="sentiment-analysis", model = "tabularisai/multilingual-sentiment-analysis")("I loved Star Wars so much!")