"""EE 250L Lab 04 PART 2"""

import paho.mqtt.client as mqtt
import socket
def call_back_pong(client, userdata, message):
   num = int(message.payload.decode()) + 1;
   print("Pong: " + num) 
   time.sleep(4)
   client.publish("gtrue/ping", f"{num}")
   print("Pinging Num!")

def on_connect(client, userdata, flags, rc):
    # Subscribe to servers
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("gtrue/pong")
    
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("gtrue/pong", call_back_pong)

if __name__ == '__main__':
    #create a client object
    client = mqtt.Client()

    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
          
    client.connect(host="172.20.10.5", port=1883, keepalive=60)
    
    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.publish("gtrue/ping", f"{num}")
    print("Pinging Num!")
    client.loop_forever()
    time.sleep(1)
        
          

          
