"""
    State
     - Lets an object alter its behavior when its internal state changes. It
     appears as if the object changed its class.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """Context"""

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        self.state.pending()

    def approve(self) -> None:
        self.state.approve()

    def reject(self) -> None:
        self.state.reject()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Payment already pending!')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Payment approved!')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Payment rejected!')


class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Payment pending!')

    def approve(self) -> None:
        print('Payment already approved!')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Payment rejected!')


class PaymentRejected(OrderState):
    def pending(self) -> None:
        print('Payment unrejectable!')

    def approve(self) -> None:
        print('Payment unrejectable!')

    def reject(self) -> None:
        print('Payment unrejectable!')


if __name__ == '__main__':
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
