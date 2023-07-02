from abc import ABC, abstractmethod


class Adder:

    def work(self, x, y):
        return x + y


class Multiplier:

    def work(self, x, y):
        return x * y


class Calculator:

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, x, y):
        print(self.strategy.work(x, y))


calc = Calculator()
calc.set_strategy(Adder())
calc.calculate(10, 20)
calc.set_strategy(Multiplier())
calc.calculate(10, 20)


# But better write:


class BaseStrategy(ABC):
    @abstractmethod
    def work(self, x, y):
        pass


class Adder(BaseStrategy):

    def work(self, x, y):
        return x + y


class Multiplier(BaseStrategy):

    def work(self, x, y):
        return x * y


class Calculator:

    def set_strategy(self, strategy: BaseStrategy):
        self.strategy = strategy

    def calculate(self, x, y):
        print('Res: ', self.strategy.work(x, y))


calc = Calculator()
calc.set_strategy(Adder())
calc.calculate(10, 20)
calc.set_strategy(Multiplier())
calc.calculate(10, 20)
