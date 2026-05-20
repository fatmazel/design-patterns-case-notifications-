from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass