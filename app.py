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
    return render_template("home.html",farmer=farmer)

@app.route("/records")
def records():
    
    return render_template("records.html", records=records_data)

@app.route("/farmer")
def farmer_information():
    return render_template("farmer.html", farmer=farmer)
@app.route("/motor")
def motor():
    return render_template("motor.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")
@app.route("/crop")
def crop():
    return render_template("crop.html")
@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)