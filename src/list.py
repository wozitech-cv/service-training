from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
TRAINING = {
    "Westerman": {
        "title": "Bobbie",
        "temp": "Westerman",
        "achieved": get_timestamp()
    },
    "Farrell": {
        "title": "Doug",
        "temp": "Farrell",
        "achieved": get_timestamp()
    },
    "Brockman": {
        "title": "Kent",
        "temp": "Brockman",
        "achieved": get_timestamp()
    },
    "Easter": {
        "title": "Bunny",
        "expires": "Easter",
        "achieved": get_timestamp()
    }
}

# Create a handler for our read (GET) training
def training():
    """
    This function responds to a request for /api
    with the complete lists of training records

    :return:        sorted list of training
    """
    # Create the list of people from our data
    return [TRAINING[key] for key in sorted(TRAINING.keys())]