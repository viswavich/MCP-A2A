import queue
import threading
import time

# Message Queue (simulates MCP queue)
message_queue = queue.Queue()

# Producer Thread
def producer():
    for i in range(8):
        msg = f"Message {i}"
        print(f"[Producer] Sending: {msg}")
        message_queue.put(msg)
        time.sleep(1)

# Consumer Thread
def consumer():
    while True:
        msg = message_queue.get()
        if msg == "END":
            break
        print(f"[Consumer] Received: {msg}")

# Run threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
message_queue.put("END")
consumer_thread.join()