import logging
import os
import json
import requests

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.INFO)

SLACK_BOT_TOKEN = os.environ['XXX']
SLACK_APP_TOKEN = os.environ['XXX']
READWISE_TOKEN = 'XXX'

app = App(token=SLACK_BOT_TOKEN)

querystring = {
    "category": "books"
}

response = requests.get(
    url="https://readwise.io/api/v2/books/",
    headers={"Authorization": "Token " + READWISE_TOKEN},
    params=querystring
)

books = response.json()

querystring = {
    "category": "supplementals"
}

response = requests.get(
    url="https://readwise.io/api/v2/books/",
    headers={"Authorization": "Token " + READWISE_TOKEN},
    params=querystring
)

supplementals = response.json()

# Convert Python dict [JSON array] to Python string
books = json.dumps(books)
supplementals = json.dumps(supplementals)

# Create and write data to a JSON file
with open("bookList.json", "w") as fBooks:
    fBooks.write(books)

with open("supplementalList.json", "w") as fSupplementals:
    fSupplementals.write(supplementals)

# Read the JSON file
with open("bookList.json", "r") as fBooks:
    bookList = json.loads(fBooks.read())

with open("supplementalList.json", "r") as fSupplementals:
    supplementalList = json.loads(fSupplementals.read())

@app.event("app_mention")
def helper(say):
    say("I can help you get a curated list of your learning resources\n")
    say("1) DM me `My book list` to get your book list\n")
    say("2) DM me `My supplemental book list` to get your supplemental list")

@app.message("My book list")
def book_list(message, say):  # Returns a book list
    index = 0

    say("Here it is!")
    for i in bookList["results"]:
        index += 1
        say(str(index) + ". " + i["title"])  # Iterating through the json list

@app.message("My supplemental book list")
def supplemental_list(message, say):  # Returns a supplemental list
    index = 0

    say("Here it is!")
    for i in supplementalList["results"]:
        index += 1
        say(str(index) + ". " + i["title"])  # Iterating through the json list

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

# Closing file
fBooks.close()
fSupplementals.close()