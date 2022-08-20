# minimal pubsub library
# 2022 Edwin Martin

class PubSub:
    _subscribers = dict()
    
    def subscribe(self, topic, subscriber):
        if not topic in self._subscribers:
            self._subscribers[topic] = set()

        self._subscribers[topic].add(subscriber)
        
        def _unsubscribe():
            self._subscribers[topic].discard(subscriber)
        
        return _unsubscribe
            
        
    def publish(self, topic, arg):
        if topic in self._subscribers:
            for subscriber in self._subscribers[topic]:
                subscriber(arg)

        if topic != '*':
            self.publish('*', (topic, arg))
