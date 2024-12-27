import jwt

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM1MzEzMDc4LCJpYXQiOjE3MzUzMTI3NzgsImp0aSI6IjVhMmFiMjMwYWZlMzQxNDhiM2M3MWVhY2Q0ZWQzZTllIiwidXNlcl9pZCI6MX0.pf9LZ-ZdNG4EPyA1G4DYOcpuZlPq3WBkfQ6CUCItCmQ"  # Replace with your actual token

try:
    decoded_access = jwt.decode(access_token, options={"verify_signature": False})
    print(decoded_access)
except jwt.ExpiredSignatureError:
    print("Token has expired")
except jwt.InvalidTokenError:
    print("Invalid token")
