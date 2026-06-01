# Automated Agriculture Monitoring System

def agriculture_monitoring():

    for i in range(3):

        print("\n----- Agriculture Monitoring -----")

        soil_moisture = int(input("Enter Soil Moisture (%): "))
        temperature = int(input("Enter Temperature (°C): "))

        print("\nSoil Moisture:", soil_moisture, "%")
        print("Temperature:", temperature, "°C")

        # Soil Moisture Check
        if soil_moisture < 40:
            print("Soil is Dry")
            print("Water Pump: ON")

        if soil_moisture >= 40:
            print("Soil Moisture is Good")
            print("Water Pump: OFF")

        # Temperature Check
        if temperature > 35:
            print("High Temperature Alert!")

        if temperature <= 35:
            print("Temperature is Normal")


agriculture_monitoring()