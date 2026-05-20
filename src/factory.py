from src.base import Notification


class NotificationFactory:
    _registry = {}

    @classmethod
    def register_notification(cls, type_name, notification_class):
        cls._registry[type_name] = notification_class

    @classmethod
    def create_notification(cls, type_name):
        notifier_class = cls._registry.get(type_name)
        if not notifier_class:
            raise ValueError(f"Bilinmeyen bildirim tipi: {type_name}")
        return notifier_class()

    @classmethod
    def clear_registry(cls):  # sadece test ortamı için
        cls._registry.clear()