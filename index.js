const mineflayer = require('mineflayer');

const botArgs = {
  host: 'game2.falixserver.net',
  port: '24452',
  username: "xbot30060"
};

const initBot = () => {

  // Setup bot connection
  let bot = mineflayer.createBot(botArgs);

  bot.on('login', () => {
    let botSocket = bot._client.socket;
    console.log(`Logged in to ${botSocket.server ? botSocket.server : botSocket._host}`);
  });

  bot.on('end', (reason) => {
    console.log(`Disconnected: ${reason}`);

    // Attempt to reconnect
    setTimeout(initBot, 5000);
  });

  bot.on('error', (err) => {
    if (err.code === 'ECONNREFUSED') {
      console.log(`Failed to connect to ${err.address}:${err.port}`)
    }
    else {
      console.log(`Unhandled error: ${err}`);
    }
  });
};

initBot();