import subprocess

# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'Njk0NTg5MDA2NzAwMjE2NDMw.XoWzIQ.k5zoSkT88IPfaaYKKT1wt0qgjjk'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

async def job(message):
    await message.channel.send('そろそろ寝ましょう！')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    if message.content == '/konn':
        await message.channel.send("こん")
    if message.author.id == 233481669858951178 or message.author.id == 538709181994369038 or message.author.id == 322325682883526656:
        messStr = str(message.content)
        messList = messStr.split(" ")
        messListLen = len(messList)
        print(type(messListLen))
        start = None
        for i in range(messListLen):
            if '"' in messList[i]:
                start = i
            elif start != None:
                messList[start] = messList[start] + messList[i]
                if '"' in messList[i]:
                    start = null
        print(messList)
        if messList[0] == "filew":
            path = str(messList[1])
            mess = str(messList[2])
            with open(path, mode='w') as f:
                f.write(mess)
        res = subprocess.check_output(messList)
        res = res.decode("utf-8")
        await message.channel.send(res)
    else:
        await message.channel.send("権限がありません")

client.run(TOKEN)
