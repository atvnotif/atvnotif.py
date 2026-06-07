import asyncio
import sys
import os

# Add parent directory to sys.path so we can import atvnotif without installing it
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from atvnotif import ATVNotifier

async def test():
    # Use a dummy IP and a dummy pairing code
    client = ATVNotifier("127.0.0.1", "1234-abcd-5678-efgh")
    
    print("Deriving key...")
    derived_key = client.key
    print(f"Key (length {len(derived_key)}): {derived_key}")
    
    # Check that key length is 32 bytes
    assert len(derived_key) == 32, "Key must be exactly 32 bytes!"
    
    payload = {
        "title": "Test Title",
        "msg": "Test Message",
    }
    
    print("Encrypting payload...")
    encrypted = client.encrypt_payload(payload)
    print(f"Encrypted data (length {len(encrypted)}): {encrypted[:20].hex()}...")
    
    # Check that length of encrypted data is at least IV (12) + Tag (16) + ciphertext
    assert len(encrypted) > 28, "Encrypted payload too short!"
    
    print("All encryption checks passed successfully!")

if __name__ == "__main__":
    asyncio.run(test())
