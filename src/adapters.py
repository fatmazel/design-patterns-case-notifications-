from src.base import Notification


class LegacySmsLibrary:
    """Üçüncü taraf kütüphane — metod isimleri sistemimize uymuyor."""
    def push_msg(self, text: str, phone: str) -> None:
        print(f"[Legacy SMS] {phone} → {text}")


class SmsAdapter(Notification):
    """
    Adapter: LegacySmsLibrary'nin push_msg(text, phone) metodunu
    bizim send(recipient, message) arayüzümüze bağlar.
    """
    def __init__(self):
        self._legacy = LegacySmsLibrary()

    def send(self, recipient, message):
        self._legacy.push_msg(message, recipient)