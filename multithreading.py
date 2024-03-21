import heapq
import threading
import time
import sys


class Task:
    def __init__(self, func, args=(), kwargs={}):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __lt__(self, other):
        return False  # For heapq to treat tasks as equal priority


class TaskScheduler:
    def __init__(self, num_workers=2):
        self.tasks = []
        self.condition = threading.Condition()
        self.workers = [threading.Thread(target=self._worker_thread) for _ in range(num_workers)]
        self.scheduled_intervals = {}
        for worker in self.workers:
            worker.setDaemon(True)  # Set as daemon after creation
            worker.start()

    def schedule(self, task, execute_at):
        with self.condition:
            heapq.heappush(self.tasks, (execute_at, task))
            self.condition.notify()

    def schedule_at_fixed_interval(self, task, interval):
        def schedule_task():
            while True:
                next_execution_time = time.time() + interval
                self.schedule(task, next_execution_time)
                time.sleep(interval)

        interval_thread = threading.Thread(target=schedule_task)
        interval_thread.start()
        self.scheduled_intervals[task] = interval_thread

    def _worker_thread(self):
        while True:
            with self.condition:
                while not self.tasks:
                    self.condition.wait()
                else:
                    current_time = time.time()
                    next_execute_time, task = self.tasks[0]
                    if next_execute_time <= current_time:
                        heapq.heappop(self.tasks)
                        threading.Thread(target=self._execute_task, args=(task,)).start()
                    else:
                        self.condition.wait(next_execute_time - current_time)

    def _execute_task(self, task):
        task.func(*task.args, **task.kwargs)


# Example usage
def example_task():
    print("Task executed at:", time.ctime())


scheduler = TaskScheduler(num_workers=2)
scheduled_task = Task(example_task)
scheduler.schedule_at_fixed_interval(scheduled_task, 10)