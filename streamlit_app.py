import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
pip install Flask

from flask import Flask, render_template
import houseprice.csv

app = Flask(__name__)

@app.route('/')
def index():
    # Baca data dari file CSV
    data = read_csv('data.csv')

    # Kirim data ke template HTML
    return render_template('index.html', data=data)

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

if __name__ == '__main__':
    app.run(debug=True)

