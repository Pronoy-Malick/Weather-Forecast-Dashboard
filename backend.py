import requests

API_KEY = "2d4a3500ca0bc54214079698f71b16ca"

def get_data(place, days, kind):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    td = 8 * days
    filtered_data = filtered_data[:td]

    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Kolkata", days = 2, kind="Temperature"))