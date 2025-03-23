import os

SECRET_KEY = os.urandom(24).hex()

with open(".env", "a") as f:
    f.write(f"\nFLASK_SECRET_KEY={SECRET_KEY}\n")

print("Secret Key Generated:", SECRET_KEY)