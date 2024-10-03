import queue
import threading
import time


# queues

class ApplicationQueue:
    def __init__(self):
        self.q = queue.Queue()


    def add_application_task(self, app):
        self.q.put(app)


    def get_application_task(self):
        if not self.q.empty():
            return self.q.get()
        else:
            return None

        
    def task_done(self):
        self.q.task_done()


    def wait_until_done(self):
        self.q.join()



class Worker(threading.Thread):
    def __init__(self, task_queue: ApplicationQueue, worker_id: int):
        super().__init__()
        self.task_queue = task_queue
        self.worker_id = worker_id
        self._stop_event = threading.Event()

    def run(self):
        print(f"Worker {self.worker_id} started")
        while not self._stop_event.is_set():
            try:
                # retrieve a task from the queue
                task = self.task_queue.get_application_task()
                print(f"Worker {self.worker_id} processing task: {task}")
                time.sleep(2)
                self.task_queue.task_done()
            except queue.Empty:
                continue

    def stop(self):
        self._stop_event.set()


def create_worker_threads(count: int, q: queue.Queue) -> list:
    workers = []
    for i in range(count):
        worker = Worker(q, i)
        worker.start()
        workers.append(worker)
    
    return workers

def wait_until_workers_complete(workers: list[Worker]) -> None:
    for worker in workers:
        worker.join()


def stop_all_workers(workers: list[Worker]):
    for worker in workers:
        worker.stop()