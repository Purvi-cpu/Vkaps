#import kaggle

# Download and unzip automatically
# kaggle.api.dataset_download_files('uciml/breast-cancer-wisconsin-data', path='./data', unzip=True)
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def Data():
    df= pd.read_csv(r"C:\Users\hp\Desktop\Vkaps_task\Python_basics\data\data.csv")
    print(f"Shape of the merged DataFrame: {df.shape}")
    print(df.head())
    print(df.describe())
    print(df.isnull().sum())
    if 'Unnamed: 32' in df.columns:
        df.drop(columns=['Unnamed: 32'], inplace=True)
    df.dropna(inplace=True)

    texture_worst_mean = df['texture_worst'].mean()
    area_worst_mean = df['area_worst'].mean()

    # Bar plot
    labels = ['Texture Worst Mean', 'Area Worst Mean']
    values = [texture_worst_mean, area_worst_mean]


    plt.figure(figsize=(8, 4))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel('Features')
    plt.ylabel('Mean Value')
    plt.title('Mean Comparison of Texture Worst and Area Worst')
    plt.tight_layout()
    plt.savefig("static/mean_comparison.png")
    #plt.show()
    plt.close()
    return render_template('Graph.html')


if __name__ == "__main__":
    app.run(debug=True)