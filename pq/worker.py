import logging
from pq.queue import Queue

logger = logging.getLogger(__name__)

class Worker:
    def __init__(self, name, queue_name):
        self.name = name
        self.queue = Queue.get_instance(queue_name)
    def run(self):
        logger.info(f" {self.name} is running")
        for job in self.queue:
            logger.debug(f" {self.name} start {job}")
            job.run()
            logger.debug(f" {self.name} finish {job}")
