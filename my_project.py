# Main entity dictionary
farm = {
    "farm_id": 101,
    "farmer_name": "Babn Alhat",
    "crop": "Soybean",
    "soil_moisture": 65,
    "temperature": 30,
    "status": "Healthy"
}

#ACCESSING DICTIONARY VALUES
print("Farm ID:", farm["farm_id"])
print("Farmer Name:", farm["farmer_name"])
print("Crop:", farm["crop"])
print("Soil Moisture:", farm["soil_moisture"])
print("Temperature:", farm["temperature"])
print("Status:", farm["status"])

# List of dictionaries (5 records)
sensor_records = [
    {"sensor_id": 1, "crop": "Soybean", "moisture": 65, "temperature": 30},
    {"sensor_id": 2, "crop": "Cotton", "moisture": 55, "temperature": 32},
    {"sensor_id": 3, "crop": "Wheat", "moisture": 70, "temperature": 28},
    {"sensor_id": 4, "crop": "Sugarcane", "moisture": 80, "temperature": 29},
    {"sensor_id": 5, "crop": "Maize", "moisture": 60, "temperature": 31}
]



# get_status() function
def get_status(moisture):
    if moisture >= 60:
        return "Healthy"
    else:
        return "Needs Water"

# Print records using loop
print("Sensor Records:")
for record in sensor_records:
    status = get_status(record["moisture"])
    print(
        f"Sensor ID: {record['sensor_id']},\n "
        f"Crop: {record['crop']},\n "
        f"Moisture: {record['moisture']}%,\n "
        f"Temperature: {record['temperature']}°C,\n "
        f"Status: {status}"
    )

# Bonus: Second dictionary type
weather_data = {
    "city": "Latur",
    "temperature": 30,
    "humidity": 70,
    "rainfall": "Low"
}

# Challenge: search_records() function
def search_records(crop_name):
    for record in sensor_records:
        if record["crop"].lower() == crop_name.lower():
            return record
    return "Record not found"

print("\nSearch Result:")
print(search_records("Wheat"))