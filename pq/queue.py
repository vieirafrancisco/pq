class Queue:
    queue_dict = {}
    def __init__(self, name, jobs=[]):
        self.name = name
        self.jobs = jobs

    def enqueue(self, job):
        self.jobs.append(job)

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
        if name in cls.queue_dict:
            instance = cls.queue_dict[name]
        else:
            instance = super().__new__(Queue)
            cls.queue_dict[name] = instance

        return instance
