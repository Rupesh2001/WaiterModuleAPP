import json
import requests

API_BASE_URL = "http://waitermoduleapp.danfesolution.com/api/menu-item"  # Use the actual API endpoint
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYWRtaW5AbW9tb2hvdXNlLmNvbSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6Ik9yZ0FkbWluIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiI1MDM4OGM5NS00YzYwLTQxNTgtYTJkYS0wNGM1OTg4MWFkY2YiLCJPcmdhbml6YXRpb25Db2RlIjoiTU9NMjQxMTk0MDEiLCJvcmdfaWQiOiI2IiwiZXhwIjoxNzU1NTg2MzM3LCJpc3MiOiJZb3VySXNzdWVyIiwiYXVkIjoiWW91cklzc3VlciJ9.9wzAHOoiZsc-XHrOLX-_tMUnNKbIK41KDeP7VnzaBEs"

def check_connection():
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    resp = requests.get(API_BASE_URL, headers=headers)  # Test GET to API endpoint
    if resp.status_code in (200, 401):  # 401 means token invalid, so still reachable
        print("Connection established!")
        return True
    print(f"Connection failed: {resp.status_code} - {resp.text}")
    return False

def send_product_data(data):
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    resp = requests.post(API_BASE_URL, json=data, headers=headers)
    print(resp.status_code, resp.text)

def main():
    if check_connection():
        with open('product_data.json') as f:
            product_data = json.load(f)
        send_product_data(product_data)

if __name__ == "__main__":
    main()
