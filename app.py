from flask import Flask, render_template

app = Flask(__name__)

farmer = {
    "name": "Rushikesh",
    "age": 25,
    "location": "Pune",
    "crop": "Wheat",
    "crop_yield": 2500
}

records_data = [
    {"id": 1, "field": "Field A", "crop": "Wheat"},
    {"id": 2, "field": "Field B", "crop": "Rice"},
    {"id": 3, "field": "Field C", "crop": "Cotton"}
]

@app.route("/")
def home():
    return render_template("home.html",farmer=farmer_information)

@app.route("/records")
def records():
    
    return render_template("records.html", records=records_data)

@app.route("/farmer")
def farmer_information():
    return render_template("farmer.html", farmer=farmer)

if __name__ == "__main__":
    app.run(debug=True)