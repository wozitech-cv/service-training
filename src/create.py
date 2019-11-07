from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Create a handler for our create (POST) training record
def training():
    return {
        "title": "Krueger",
        "expires": "Freddie",
        "achieved": get_timestamp()
    }