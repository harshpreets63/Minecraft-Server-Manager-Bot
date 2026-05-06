from subprocess import Popen, PIPE
import signal
from bot import SERVER_PATH
from time import sleep
import os

import threading



class ServerProcess:
    
    def __init__(self):
        self.process = None
        self.server_path = SERVER_PATH
        
        
        
    def start_server(self):
        if self.process is None:
            self.process = Popen(["java", "-Xms4G", "-Xmx16G", "-jar", "server.jar", "nogui"], stdin=PIPE,  stdout=PIPE, text= True, cwd= self.server_path)
            threading.Thread(target=self.save_logs).start()
            
            
    def stop_server(self):
        if self.process is not None:
            print("Stopping Server")
            self.process.stdin.write("stop\n")
            self.process.stdin.flush()
            self.process.wait()
            self.process = None
    
    def save_logs(self):
        print("Logging Started")
        with open("server.log", "a") as file:
            for line in self.process.stdout:
                if"Done" in line:
                    print("Server Started")
                file.write(line)
                file.flush()
                    
            
        
    
# serv_init = ServerProcess()
# start = serv_init.start_server()
# 
# sleep(10)
# stop = serv_init.stop_server()