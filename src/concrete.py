from src.base import Notification


class EmailNotification(Notification):
    def send(self, recipient, message):
        print(f"E-posta gönderiliyor: {recipient}")
        print(f"İçerik: {message}")
        print("E-posta başarıyla gönderildi.\n")


class SMSNotification(Notification):
    def send(self, recipient, message):
        if len(message) > 160:
            message = message[:157] + "..."
        print(f"SMS gönderiliyor: {recipient}")
        print(f"İçerik: {message}")
        print("SMS başarıyla gönderildi.\n")


class PushNotification(Notification):
    def send(self, recipient, message):
        print(f"Push bildirimi gönderiliyor: {recipient}")
        print(f"İçerik: {message}")
        print("Push bildirimi gönderildi.\n")