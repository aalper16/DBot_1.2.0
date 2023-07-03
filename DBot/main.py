import discord 
import webbrowser as web
import os
import pyautogui as pg
import random
from playsound import playsound


openedapps = []
messages = []


memes = ["pikachu_meme.png", "makeyoutraumaed.jpeg", "wrongface.png", "whattheface.png", "bruhh.png", "dbotmeme.jpg", "heheboi.jpeg", "cat.jpeg", "shorse.jpg", "oksir.jpg", "panik.jpg"]

intents = discord.Intents.default()

intents.message_content = True 

username = os.environ["USERNAME"]
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f"Giriş yapılan hesap: {client.user}")
    

    

@client.event
async def on_message(message):


    print("kanal: ",  message.channel)
    print("gönderen :",  message.author)
    print(message.content)
    print("-------------------------")

    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send('`Merhaba!`')

    elif message.content.startswith('$bay bay'):
        await message.channel.send('`Görüşürüz!`')

    elif message.content.startswith('$nasılsın'):
        await message.channel.send('`Her zaman iyi ve çevrimiçiyim!`')
        

    elif message.content.startswith('$chrome'):
        openedapps.append("chrome")
        os.startfile('chrome.exe')
        await message.channel.send("`chrome'u açtım!`")
        
        print(openedapps)

    elif message.content.startswith('$windows'):
        openedapps.append("windows")
        pg.hotkey("win")
        await message.channel.send('`windows ana menüsünü açtım!`')
        
        print(openedapps)

    elif message.content.startswith('$youtube'):
        openedapps.append("youtube")
        web.open('https://www.youtube.com')
        await message.channel.send("`youtube'u açtım!`")
        
        print(openedapps)
 
    elif message.content.startswith('$brave'):
        openedapps.append("brave")
        os.startfile('brave.exe')
        await message.channel.send("`brave'i açtım!`")
        
        print(openedapps)

    elif message.content.startswith('$komut istemi'):
        openedapps.append("cmd")
        os.startfile('cmd.exe')
        await message.channel.send("`komut istemi'ni açtım!`")
        
        print(openedapps)


    elif message.content.startswith('$ayarlar'):
        openedapps.append("settings")
        os.system("start ms-settings:")
        await message.channel.send("`ayarlar'ı açtım!`")
        
        print(openedapps)


    elif message.content.startswith('$instagram'):
        openedapps.append("instagram")
        web.open("https://www.instagram.com/")
        await message.channel.send("`instagram'ı açtım!`")
        
        print(openedapps)


    elif message.content.startswith('$facebook'):
        openedapps.append("facebook")
        web.open("https://www.facebook.com")
        await message.channel.send("`facebook'u açtım!`")
        
        print(openedapps)


    elif message.content.startswith('$twitch'):
        openedapps.append("twitch")
        web.open('https://www.twitch.com')
        await message.channel.send("`twitch'i açtım!`")
        
        print(openedapps)


#? UPDATE   
#!TkAssistant
    elif message.content.startswith('$TkAssistant'):
        openedapps.append("TkAssistant")
        await message.channel.send("`https://www.dosya.tc/server42/qgz35v/TkAssistant-1.1.0-main.zip.html`")
        await message.channel.send("`Bu linkten TkAssistant 1.1.0'ı indirebilirsiniz.`")
        await message.channel.send("`https://github.com/gitcloneAlperTuna/TkAssistant-1.1.0`")
        await message.channel.send("`Bu linkte de programın komutlarını bulabilirsiniz.`")
        await message.channel.send("`by Alper Tuna KILIÇ`")
        
        print(openedapps)


    elif message.content.startswith('$free_money'):
        openedapps.append("Rickroll")
        await message.channel.send("`rickrolled!`")
        print(openedapps)
        playsound ("rickroll.mp3")

    elif message.content.startswith('$aternos'):
        openedapps.append("aternos")
        print(openedapps)
        web.open("https://aternos.org/server/")
        await message.channel.send("`aternos'u açtım`")
        


    elif message.content.startswith('$hakkında'):
        openedapps.append("about")
        await message.channel.send("`Alper Tuna KILIÇ tarafından kodlanmıştır.`")
        await message.channel.send("`Kopyalanamaz, satılamaz.`")
        await message.channel.send("`Bu botu kullanarak şunları kabul etmiş olursunuz: `")
        await message.channel.send("`Bilgisayar sisteminde değişiklik veya olası hasarlar,`")
        await message.channel.send("`Tarayıcı üzerinde web sitesi açma,`")
        await message.channel.send("`Göderilen mesajları görme, `")
        await message.channel.send("`Bilgisayara dosya indirme, kaldırma,`")
        await message.channel.send("`Bilgisayardaki dosyaları okuma.`")
        print(openedapps)

    
    elif message.content.startswith('$komik'):
        openedapps.append("memes")
        f = open("images/" + random.choice(memes), "rb")
        print(openedapps)

        picture = discord.File(f)

       
        await message.channel.send(file = picture)
        f.close()
        


    elif message.content.startswith('$username'):
        openedapps.append("username")
        await message.channel.send("`" + username + "`")
        print(openedapps)




    elif message.content.startswith('$stat'):
        await message.channel.send("`geliştirme aşamasında!\nEğer bu komutu yazdığınızda ekranda bir yazı belirmiyorsa bot bakım aşamasındaır.`"),
    

    
    elif message.content.startswith('$help'):
        openedapps.append("help")
        await message.channel.send("`bana $merhaba diyebilirsin!`")
        await message.channel.send("`benimle vedalaşmak için $bay bay diyebilirsin!`")
        await message.channel.send("`bana durumumu sormak için $nasılsın diyebilirsin!`")
        await message.channel.send("`chrome'u açmak istersen $chrome yazabilirsin.`")
        await message.channel.send("`windows ana menüsünü açmak istersen $windows yazabilirsin.`")
        await message.channel.send("`youtube'u açmak istersen $youtube yazabilirsin.`")
        await message.channel.send("`brave'i açmak istersen $brave yazabilirsin.`")
        await message.channel.send("`komut istemi'ni açmak için $komut istemi yazabilirsin.`")
        await message.channel.send("`ayarlar'ı açmak için $ayarlar yazabilirsin.`")
        await message.channel.send("`instagram'ı açmak için $instagram yazabilirsin.`")
        await message.channel.send("`facebook'u açmak istersen $facebook yazabilirsin.`")
        await message.channel.send("`twitch'i açmak için $twitch yazabilirsin.`")
        await message.channel.send("`$TkAssistant, Alper Tuna'nın TkAssistant adlı programını indirmek için kullanabilirisiniz`")
        await message.channel.send("`aternos'u açmak istersen $aternos yazabilirsin.`")
        await message.channel.send("`$komik, sana komik meme'ler gönderir.`")
        await message.channel.send("`$username, senin bilgisayarının kullanıcı adını gösterir`")
        await message.channel.send("`$stat, botun durumunu gösterir.`")

        print(openedapps)

















































#! TOKEN
client.run('MTExODA3MzQ2NzM4OTEwNDIwOA.GsDvq3.JylTmhGOquguxkcOC6hIcoK6HcdcgAGCa34vKc')