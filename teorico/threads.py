import threading
import time
import random

class Filosofos(threading.Thread):

    def __init__(self, name, leftFork, rightFork):
        print(f'{name}, sentou na mesa')
        threading.Thread.__init__(self, name=name)
        self.leftFork = leftFork
        self.rightFork = rightFork

    def run (self):
        print(f'{threading.current_thread().getName()}, começou a pensar!')
        while True:
            time.sleep(random.randint(1, 5))
            print(f'{}, parou de pensar!')