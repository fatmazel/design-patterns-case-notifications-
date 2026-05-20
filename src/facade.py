from src.factory import NotificationFactory
from src.decorators import EncryptionDecorator, LoggingDecorator
from src.base import Notification


class NotificationServiceFacade:
    """Karmaşıklığı gizler: factory → encrypt → log → send."""

    def send_secure_notification(self, type_name, recipient, message):
        notifier: Notification = NotificationFactory.create_notification(type_name)
        encrypted = EncryptionDecorator(notifier)
        logged = LoggingDecorator(encrypted)
        logged.send(recipient, message)