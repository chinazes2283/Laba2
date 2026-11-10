class BankAccount:
    def __init__(self, account_holder: str, balance: float, credit_limit: float):
        self._account_holder = account_holder
        self.__balance = balance
        self._credit_limit = credit_limit

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Баланс повинен бути числовим значенням")
        if value < 0:
            raise ValueError("Баланс не може бути від'ємним")
        self.__balance = float(value)

    @property
    def total_available(self) -> float:
        return self.__balance + self._credit_limit

    @property
    def account_holder(self) -> str:
        return self._account_holder


acc = BankAccount("Олександр", 1500.0, 500.0)

print(точки_доступу := f"Власник: {acc.account_holder}, Баланс: {acc.balance}")
print(f"Загальні доступні кошти (обчислювана властивість): {acc.total_available}")

acc.balance = 3000.0
print(f"Оновлений баланс: {acc.balance}")
print(f"Оновлені загальні доступні кошти: {acc.total_available}")

try:
    acc.balance = -200.0
except ValueError as e:
    print(f"Перехоплено виняток ValueError: {e}")

try:
    acc.balance = "багато"
except TypeError as e:
    print(f"Перехоплено виняток TypeError: {e}")

try:
    print(acc.__balance)
except AttributeError as e:
    print(f"Спроба прямого доступу до __balance викликала помилку: {e}")

print(f"Доступ через name mangling (_BankAccount__balance): {acc._BankAccount__balance}")
