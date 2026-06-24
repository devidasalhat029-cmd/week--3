from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        "soil_moisture": 65,
        "temperature": 28,
        "humidity": 72,
        "pump_status": "ON"
    }
    return render_template("index.html", data=data)

@app.route('/details')
def details():
    return render_template("details.html")

@app.route('/login')
def login():
    data = {
        "soil_moisture": 65,
        "temperature": 28,
        "humidity": 72,
        "pump_status": "ON"
    }
    return render_template("login.html", data=data)
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")



@app.route('/weather')
def weather():
    return render_template("weather.html")

@app.route('/motor')
def motor():
    return render_template("motor.html")
@app.route('/crop')
def crop():
    return render_template("crop.html")

@app.route('/analytics')
def analytics():
    return render_template("analytics.html")

if __name__ == '__main__':
    app.run(debug=True)