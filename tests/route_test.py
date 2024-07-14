import requests
from datetime import datetime, timedelta

# URL of the endpoint
url = 'http://127.0.0.1:5000/receive-mobility-data'

# Create sample data
bus_line_id = 'line 4'
start_time = datetime.now()
points = []

for i in range(20):
    point = {
        'timestamp': (start_time + timedelta(seconds=i)).isoformat(),
        'latitude': 40.7128 + i * 0.001,
        'longitude': -74.0060 + i * 0.001,
        'acceleration_x': 0.1 * i,
        'acceleration_y': 0.2 * i,
        'acceleration_z': 0.3 * i,
        'rotation_x': 0.01 * i,
        'rotation_y': 0.02 * i,
        'rotation_z': 0.03 * i
    }
    points.append(point)

data = {
    'bus_line': bus_line_id,
    'points': points
}

# Send POST request
response = requests.post(url, json=data)

# Print response
print(f"Status Code: {response.status_code}")
print("Response JSON:", response.json())
