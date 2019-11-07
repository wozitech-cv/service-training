from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Create a handler for our update (PUT) training record
def training(id):
    # TODO - process the given id
    return {
        "title": "Christmas",
        "expires": "Father",
        "achieved": get_timestamp()
    }