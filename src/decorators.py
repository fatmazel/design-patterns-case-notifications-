from src.base import Notification


class NotificationDecorator(Notification):
    def __init__(self, wrapped: Notification):
        self._wrapped = wrapped

    def send(self, recipient, message):
        self._wrapped.send(recipient, message)


class EncryptionDecorator(NotificationDecorator):
    def send(self, recipient, message):
        encrypted = message[::-1]
        print(f"[SİSTEM] Mesaj şifrelendi.")
        super().send(recipient, f"ENC({encrypted})")


class LoggingDecorator(NotificationDecorator):
    def send(self, recipient, message):
        super().send(recipient, message)
        print(f"[LOG] '{recipient}' adresine bildirim gönderildi.")