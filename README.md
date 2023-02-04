# Reactor

This code is setting up a Telegram client to access a Telegram account via the Telethon library. The code is loading environmental variables from a dotenv file, setting the logging level to Warning, then creating a client with the credentials from the dotenv file. Finally, the code sets an event handler so that when a new message arrives in the specified target chat, the client will react to it with the specified emoji.
