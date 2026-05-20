from src.concrete import EmailNotification, SMSNotification, PushNotification
from src.adapters import SmsAdapter
from src.factory import NotificationFactory
from src.facade import NotificationServiceFacade


# Kayıtlar
NotificationFactory.register_notification("email", EmailNotification)
NotificationFactory.register_notification("sms", SMSNotification)
NotificationFactory.register_notification("push", PushNotification)
NotificationFactory.register_notification("legacy_sms", SmsAdapter)


if __name__ == "__main__":
    facade = NotificationServiceFacade()

    print("=== E-posta (şifreli + loglu) ===")
    facade.send_secure_notification("email", "fatmazehra@example.com", "Merhaba Faz 2!")

    print("=== Normal SMS (şifreli + loglu) ===")
    facade.send_secure_notification("sms", "+90555...", "Bu bir test mesajıdır.")

    print("=== Legacy SMS — Adapter ile ===")
    facade.send_secure_notification("legacy_sms", "+90532...", "Adaptör testi.")