import logging
from threading import Thread
from random import randint
from time import sleep
from pq.queue import Queue
from pq.job import Job
from pq.worker import Worker
from task import JobRequestSiteArticle


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    site_list = ["https://revistaquem.globo.com/QUEM-News/noticia/2020/12/nasce-raika-filha-de-alok-e-romana-novais.html",
                "https://gq.globo.com/Men-of-the-Year/noticia/2020/12/pabllo-vittar-leva-o-men-year-2020.html"]
    jobs = [JobRequestSiteArticle(url=url, path="./artigos/") for url in site_list]
    queue = Queue("teste", [])

    queue.enqueue_jobs(jobs)
    
    worker = Worker("test", "teste")
    worker2 = Worker("test1", "teste")


    for worker in [worker, worker2]:
        thread = Thread(target=worker.run)
        thread.start()
    

