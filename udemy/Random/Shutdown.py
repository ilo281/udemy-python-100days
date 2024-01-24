import os

def shutdown():

    shutdown_str = 'shutdown /s /t 0'
    os.system(shutdown_str)


shutdown()
