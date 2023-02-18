"""EE 250L Lab 04 PART 2"""

import paho.mqtt.client as mqtt
import socket
def call_back_pong(client, userdata, message):
   num = int(message.payload.decode()) + 1;
   print("Pong: " + num) 
   time.sleep(4)
   client.publish("cmbaker/ping", f"{num}")
   print("Pinging Num!")

def on_connect(client, userdata, flags, rc):
    # Subscribe to servers
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("cmbaker/pong")
    num = 0
    
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("cmbaker/pong", call_back_pong)

if __name__ == '__main__':
    #create a client object
    client = mqtt.Client()

    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
          
    client.connect(host="68.181.32.115", port=11000, keepalive=60)
    
    client.loop_start()
    num = 0
    
    client.publish("cmbaker/ping", f"{num}")
    print("Pinging Num!")
    
    while True:
      pass
        
          

          
