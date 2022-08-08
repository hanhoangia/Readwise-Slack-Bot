# Readwise-Slack-Bot
## About
Phoenix is a Slack Bot I developed to study API Testing using Slack API and Readwise API.

## Usage
By mentioning Phoenix `@Phoenix`, it responds with the options that you can ask it to do (i.e. get book and supplemental book list).

## Demo
[Insert demonstrating videos here]

## How it works
The program starts by making a call to Readwise API that requests and receives the corresponding data (i.e. book list, podcast list). When you make a contact with Phoenix, Phoenix is triggered and tells the program to act correspondingly (e.g. send a book list) through Slack API.<br />
The entire bot is written in Python 3.10.6.

## Prerequisites
- Python 3
- Slack Client
- Slack Bolt Framework (pip3 install slack_bolt)
- Python Requests Library (pip3 install requests)
- IDE (VSCode)

## Installation
<ol>
<li>Install Phoenix to your Slack workspace.</li>
<li>Install the prerequisities.</li>
<li>Clone this repo.</li>
<li>Run the program!</li>
</ol>
**Note: Change the token strings 'XXX' to that of your own tokens and you're good to go!**

## Next Steps
- Refactor the code.
- Dockerize the program and host it on GCP.
- Add a Redirect URL and publish the bot to the Slack App Directory
- Continue to expand the functionality of the bot (e.g. get the highlights of a specific object like book and podcast, get the highlight details with a specific keyword from all sources).

## References
- [API Testing for Beginners (Tutorial)](https://www.youtube.com/watch?v=GZvSYJDk-us)
- [Slack API Documentation](https://api.slack.com/docs)
- [Readwise API Documentation](https://readwise.io/api_deets)

**Credit: Made by Han Hoang. MIT License.**
