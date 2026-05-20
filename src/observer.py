from abc import ABC, abstractmethod


# ==========================================
# OBSERVER PATTERN
# ==========================================

class NotificationObserver(ABC):
    """Soyut gözlemci arayüzü."""
    @abstractmethod
    def update(self, event: str, recipient: str, message: str) -> None:
        pass


class EmailObserver(NotificationObserver):
    """E-posta gönderimlerini izler."""
    def update(self, event: str, recipient: str, message: str) -> None:
        print(f"[EmailObserver] Olay: {event} | Alıcı: {recipient}")


class SMSObserver(NotificationObserver):
    """SMS gönderimlerini izler."""
    def update(self, event: str, recipient: str, message: str) -> None:
        print(f"[SMSObserver] Olay: {event} | Alıcı: {recipient}")


class NotificationEventManager:
    """Gözlemcileri yöneten yayıncı sınıf."""

    def __init__(self):
        self._observers: list[NotificationObserver] = []

    def subscribe(self, observer: NotificationObserver) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: NotificationObserver) -> None:
        self._observers.remove(observer)

    def notify(self, event: str, recipient: str, message: str) -> None:
        for observer in self._observers:
            observer.update(event, recipient, message)