# atvnotif

A Python client library for sending encrypted notifications to the **Android TV Notifier** app (`com.smrtprjcts.atvnotif`).

## Installation

```bash
pip install atvnotif
```

## Usage

```python
import asyncio
from atvnotif import ATVNotifier

async def main():
    # Replace with your TV's IP address and pairing code (remove hyphens or leave them, the library cleans it)
    notifier = ATVNotifier("192.168.1.100", "1234-5678-ABCD")
    
    await notifier.async_notify(
        message="Someone is at the door!",
        title="Doorbell Alert",
        duration=10,
        position=0,  # Top-Right
        notif_sound=True
    )

if __name__ == "__main__":
    asyncio.run(main())
```
