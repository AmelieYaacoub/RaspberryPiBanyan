#!/usr/bin/env python3

import logging
import argparse
import traceback
import signal
import sys
import time
from python_banyan.banyan_base import BanyanBase

import RPi.GPIO as GPIO


BANYAN_IP="192.168.178.52"

class test(BanyanBase):
    """
    This class subscribes to all messages on the back plane and prints out both topic and payload.
    """

    def __init__(self, back_plane_ip_address=BANYAN_IP,
                 process_name=None, com_port="None", baud_rate=115200, log=False, quiet=False, loop_time="0.1"):
        """
        This is constructor for the Monitor class
        :param back_plane_ip_address: IP address of the currently running backplane
        :param subscriber_port: subscriber port number - matches that of backplane
        :param publisher_port: publisher port number - matches that of backplane
        """

        # initialize the base class
        super().__init__(back_plane_ip_address,  process_name=process_name, numpy=True)

        """"""

        # Loop sending messages to unitygateway to request a cube color change
        while True:
            C1 = 12
            B = 16
            A = 18
            G = 22
            F = 32
            E = 36
            D = 38
            C = 40
            GPIO.setmode(GPIO.BOARD)
            
            GPIO.setup(C1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
            GPIO.setup(B,GPIO.IN,pull_up_down=GPIO.PUD_UP)
            GPIO.setup(A,GPIO.IN,pull_up_down=GPIO.PUD_UP)
            GPIO.setup(G,GPIO.IN,pull_up_down=GPIO.PUD_UP)
            GPIO.setup(F,GPIO.IN,pull_up_down=GPIO.PUD_UP)
            GPIO.setup(E,GPIO.IN,pull_up_down=GPIO.PUD_UP)
            GPIO.setup(D,GPIO.IN,pull_up_down=GPIO.PUD_UP)
            GPIO.setup(C,GPIO.IN,pull_up_down=GPIO.PUD_UP)
            
           
            try:
                if (GPIO.input(C1)==0):
                    note=8
                  
                elif (GPIO.input(B)==0):
                    note=7
                    
                elif (GPIO.input(A)==0):
                    note=6
                elif (GPIO.input(A)==0):
                    note=5
                elif (GPIO.input(A)==0):
                    note=4
                elif (GPIO.input(A)==0):
                    note=3
                elif (GPIO.input(A)==0):
                    note=2
                elif (GPIO.input(A)==0):
                    note=1
                else:
                    note=-1
                    
                unity_message = {"action":"color", "info":"blue", "value": note, "target":"Cube"}    
                self.send_unity_message(unity_message)

                


            except KeyboardInterrupt:
                self.clean_up()

        """"""

    def send_unity_message(self, unity_message):
        """
        Logs the game activity. self.room_name must be set before calling this function

        :return:
        """
        # Set the topic so the unitygateway picks up the message.
        topic = "send_to_unity"

        # Send off the message!
        self.publish_payload(unity_message, topic)

    def clean_up(self):
        """
        Clean up before exiting - override if additional cleanup is necessary

        :return:
        """
        self.publisher.close()
        self.subscriber.close()
        self.context.term()
        sys.exit(0)

def unity_test():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", dest="back_plane_ip_address", default="None",
                         help="None or IP address used by Back Plane")
    parser.add_argument("-n", dest="process_name", default="Unity Sender",
                         help="Set process name in banner")
    parser.add_argument("-t", dest="loop_time", default=".1",
                         help="Event Loop Timer in seconds")

    args = parser.parse_args()
    kw_options = {}

    if args.back_plane_ip_address != "None":
        kw_options["back_plane_ip_address"] = args.back_plane_ip_address

    kw_options["process_name"] = args.process_name
    kw_options["loop_time"] = float(args.loop_time)

    my_test = test(**kw_options)

    # signal handler function called when Control-C occurs

    def signal_handler(sig, frame):
        print("Control-C detected. See you soon.")

        my_test.clean_up()
        sys.exit(0)

    # listen for SIGINT
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


if __name__ == "__main__":
    unity_test()
