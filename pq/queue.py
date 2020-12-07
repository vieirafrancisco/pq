from threading import Lock

class Pilha:
    def __init__(self, jobs):
        jobs = jobs or []
        self.array = jobs
        self.pos = len(self.array)
        self.lock = Lock()

    def pop(self):
        with self.lock:
            if self.pos == 0:
                raise Exception("pilha vazia")

            obj = self.array[-1]
            self.array = self.array[:-1]
            self.pos-=1

        return obj

    def append(self, obj):
        with self.lock:
            self.array.append(obj)
            self.pos+=1

    def __len__(self):
        return self.pos
    
class Queue:
    queue_dict = {}
    def __init__(self, name, jobs=None):

        jobs = jobs or []
        self.name = name
        self.jobs = Pilha(jobs)

    def enqueue(self, job):
        self.jobs.push(job)

    def enqueue_jobs(self, jobs_generator):
        for job in jobs_generator:
            self.jobs.append(job)
    
    def __iter__(self):
        return self

    def __next__(self):
        if len(self.jobs) == 0:
            raise StopIteration
        
        return self.jobs.pop()

    def __new__(cls, name, *args, **kwargs):
        instance = object.__new__(Queue)
        cls.queue_dict[name] = instance

        return instance
    
    @classmethod
    def get_instance(cls, name):
        if name in cls.queue_dict:
            return cls.queue_dict[name]
        else:
            return Queue(name)
