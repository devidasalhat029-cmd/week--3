# Main Entity Dictionary
farm = {
    "farm_id": 101,
    "farmer_name": "Ramesh Patil",
    "village": "Latur",
    "crop": "Soybean",
    "soil_moisture": 65,
    "temperature": 30
}

# Second Dictionary (Bonus)
weather = {
    "city": "Latur",
    "temperature": 32,
    "humidity": 70,
    "rainfall": "Low"
}

# List of Dictionaries (5 records)
sensor_records = [
    {"sensor_id": 1, "crop": "Soybean", "moisture": 65},
    {"sensor_id": 2, "crop": "Cotton", "moisture": 55},
    {"sensor_id": 3, "crop": "Wheat", "moisture": 70},
    {"sensor_id": 4, "crop": "Sugarcane", "moisture": 80},
    {"sensor_id": 5, "crop": "Maize", "moisture": 60}
]

def get_status(moisture):
    if moisture >= 60:
        return "Healthy"
    return "Needs Water"

print("Sensor Records:")
for record in sensor_records:
    print(record["crop"], "-", get_status(record["moisture"]))

def search_records(crop_name):
    for record in sensor_records:
        if record["crop"].lower() == crop_name.lower():
            return record
    return "Record Not Found"

crop = input("Enter crop name: ")
print(search_records(crop))