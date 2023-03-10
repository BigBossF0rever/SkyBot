from javascript import require, On
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

RANGE_GOAL = 1
BOT_USERNAME = 'BigBotForever'

bot = mineflayer.createBot({
  'host': 'game2.falixserver.net',
  'port': 24452,
  'username': BOT_USERNAME
})

bot.loadPlugin(pathfinder.pathfinder)
print("Started mineflayer")

@On(bot, 'spawn')
def handle(*args):
  print("I spawned 👋")
  movements = pathfinder.Movements(bot)

  @On(bot, 'chat')
  def handleMsg(this, sender, message, *args):
    print("Got message", sender, message)
    if sender and (sender != BOT_USERNAME):
      #bot.chat('Hi, you said ' + message)
      if 'come' in message:
        player = bot.players[sender]
        print("Target", player)
        target = player.entity
        if not target:
          bot.chat("I don't see you !")
          return

        pos = target.position
        bot.pathfinder.setMovements(movements)
        bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, RANGE_GOAL))
      
      if "BigBossForever" in message:
        bot.chat("BigBossForever est actuellement afk")

    if message.startswith("!help"):
      bot.chat("Available commands: help")


@On(bot, "end")
def handle(*args):
  print("Bot ended!", args)


# Errors
@On(bot, 'kicked')
def handle(_, reason):
  print('kicked', reason)
  
  bot = mineflayer.createBot({
    'host': 'game2.falixserver.net',
    'port': 24452,
    'username': BOT_USERNAME
  })

  bot.loadPlugin(pathfinder.pathfinder)
  print("Started mineflayer")

@On(bot, 'error')
def handle(_, reason):
  print('error', reason)