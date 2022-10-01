from ask import Ask


class ListenCommand:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def filter(self):
        models = [
            'window',
            'door'
        ]

    def listen_command(self):
        try:
            if 'open' in self.kwargs.items():
                active_status = Ask({self.kwargs.get('open'): self.kwargs.get('open')})
                return active_status
        except Exception as e:
            print(e)