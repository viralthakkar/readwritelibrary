import multiprocessing
import threading
import queue
import time


class JobScheduler:
    def __init__(self, num_processes, num_threads):
        self.num_processes = num_processes
        self.num_threads = num_threads
        self.process_pool = multiprocessing.Pool(processes=num_processes)
        self.thread_pool = []

    def add_job(self, target, args=()):
        self.process_pool.apply_async(self._execute_job, (target, args))

    def _execute_job(self, target, args):
        thread_pool = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=target, args=args)
            thread_pool.append(thread)
            print("Tes")
            thread.start()
        for thread in thread_pool:
            thread.join()

    def wait_completion(self):
        self.process_pool.close()
        self.process_pool.join()


def example_job(msg):
    for i in range(5):
        print(msg)
        time.sleep(1)


if __name__ == "__main__":
    num_processes = 2  # Number of processes
    num_threads = 3  # Number of threads per process
    scheduler = JobScheduler(num_processes, num_threads)

    # Add example jobs
    scheduler.add_job(example_job, ("Job 1",))
    scheduler.add_job(example_job, ("Job 2",))
    scheduler.add_job(example_job, ("Job 3",))

    # Wait for all jobs to complete
    scheduler.wait_completion()


