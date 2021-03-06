# DISCORD HIERARCHY ROLE BOT
A discord bot which allows users to have only the highest role in a defined list.

The bot will not modify any user's roles that you do not define in your `config.yml` file, keeping them safe from removal.
<br />
<br />
# SETUP

## <ins>STEP 1</ins>

Download this repository [HERE](https://github.com/zluckytraveler/discord-hierarchy-roles/archive/refs/heads/main.zip) 
<br />
<br />
## <ins>STEP 2</ins>
Learn how to create a <ins>Discord Bot</ins> and find a <ins>Discord ID</ins>.<br />

If you already know how to do this continue to STEP 3.

### DISCORD BOT
1. Go to [Discord Developer](https://discord.com/developers)
2. Create a Application.
3. Create a Bot.
4. Enable intents for `PRESENCE INTENT`, `SERVER MEMBERS INTENT`, `MESSAGE CONTENT INTENT`
6. Create a token by selecting `Reset Token`, then copy and save the token, you will need it later.
7. Under `OAuth2` select `URL Generator`, then enable `bot` & `Administator` under `Scopes` & `Permissions`.
8. Copy the generated url at he bottom of the page, and paste it into your browsers address bar.
9. Follow the Discord popup steps for inviting the bot to your Discord server.

### DISCORD ID
1. Login to your Discord Account.
2. Select the gear icon to open your user settings.
3. Select the Advance tab on the side bar.
4. Enable developer mode.
5. Right click on your Role.
8. Now copy the ID. 
<br />

## <ins>STEP 3</ins>
Add your Discord Bot Token and Role ID's to `config.yml`, and save the file.

You can add as many Role ID's you want to the file by creating a new entry, it has no limit. The first Role ID is going to be highest role that you define, with every role below being in a lower position in the hierarchy.
<br />
<br />
<br />
# INSTALL

## DOCKER CLI

Simply run the command.

```docker run --name Hierarchy-Role-Bot -d --restart=unless-stopped -v /PATH TO CONFIG/:/app/config.yml zluckytraveler/discord-hierarchy-roles```
<br />
<br />
## DOCKER BUILD

### <ins>STEP 1</ins>
Change the directory to where the files are stored.

```cd <PATH TO DIRECTORY>```

### <ins>STEP 2</ins>
Build the image. The image name must be all lowercase without any spacing

```docker build -t <YOUR IMAGE NAME> .```

### <ins>STEP 3</ins>
Start the container by using the Docker run command.

```docker run -d --restart=unless-stopped <YOUR IMAGE NAME>```
<br />
<br />
## LOCAL

### <ins>STEP 1</ins>

Change the directory to where the files are stored.

```cd <PATH TO DIRECTORY>```

### <ins>STEP 2</ins>

Install the requirements. <br />

```pip3 install -r requirements.txt```


### <ins>STEP 3</ins>

Run the Bot. <br />

```python3 app.py```
