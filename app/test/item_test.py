import requests

url = "http://127.0.0.1:8000/item/add_item"

data = {
  "item_code": 0,
  "item_name": "string",
  "item_stock": 0,
  "item_unit": "string",
  "item_manufact": "string",
  "item_phone": "string",
  "item_email": "string",
  "item_img": "string",
  "item_price": 0,
  "item_descript": "string"
}

files = {
    'image': ('image.jpeg', open('app/test/item_test.py', 'rb'), 'image/jpeg')
}

headers = {
    'Content-Type': 'multipart/form-data'
}

response = requests.post(url, headers=headers, data=data, files=files)

print(response.status_code)
print(response.json())
