from abc import ABC, abstractmethod

# Strategy
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid Rs.{amount} using Credit Card")


# Concrete Strategy 2
class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid Rs.{amount} using PayPal")


# Concrete Strategy 3
class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid Rs.{amount} using UPI")


# Concrete Strategy 4
class NetBankingPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid Rs.{amount} using Net Banking")


# Context
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main program
processor = PaymentProcessor(UPIPayment())
processor.process_payment(1500)

processor.set_strategy(CreditCardPayment())
processor.process_payment(2500)

processor.set_strategy(PayPalPayment())
processor.process_payment(1000)

processor.set_strategy(NetBankingPayment())
processor.process_payment(2000)