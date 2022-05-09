# Discord Hierarchy Role Bot
A discord bot which allows users to have only the highest role you defined in a list.

# Install
**DOCKER CLI**

Simply run the command.

```docker run -d --restart=unless-stopped -v /PATH TO CONFIG/:/app/config.yml zippytron/zltfiverr```


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
