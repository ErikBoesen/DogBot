# DogBot GroupMe Bot

## Introduction

A simple GroupMe bot that reacts to a user saying "dog" in a group by sending a picture of a dog.

## Prerequisites
DogBot is meant to run on AWS Lambda using the Serverless framework.

To install serverless on your local machine:
```sh
npm install -g serverless
```

## Deployment
Install `pip` dependencies locally in the `vendor` directory:
```sh
pip install -r requirements.txt -t vendor
```

Deploy using serverless:
```sh
serverless deploy
```

The bot should now be ready to receive messages! A lambda function URL will be logged that can be used as the MeBots bot callback URL to receive messages.

Check out the [MeBots Help Group](https://mebots.io/help) if you need any guidance.

## Logs
To view your bot's logs:
```sh
serverless logs -f receive
```

## Author
[Erik Boesen](https://github.com/ErikBoesen)
