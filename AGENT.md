# Agent Guidelines: `atvnotif` (Python Library)

This repository houses the standalone Python library (`atvnotif`) used for sending encrypted notifications to the Android TV Notifier app.

## Project Structure
*   `atvnotif/client.py`: The client (`ATVNotifier`) that handles encryption/decryption, sending notifications, fetching app lists, and opening apps.
*   `atvnotif/discover.py`: Zeroconf discovery for locating devices on the local network.
*   `atvnotif/qr.py`: QR code and OCR decoding logic for setup pairing.

## How to Release and Push New Changes

### 1. Bump the Version
Update the version inside [pyproject.toml](file:///run/media/liveuser/CachyOS/@home/blu/Projects/atvnotif/pyproject.toml):
```toml
[project]
name = "atvnotif"
version = "0.1.x"  # Bump this
```

### 2. Build the Package
From the repository root, run the build module:
```bash
python3 -m build
```

### 3. Upload to PyPI
Use `twine` (located in the user's local path) with the PyPI token found in the parent `.env` file (`/run/media/liveuser/CachyOS/@home/blu/Projects/.env`):
```bash
export $(grep -v '^#' ../.env | xargs)
/home/liveuser/.local/bin/twine upload --username __token__ --password "$PYPI_TOKEN" dist/atvnotif-0.1.x*
```

### 4. Sync Nested Copies
Whenever you update code in this library, **always** synchronize the updated `.py` files to the nested library folder inside the HASS integration workspace:
```bash
cp -rf atvnotif/*.py ../atvnotif_hass/custom_components/atvnotif/atvnotif/
```

### 5. Commit and Push to GitHub
```bash
git add .
git commit -m "Bump to version 0.1.x"
git push
```
