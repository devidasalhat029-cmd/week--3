from flask import Flask

app = Flask(__name__)

#Project data :dictionary
farm_info = {
    "project_name": "Automated Agricultural Monitoring System",
    "location": "Kalamboli Farm",
    "crop": "Rice",
    "farmer": "Yogita",
    "status": "Healthy"
}

sensor_records = [
    {"id": 1, "temperature": 28, "humidity": 65},
    {"id": 2, "temperature": 30, "humidity": 60},
    {"id": 3, "temperature": 27, "humidity": 70},
    {"id": 4, "temperature": 29, "humidity": 68},
    {"id": 5, "temperature": 31, "humidity": 58}
]

@app.route("/")
def home():
    return f"""
    <h1>{farm_info['project_name']}</h1>
    <p>Smart system for monitoring crop and environmental conditions.</p>
    """  
@app.route("/records")
def records():
    records_html = "<h2>Sensor Records</h2><ul>"
    for record in sensor_records:
        records_html += f"<li>Record {record['id']}: Temperature: {record['temperature']}°C, Humidity: {record['humidity']}%</li>"
    records_html += "</ul>"
    return records_html

@app.route("/status")
def status():
    
    return f"""
    <h2>Farm Status</h2>
    <p>Location: {farm_info['location']}</p>
    <p>Crop: {farm_info['crop']}</p>
    <p>Farmer: {farm_info['farmer']}</p>
    <p>Status: {farm_info['status']}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)