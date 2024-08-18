import discord
from discord.ext import commands
import random
import os

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents) # type: ignore




@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def bilgi(ctx):
    bilgi_metni = (
        "Çevre kirliliği, doğanın hava, su ve toprak gibi temel unsurlarının insan faaliyetleri sonucu zarar görmesi anlamına gelir. "
        "Sanayi, tarım, enerji üretimi ve ulaşım gibi insan kaynaklı faaliyetler, çevreye zararlı kimyasallar ve atıklar salarak ekosistemlere zarar verir. "
        "Hava kirliliği solunum yolu hastalıklarına yol açarken, su kirliliği deniz yaşamını tehdit eder ve içme suyu kaynaklarını kirletir. "
        "Toprak kirliliği ise tarım ürünlerinin kalitesini düşürür ve gıda güvenliğini tehlikeye atar. "
        "Çevre kirliliği, hem insan sağlığına hem de biyolojik çeşitliliğe ciddi zararlar veren küresel bir sorundur. "
        "Bu nedenle, sürdürülebilir bir gelecek için çevrenin korunması ve temiz tutulması büyük önem taşır."
        )
    
    await ctx.send(bilgi_metni)

@bot.command()
async def çevre_bilgi(ctx):
    rastgele = random.choice(os.listdir("resimler"))
    with open(f'resimler/{rastgele}', 'rb') as f:
        resim = discord.File(f)
    await ctx.send(file=resim)
@bot.command()
async def çevrekirliligibilgi(ctx):
    await ctx.send("Çevre kirliliği hakkında bilgi almak istiyor musunuz? (evet/hayır)")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["evet", "hayır"]

    try:
        # Kullanıcıdan yanıt bekler (zaman aşımı 30 saniye)
        msg = await bot.wait_for("message", timeout=30.0, check=check)
        
        if msg.content.lower() == "evet":
            # Kullanıcı "evet" dediyse, bilgi metnini gönder
            bilgi_metni = (
                "Unilever\n"
                "Nestlé\n"
                "Procter & Gamble\n"
                "Mondelēz International\n"
                "Philip Morris International\n"
                "Danone\n"
                "Mars Inc\n"
                "Colgate-Palmolive\n"
            )
            await ctx.send(bilgi_metni)
        else:
            # Kullanıcı "hayır" dediyse, hiçbir şey yapma
            await ctx.send("Tamam, bilgi vermiyorum.")
    
    except discord.TimeoutError:
        # Kullanıcı zamanında yanıt vermezse
        await ctx.send("Zaman aşımına uğradı. Lütfen tekrar deneyin.")


bot.run('------')
