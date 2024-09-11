import discord
from discord.ext import tasks
import json
import asyncio
import datetime
import os 
from colorama import Fore, Style, init
from termcolor import colored
import logging
import ctypes
import itertools


for logger_name in logging.root.manager.loggerDict:
    logging.getLogger(logger_name).disabled = True


init(autoreset=True)

ctypes.windll.kernel32.SetConsoleTitleW("Discord Voice Channel Switcher - xz2r")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

TOKEN = config['token']

class VoiceBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.voice_channel = None
        self.voice_connection = None
        self.start_time = None
        self.status_message = None
        self.selected_guild = None
        self.selected_channel = None 
        self.last_update_time = None 

    async def on_ready(self):
        print(f'Bot giriş yaptı: {self.user}')
        await self.list_guilds()

    async def list_guilds(self):
        self.clear_console()
        print("""
    ██╗  ██╗███████╗██████╗ ██████╗ 
    ╚██╗██╔╝╚══███╔╝╚════██╗██╔══██╗
     ╚███╔╝   ███╔╝  █████╔╝██████╔╝
     ██╔██╗  ███╔╝  ██╔═══╝ ██╔══██╗
    ██╔╝ ██╗███████╗███████╗██║  ██║
    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝               
                               Created by xz2r
              \nBulunan sunucular:""")
        for idx, guild in enumerate(self.guilds, start=1):
            print(f"{idx}: {guild.name}")

        if self.selected_guild is None:
            guild_index = int(input("\nBir sunucu seçin (sayı girin): ")) - 1
            if 0 <= guild_index < len(self.guilds):
                self.selected_guild = self.guilds[guild_index]
                print(f"Seçilen sunucu: {self.selected_guild.name}")
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
                await self.list_guilds()

        await self.list_connectable_voice_channels(self.selected_guild)

    async def list_connectable_voice_channels(self, guild):
        """
        Botun bağlanma iznine sahip olduğu ses kanallarını listeler.
        """
        self.clear_console()
        connectable_channels = [] 

        for vc in guild.voice_channels:
            permissions = vc.permissions_for(guild.me)
            if permissions.connect:
                connectable_channels.append(vc)

        if not connectable_channels:
            print("""
        ██╗  ██╗███████╗██████╗ ██████╗ 
        ╚██╗██╔╝╚══███╔╝╚════██╗██╔══██╗
         ╚███╔╝   ███╔╝  █████╔╝██████╔╝
         ██╔██╗  ███╔╝  ██╔═══╝ ██╔══██╗
        ██╔╝ ██╗███████╗███████╗██║  ██║
        ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝               
                                   Created by xz2r
                  \nBu sunucuda botun bağlanabileceği ses kanalı bulunmuyor.:""")
            return

        print("""
        ██╗  ██╗███████╗██████╗ ██████╗ 
        ╚██╗██╔╝╚══███╔╝╚════██╗██╔══██╗
         ╚███╔╝   ███╔╝  █████╔╝██████╔╝
         ██╔██╗  ███╔╝  ██╔═══╝ ██╔══██╗
        ██╔╝ ██╗███████╗███████╗██║  ██║
        ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝               
                                   Created by xz2r
                    \nBotun bağlanabileceği ses kanalları:""")
        for idx, vc in enumerate(connectable_channels, start=1):
            print(f"{idx}: {vc.name}")

        channel_index = int(input("\nBir ses kanalı seçin (sayı girin): ")) - 1

        if 0 <= channel_index < len(connectable_channels):
            self.selected_channel = connectable_channels[channel_index]
            print(f"Seçilen ses kanalı: {self.selected_channel.name}")

            self.voice_channel = self.selected_channel
            await self.join_voice_channel()
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
            await self.list_connectable_voice_channels(guild)

    async def join_voice_channel(self):
        if self.voice_channel:
            self.voice_connection = await self.voice_channel.connect()

            await self.voice_channel.guild.change_voice_state(channel=self.voice_channel, self_mute=False, self_deaf=True)

            self.start_time = datetime.datetime.now()
            self.clear_console()
            print(f'{self.voice_channel.name} kanalına bağlanıldı.')

            self.update_console_status.start()

            text_channel = discord.utils.get(self.voice_channel.guild.text_channels, name="genel") 
            if text_channel:
                self.status_message = await text_channel.send(f'{self.voice_channel.name} kanalına bağlanıldı. Geçen süre: 0:00:00')
                self.update_status.start()
            
            self.check_voice_connection.start()

    @tasks.loop(seconds=10)
    async def update_status(self):
        if self.voice_connection and self.voice_connection.is_connected() and self.status_message:
            elapsed_time = datetime.datetime.now() - self.start_time

            if not self.last_update_time or (datetime.datetime.now() - self.last_update_time).total_seconds() > 10:
                await self.status_message.edit(content=f'{self.voice_channel.name} kanalına bağlı. Geçen süre: {str(elapsed_time).split(".")[0]}')
                self.last_update_time = datetime.datetime.now()

    @tasks.loop(seconds=1)
    async def update_console_status(self):
        self.clear_console()
        self.print_channel_info(self.voice_channel)

    @tasks.loop(seconds=5)
    async def check_voice_connection(self):
        if not self.voice_connection or not self.voice_connection.is_connected():
            print(f"{self.voice_channel.name} kanalından bağlantı kesildi. Yeniden bağlanılıyor...")
            await self.join_voice_channel()

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_channel_info(self, channel):
        elapsed_time = datetime.datetime.now() - self.start_time
        print(f"Kanal Adı: {channel.name}")
        print(f"Kanal ID'si: {channel.id}")
        print(f"Kanalda Bulunan Üyeler: {', '.join([member.name for member in channel.members])}")
        print(f"Geçirilen Süre: {str(elapsed_time).split('.')[0]}")

    async def on_disconnect(self):
        print('Bot bağlantısı kesildi.')
        self.update_status.stop()
        self.update_console_status.stop()
        self.check_voice_connection.stop()

bot = VoiceBot()
bot.run(TOKEN)
