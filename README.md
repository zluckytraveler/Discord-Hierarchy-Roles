# **Discord Hierarchy Role Bot**
A discord bot which allows users to have only the highest role you defined in a list.

# **SETUP**

**STEP 1**

Download this repository [HERE](https://github.com/zluckytraveler/discord-hierarchy-roles/archive/refs/heads/main.zip) 

**STEP 2**

Learn how to creat a custom bot and find a role id. If you already know how to do this please continue to STEP 3.

**DISCORD BOT** 
1. Go to [Discord Developer](https://discord.com/developers)
2. Create a Application.
3. Create a Bot.
4. Enable intents for the folowing settings: **PRESENCE INTENT, SERVER MEMBERS INTENT, MESSAGE CONTENT INTENT**
5. Create a token for the first time by selecting "Reset Token". Copy the token and save it, you will need it later on.
6. Select **URL Generator** located under **OAuth2**, then enable **bot** under Scopes, followed by **Administator** for Permissions.
7. Copy the generated url at he bottom of the page, and paste it into your browsers address bar.
8. Follow the Discord popup steps for inviting the bot to your Discord server.

**ROLE ID**
1. Select the gear icon to open your user settings
2. Select the Advance tab on side bar
3. Enable developer mode
5. Go to your server and select Server Settings
6. Select the Roles setting
7. Select the three vertical dots next tot he role name
9. Now copy the Role ID

**STEP 3**

Add your Discord Bot Token and Role ID's to `config.yml`, and save the file.

You can add as many Role ID's you want to the file by creating a new entry, it has no limit. The first Role ID is going to be highest role that you define, with every role below being in a lower position in the hierarchy.


# **Install**
@settings {
  font-size: 100;
**DOCKER CLI**}

Simply run the command.

```docker run -d --restart=unless-stopped -v /PATH TO CONFIG/:/app/config.yml zluckytraveler/discord-hierarchy-roles```


**DOCKER BUILD**

STEP 1

Change the directory to where the files are stored.

```cd <PATH TO DIRECTORY>```

STEP 2

Build the image. The image name must be all lowercase without any spacing

```docker build -t <YOUR IMAGE NAME> .```

STEP 3

Start the container by using the Docker run command.

```docker run -d --restart=unless-stopped <YOUR IMAGE NAME>```

**LOCAL**

STEP 1

Change the directory to where the files are stored.

```cd <PATH TO DIRECTORY>```

STEP 2

Install the requirements file. Depending on your pip you may need to use `pip`, `pipx`, or `pip3`.

```pip install -r requirements.txt```


STEP 3

Run the Bot. Depending on your python you may need to use `python`, `python2`, or `python3`.

```python app.py```
