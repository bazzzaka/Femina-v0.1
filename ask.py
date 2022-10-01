

class Ask:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def ask_process(self):
        print('Ask -*RUNNING*-')
        print(f'args is \n {self.args}\nkwargs is \n {self.kwargs}')

    def start(self):
        try:
            self.ask_process()
        except Exception as e:
            print(e)
