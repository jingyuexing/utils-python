class EventEmitter:
    def __init__(self):
        self.events = {}

    def on(self, event_name:str):
        def decorator(callback):
            if event_name not in self.events:
                self.events[event_name] = []
            self.events[event_name].append(callback)
            return callback
        return decorator

    def emit(self, event_name, *args, **kwargs):
        if event_name in self.events:
            for callback in self.events[event_name]:
                callback(*args, **kwargs)

    def off(self, event_name, callback):
        if event_name in self.events:
            self.events[event_name] = [cb for cb in self.events[event_name] if cb != callback]
