import sys
import os
import asyncio

# Ensure library is in path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from atvnotif import discover_devices, decode_qr_image

def test_qr_decode():
    import sys
    qr_image_path = sys.argv[1] if len(sys.argv) > 1 else "test_qr.jpg"
    print(f"Testing QR decode on: {qr_image_path}")
    try:
        data = decode_qr_image(qr_image_path)
        print("QR Decode Result:")
        print("  IP Address:  ", data.get("ip"))
        print("  Pairing Code:", data.get("pairing_code"))
        print("SUCCESS: QR decode test passed!")
    except Exception as e:
        print("FAILED: QR decode failed:", e)
        raise e

def test_discovery():
    print("Testing network discovery (scanning for 5 seconds)...")
    devices = discover_devices(timeout=5.0)
    print(f"Found {len(devices)} device(s):")
    for device in devices:
        print(f" - {device['name']} at {device['host']}:{device['port']} (Pairing Code: {device['pairing_code']})")

if __name__ == "__main__":
    test_qr_decode()
    test_discovery()
