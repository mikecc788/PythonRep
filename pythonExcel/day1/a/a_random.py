import random
import threading

a = [0,1,2,3,4,5]
def thread_job():
    print('this is add thread')

b=random.shuffle(a)
def thread():

    added_thread = threading.Thread(target=thread_job())
    added_thread.start()
    print(threading.active_count())
    print(threading.enumerate())
print(b)
if __name__ == '__main__':
   thread()