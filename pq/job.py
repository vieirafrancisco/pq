class Job:
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.callback(*self.args, **self.kwargs)
     
    def __str__(self):
        return f"job:{self.__class__.__name__}, args: {self.args}, kwargs: {self.kwargs}"
