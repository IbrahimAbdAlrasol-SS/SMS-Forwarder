from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import List, Dict

app = FastAPI()

messages: List[Dict] = []

@app.get("/forward")
async def forward_sms(
    msg: str = Query(..., description="The SMS message content"),
    time: str = Query(..., description="Time when the message was received"),
    in_number: str = Query(..., alias="in-number", description="Sender's phone number"),
    filter_name: str = Query(..., alias="filter-name", description="Name/identifier of the filter")
):
    """
    Forward an SMS message to the API server.

    Args:
        msg (str): The SMS message content.
        time (str): Time when the message was received.
        in_number (str): Sender's phone number.
        filter_name (str): Name/identifier of the filter.

    Returns:
        dict: A dictionary with a single key-value pair indicating the status of
            the forwarding process.
    """
    message = {
        "message": msg, # content
        "time": time, # real time of receiving the message
        "from": in_number, # sender phone number, or name if its Govermenet.
        "device": filter_name # its not really important, its a filter name.
    }
    # Add the message to the list of messages
    messages.append(message)
    # Return a dictionary with a single key-value pair indicating the status
    # of the forwarding process
    return {"status": "saved", "count": len(messages)}

@app.get("/messages")
async def get_all_messages() -> Dict[str, List[Dict[str, str]]]:
    """
    Get all the SMS messages forwarded to the API server.

    Returns:
        dict: A dictionary with a single key-value pair containing a list of all
            forwarded messages.
    """
    return {"messages": messages} # it will return all received sms message, it should be private!
