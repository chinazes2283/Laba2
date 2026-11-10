from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, total_amount: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def calculate_discount(self, total_amount: float) -> float:
        return 0.0


class SeasonalDiscount(DiscountStrategy):
    def calculate_discount(self, total_amount: float) -> float:
        return total_amount * 0.15


class VIPDiscount(DiscountStrategy):
    def calculate_discount(self, total_amount: float) -> float:
        return total_amount * 0.30


class HolidayDiscount(DiscountStrategy):
    def calculate_discount(self, total_amount: float) -> float:
        return total_amount * 0.20


class Order:
    def __init__(self, items_cost: float, discount_strategy: DiscountStrategy):
        self._items_cost = items_cost
        self._discount_strategy = discount_strategy

    def set_discount_strategy(self, strategy: DiscountStrategy) -> None:
        self._discount_strategy = strategy

    def get_final_amount(self) -> float:
        discount = self._discount_strategy.calculate_discount(self._items_cost)
        return self._items_cost - discount


order = Order(2000.0, NoDiscount())
print(f"Сума без знижки: {order.get_final_amount()} грн")

order.set_discount_strategy(SeasonalDiscount())
print(f"Сума з сезонною знижкою (15%): {order.get_final_amount()} грн")

order.set_discount_strategy(VIPDiscount())
print(f"Сума для VIP-клієнта (30%): {order.get_final_amount()} грн")

order.set_discount_strategy(HolidayDick := HolidayDiscount())
print(f"Сума зі святковою знижкою (20%): {order.get_final_amount()} грн")
