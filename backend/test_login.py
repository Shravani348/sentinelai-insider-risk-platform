# backend/test_login.py
import requests

print("Sending login request...")
response = requests.post(
    'http://127.0.0.1:8000/api/v1/auth/access-token', 
    data={'username':'ADM-001', 'password':'admin123'}
)

print(f"Status Code: {response.status_code}")
print(f"Error Details: {response.text}")