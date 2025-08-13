import requests

API_BASE_URL = "https://api-waitermoduleapp.danfesolution.com/api/products"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYWRtaW5AbW9tb2hvdXNlLmNvbSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6Ik9yZ0FkbWluIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiI1MDM4OGM5NS00YzYwLTQxNTgtYTJkYS0wNGM1OTg4MWFkY2YiLCJPcmdhbml6YXRpb25Db2RlIjoiTU9NMjQxMTk0MDEiLCJvcmdfaWQiOiI2IiwiZXhwIjoxNzU1NTg2MzM3LCJpc3MiOiJZb3VySXNzdWVyIiwiYXVkIjoiWW91cklzc3VlciJ9.9wzAHOoiZsc-XHrOLX-_tMUnNKbIK41KDeP7VnzaBEs"
  # Replace with your token

def get_product_list():
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    try:
        resp = requests.get(API_BASE_URL, headers=headers)
        if resp.status_code == 200:
            products = resp.json()
            print("Product List:")
            for product in products:
                print(product)
        else:
            print(f"Failed to retrieve product list: {resp.status_code} - {resp.text}")
    except requests.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    get_product_list()
