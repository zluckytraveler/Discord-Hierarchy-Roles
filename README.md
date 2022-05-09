# Discord Hierarchy Role Bot
A discord bot which allows users to have only the highest role you defined in a list.

# SETUP

STEP 1

Doownload this repository [HERE](https://github.com/zluckytraveler/discord-hierarchy-roles/archive/refs/heads/main.zip) 

STEP 2

Create a custom bot on [Discord Developer](https://discord.com/developers)

1. Create a Application.
2. Create a Bot.
3. Enable intents for the folowing settings: **PRESENCE INTENT, SERVER MEMBERS INTENT, MESSAGE CONTENT INTENT**
4. Create a token for the first time by selecting "Reset Token". Copy the token and save it, you will need it for the next step.
5. Select **URL Generator** located under **OAuth2**, then enable **bot** under Scopes, followed by **Administator** for Permissions.
6. Copy the generated url at he bottom of the page, and paste it into your browsers address bar.
7. Follow the Discord popup steps for inviting the bot to your Discord server.

STEP 3

Add your Discord Bot Token and Role ID's to `config.yml`, and save it.

# Install
**DOCKER CLI**

Simply run the command.

```docker run -d --restart=unless-stopped -v /PATH TO CONFIG/:/app/config.yml zluckytraveler/discord-hierarchy-roles```


**DOCKER BUILD**

STEP 1

Change the directory to where the files are stored.

```cd <PATH TO DIRECTORY>```

STEP 2

Build the image. The image name must be all lowercase without any spacing

```docker build -t <YOUR IMAGE NAME> .```

STEP #3

Start the container by using the Docker run command.

```docker run -d --restart=unless-stopped <YOUR IMAGE NAME>```
