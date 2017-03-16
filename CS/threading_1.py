import threading
import time


exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print ("starting {}".format(self.name))
        print_time(self.name, self.counter, 5)
        print ("Exiting {}".format(self.name))

def print_time(threadname, delay, counter):
    while (counter):
        if exitFlag:
            threadname.exit()
        time.sleep(delay)
        print ("%s : %s " %(threadname, time.ctime(time.time())))
        counter -=1

thread1 = myThread(1, "threadId-1",1)
thread2 = myThread(1, "threadId-2",2)

thread1.start()
thread2.start()

print ("Exiting main thread")