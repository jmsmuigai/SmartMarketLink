from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load mock data
market_data = pd.read_csv("market_data.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    crop = request.form["crop"]
    data = market_data[market_data["Crop"].str.lower() == crop.lower()]
    return render_template("results.html", crop=crop, data=data.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
