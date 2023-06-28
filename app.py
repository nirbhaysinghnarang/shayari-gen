from flask import Flask, request
 
from shayari import Shayari
from twilio.twiml.messaging_response import MessagingResponse
 
 
app = Flask(__name__)
 
@app.route("/", methods=["POST"])
def generate():
    if not request.json.get("keywords"):
        return str("Invalid request body")
    return str((Shayari(request.json["keywords"].split(" ")).generate()))
 
 
if __name__ == "__main__":
    app.run()