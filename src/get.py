from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Create a handler for our read (GET) training
def training(id):
    # TODO - process the given id
    return {
        "title": "Bunny",
        "expires": "Easter",
        "achieved": get_timestamp()
    }