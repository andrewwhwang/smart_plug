var mqtt = require('mqtt')
var GPIO = require('onoff').Gpio;

var outlets = new Array();
outlets.push(new GPIO(4, 'out'));
outlets.push(new GPIO(17, 'out'));

var options = {
  port: 1883,
  username: 'username',
  password: 'password',
};

var client = mqtt.connect('mqtt://IP ADDRESS HERE', options);

client.on('connect', function() {
  console.log('connected')
  client.subscribe('switch/+', function() {
    client.on('message', function(topic, message, packet) {
      outlets[Number(topic.split('/')[1])].writeSync(Number(message));
    });
  });
});
