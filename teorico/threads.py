import threading
import time
import random

def contador_1 ():
    x = 1000000000
    while x > 0:
        x -= 1

def sequencial():
    tempo = time.time()
    contador_1()
    contador_1()
    tempo_f = time.time()
    print(f'tempo sequencial: {tempo_f - tempo}')

def concorente():
    tempo_i = time.time()
    t1 = threading.Thread(target=contador_1())
    t2 = threading.Thread(target=contador_1())
    time.sleep(random.randint(1, 20))
    t1.start()
    time.sleep(random.randint(1, 20))
    t2.start()
    t1.join()
    t2.join()
    tempo_f1 = time.time()
    print(f'tempo concorente: {tempo_f1 - tempo_i}')


sequencial()
concorente()