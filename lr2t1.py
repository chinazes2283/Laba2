from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    @property
    def name(self) -> str:
        return self._name

    @property
    def base_salary(self) -> float:
        return self._base_salary

    @abstractmethod
    def calculate_monthly_pay(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Працівник: {self._name}, Базовий оклад: {self._base_salary} грн"


class Developer(Employee):
    def __init__(self, name: str, base_salary: float, programming_language: str, tasks_completed: int):
        super().__init__(name, base_salary)
        self._programming_language = programming_language
        self._tasks_completed = tasks_completed

    def calculate_monthly_pay(self) -> float:
        bonus = self._tasks_completed * 500
        return self._base_salary + bonus

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, Мова: {self._programming_language}, Виконано завдань: {self._tasks_completed}"


class Manager(Employee):
    def __init__(self, name: str, base_salary: float, team_size: int, bonus_coefficient: float):
        super().__init__(name, base_salary)
        self._team_size = team_size
        self._bonus_coefficient = bonus_coefficient

    def calculate_monthly_pay(self) -> float:
        return self._base_salary + (self._team_size * 1000 * self._bonus_coefficient)

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, Розмір команди: {self._team_size}, Коефіцієнт: {self._bonus_coefficient}"


class Designer(Employee):
    def __init__(self, name: str, base_salary: float, design_tool: str, projects_count: int):
        super().__init__(name, base_salary)
        self._design_tool = design_tool
        self._projects_count = projects_count

    def calculate_monthly_pay(self) -> float:
        return self._base_salary + (self._projects_count * 1200)

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, Інструмент: {self._design_tool}, Проєктів: {self._projects_count}"


staff_members = [
    Developer("Олександр", 25000.0, "Python", 10),
    Manager("Марія", 30000.0, 5, 1.5),
    Designer("Андрій", 22000.0, "Figma", 4)
]

for employee in staff_members:
    print(employee)
    print(f"Зарплата до виплати: {employee.calculate_monthly_pay()} грн\n")

print(f"Чи є staff_members[0] екземпляром Developer: {isinstance(staff_members[0], Developer)}")
print(f"Чи є staff_members[0] екземпляром Employee: {isinstance(staff_members[0], Employee)}")
print(f"Чи є підкласом Designer клас Employee: {issubclass(Designer, Employee)}")
