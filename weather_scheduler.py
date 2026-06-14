import requests
from datetime import datetime

def check_weather(lat, lon, location_name):
    print(f"\nFetching NWS weather data for {location_name}...")
    headers = {"User-Agent": "TennisTMate_AutoScheduler/1.0 (aden.f.ingwerson@gmail.com)"}
    
    try:
        # Step 1: Get the exact grid endpoints for these coordinates
        points_url = f"https://api.weather.gov/points/{lat},{lon}"
        res = requests.get(points_url, headers=headers).json()
        forecast_url = res['properties']['forecastHourly']
        
        # Step 2: Get the hourly forecast
        forecast = requests.get(forecast_url, headers=headers).json()
        periods = forecast['properties']['periods']
        
        print(f"--- Next 5 Hours in {location_name} ---")
        for p in periods[:5]:
            time_str = datetime.fromisoformat(p['startTime']).strftime('%I:%M %p')
            pop = p.get('probabilityOfPrecipitation', {}).get('value') or 0
            
            # Highlight bad weather
            alert = "🚨 " if pop >= 50 or "Rain" in p['shortForecast'] or "Thunder" in p['shortForecast'] else "✅ "
            
            print(f"{alert}{time_str}: {p['temperature']}°F | Rain chance: {pop}% | Wind: {p['windSpeed']} | {p['shortForecast']}")
            
    except Exception as e:
        print(f"Error fetching weather for {location_name}: {e}")

if __name__ == "__main__":
    # Coordinates for Holdrege and Hastings
    check_weather(40.4403, -99.3734, "Holdrege, NE")
    check_weather(40.5858, -98.3898, "Hastings, NE")
