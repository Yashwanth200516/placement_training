from collections import deque
printer_queue = deque()
for i in range(1, 6):
    printer_queue.append(f"Job_{i}")
    print(f"Added: Job_{i}")
print("--- Processing Jobs ---")
while printer_queue:
    current_job = printer_queue.popleft()
    print(f"Printing: {current_job}")