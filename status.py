import json
import os

STATUS_FILE = "status.json"

def update_status(key, value):
    """Update the status of various processes."""
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            status = json.load(f)
    else:
        status = {}

    status[key] = value

    with open(STATUS_FILE, "w") as f:
        json.dump(status, f, indent=4)

def get_status():
    """Retrieve the current status."""
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            return json.load(f)
    return {}
