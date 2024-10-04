import queue
import threading
import time

import engine.ai_req as ai_req


class ApplicationQueue:
    def __init__(self):
        self.q = queue.Queue()

    def add_application_task(self, app):
        self.q.put(app)

    def get_application_task(self):
        return self.q.get()

    def task_done(self):
        self.q.task_done()

    def wait_until_done(self):
        self.q.join()


class Task:
    def __init__(self, task_id: int, prompt: str, app):
        self.task_id = task_id
        self.prompt = prompt
        self.app = app


class Worker(threading.Thread):
    def __init__(self, task_queue: ApplicationQueue, worker_id: int):
        super().__init__()
        self.task_queue = task_queue
        self.worker_id = worker_id
        self._stop_event = threading.Event()
        self.daemon = True
        

    def run(self):
        print(f"Worker {self.worker_id} started")

        while not self._stop_event.is_set():
            try:
                # retrieve a task from the queue
                task = self.task_queue.get_application_task()
                print(f"Worker {self.worker_id} got task: {task.task_id}")
                if task is None:
                    self.task_queue.task_done()
                    break
                try:
                    print(f"Worker {self.worker_id} processing task: {task.task_id}")
                    time.sleep(2)
                finally:
                    print(f"Worker {self.worker_id} finished task: {task}")
                    self.task_queue.task_done()
            except queue.Empty:
                continue

    def stop(self):
        print(f"Stopping worker {self.worker_id}")
        self._stop_event.set()


def create_worker_threads(worker_count: int, task_q: queue.Queue) -> list:
    workers = []
    for i in range(worker_count):
        worker = Worker(task_q, i)
        worker.start()
        workers.append(worker)
    
    return workers

def wait_until_workers_complete(workers: list[Worker]) -> None:
    for worker in workers:
        worker.join()


def stop_all_workers(workers: list[Worker]) -> None:
    for worker in workers:
        worker.stop()