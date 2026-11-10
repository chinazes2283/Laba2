from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"[LOG]: {message}")


class NotificationService(ABC):
    def __init__(self, logger: Logger):
        self._logger = logger

    @property
    @abstractmethod
    def channel_name(self) -> str:
        pass

    @abstractmethod
    def send_notification(self, recipient: str, text: str) -> bool:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

    def generate_report(self, recipient: str, text: str) -> str:
        self._logger.log(f"Генерація звіту для каналу: {self.channel_name}")
        return f"Канал: {self.channel_name} | Одержувач: {recipient} | Текст: {text}"


class EmailService(NotificationService):
    def __init__(self, logger: Logger, smtp_server: str):
        super().__init__(logger)
        self._smtp_server = smtp_server

    @property
    def channel_name(self) -> str:
        return "Email"

    def send_notification(self, recipient: str, text: str) -> bool:
        self._logger.log(f"Надсилання Email на {recipient} через сервер {self._smtp_server}")
        return True

    def get_cost(self) -> float:
        return 0.05


class SMSService(NotificationService):
    def __init__(self, logger: Logger, gateway_number: str):
        super().__init__(logger)
        self._gateway_number = gateway_number

    @property
    def channel_name(self) -> str:
        return "SMS"

    def send_notification(self, recipient: str, text: str) -> bool:
        self._logger.log(f"Надсилання SMS на номер {recipient} через шлюз {self._gateway_number}")
        return True

    def get_cost(self) -> float:
        return 0.50


try:
    invalid_service = NotificationService(ConsoleLogger())
except TypeError as e:
    print(f"Перехоплено TypeError при спробі створення екземпляра абстрактного класу: {e}")

logger = ConsoleLogger()
services = [
    EmailService(logger, "smtp.ukr.net"),
    SMSService(logger, "+380670000000")
]

for service in services:
    print(f"Канал: {service.channel_name}")
    print(f"Звіт: {service.generate_report('test@example.com', 'Вітаємо!')}")
    service.send_notification("0991234567", "Ваш код підтвердження: 1234")
    print(f"Вартість відправки: {service.get_cost()} USD\n")
