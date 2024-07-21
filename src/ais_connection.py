import websockets
import json
import logging
from utils import print_ship_table, get_ship_type_description
from config import API_KEY, URI, BOUNDING_BOX

logging.info("Connecting...")


async def connect_to_ais_stream():
    ships = {}
    subscription_message = {
        "APIKey": API_KEY,
        "BoundingBoxes": BOUNDING_BOX,
        "FiltersShipMMSI": [],
        "FilterMessageTypes": ["ShipStaticData"],
    }
    logging.info("Connected!")
    try:
        async with websockets.connect(URI) as websocket:
            await websocket.send(json.dumps(subscription_message))
            logging.info("Subscription message sent.")

            try:
                async for message in websocket:
                    ais_data = json.loads(message)
                    update_ships_dict(ais_data, ships)
                    print_ship_table(ships)
            except Exception as e:
                logging.error(f"Error handling message: {e}")
    except Exception as e:
        logging.error(f"Connection error: {e}")
        logging.error("Traceback:", exc_info=True)


def update_ships_dict(ais_data, ships):
    message = ais_data.get("Message", {}).get("ShipStaticData")
    if message and message.get("Valid", False):  # Ensure the message is valid
        ship_id = message.get("UserID")
        if ship_id:
            print("Ship ID:", ship_id)  # Debug print to check ship ID
            # Extract ship type using the get_ship_type_description function
            ship_type = get_ship_type_description(message.get("Type"))
            # Extract ship destination, default to 'Unknown' if not available
            ship_destination = message.get("Destination", "Unknown")

            # Store or update the ship's information in the dictionary
            ships[ship_id] = {
                "Name": message.get("Name", "Unknown"),
                "Type": ship_type,
                "Destination": ship_destination,
            }
