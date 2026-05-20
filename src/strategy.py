from abc import ABC, abstractmethod


# ==========================================
# STRATEGY PATTERN
# ==========================================

class SendStrategy(ABC):
    """Soyut gönderim stratejisi."""
    @abstractmethod
    def execute(self, recipient: str, message: str) -> None:
        pass


class ImmediateSendStrategy(SendStrategy):
    """Anlık gönderim stratejisi."""
    def execute(self, recipient: str, message: str) -> None:
        print(f"[Anlık Gönderim] {recipient} → {message}")


class BatchSendStrategy(SendStrategy):
    """Toplu gönderim stratejisi — mesajları biriktirir."""
    def __init__(self):
        self._queue: list[tuple] = []

    def execute(self, recipient: str, message: str) -> None:
        self._queue.append((recipient, message))
        print(f"[Toplu Gönderim] Kuyruğa eklendi ({len(self._queue)} mesaj bekliyor)")

    def flush(self) -> None:
        """Kuyruktaki tüm mesajları gönderir."""
        print(f"[Toplu Gönderim] {len(self._queue)} mesaj gönderiliyor...")
        for recipient, message in self._queue:
            print(f"  → {recipient}: {message}")
        self._queue.clear()


class NotificationContext:
    """Stratejiyi kullanan context sınıfı."""
    def __init__(self, strategy: SendStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SendStrategy) -> None:
        self._strategy = strategy

    def send(self, recipient: str, message: str) -> None:
        self._strategy.execute(recipient, message)