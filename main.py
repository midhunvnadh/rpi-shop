from wheels import wheels
from rfid import rfid

import threading

if __name__ == '__main__':
    thread_a = threading.Thread(target=wheels)
    thread_b = threading.Thread(target=rfid)

    # Start threads
    thread_a.start()
    thread_b.start()

    # Wait for threads to finish
    thread_a.join()
    thread_b.join()

    print("Threads finished.")
