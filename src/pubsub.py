# minimal pubsub library with uasyncio support
# 2022 Edwin Martin
import uasyncio as asyncio


class PubSub:
    _subscribers = dict()

    def subscribe(self, topic, subscriber):
        if not topic in self._subscribers:
            self._subscribers[topic] = []

        self._subscribers[topic].append(subscriber)

        def _unsubscribe():
            self._subscribers[topic].remove(subscriber)

        return _unsubscribe

    def publish(self, topic, arg):
        if topic in self._subscribers:
            for subscriber in self._subscribers[topic]:
                subscriber(arg)

        if topic != '*':
            self.publish('*', (topic, arg))

    async def wait(self, topic):
        event = asyncio.Event()
        data = {}

        def resolve(dataIn):
            data['data'] = dataIn
            event.set()
            unsubscribe()

        unsubscribe = self.subscribe(topic, resolve)

        await event.wait()
        event.clear()

        return data['data']
