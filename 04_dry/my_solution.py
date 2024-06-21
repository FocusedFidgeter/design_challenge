# dry_code_wip.py
from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum
from typing import Iterable


class OrderType(StrEnum):
    ONLINE = "online"
    IN_STORE = "in store"


@dataclass
class Item:
    name: str
    price: Decimal


@dataclass
class Email:
    body: str
    subject: str
    recipient: str
    sender: str

    @staticmethod
    def generate_confirmation_email(order: "Order") -> "Email":
        return Email(
            body=f"Thank you for your order! Your order #{order.order_id} has been confirmed.",
            subject="Order Confirmation",
            recipient=order.customer_email,
            sender="sales@webshop.com",
        )

    @staticmethod
    def generate_shipping_notification(order: "Order") -> "Email":
        return Email(
            body=f"Good news! Your order #{order.order_id} has been shipped and is on its way.",
            subject="Order Shipped",
            recipient=order.customer_email,
            sender="sales@webshop.com",
        )


@dataclass
class Order:
    order_id: int
    order_type: OrderType
    customer_email: str

    def __init__(self, order_id: int, order_type: OrderType, customer_email: str):
        self.order_id = order_id
        self.order_type = order_type
        self.customer_email = customer_email

    def process(self) -> None:
        if self.order_type == OrderType.ONLINE:
            print("Processing online order...")
            print(Email.generate_confirmation_email(self))
            print("Shipping the order...")
            print(Email.generate_shipping_notification(self))
        elif self.order_type == OrderType.IN_STORE:
            print("Processing in-store order...")
            print(Email.generate_confirmation_email(self))
            print("Order ready for pickup.")
        else:
            raise ValueError("Invalid order type.")
        print("Order processed successfully.")


def calculate_price(items: Iterable[Item], discount: Decimal = Decimal("0")) -> Decimal:
    total_price = Decimal(sum(item.price for item in items))
    discounted_price = total_price - (total_price * discount)
    return discounted_price


def main() -> None:
    items = [
        Item(name="T-Shirt", price=Decimal("19.99")),
        Item(name="Jeans", price=Decimal("49.99")),
        Item(name="Shoes", price=Decimal("79.99")),
    ]

    online_order = Order(
        order_id=123, order_type=OrderType.ONLINE, customer_email="sarah@gmail.com"
    )

    total_price = calculate_price(items, Decimal("0.0"))
    print("Total price:", total_price)

    discounted_price = calculate_price(items, Decimal("0.1"))
    print("Discounted price:", discounted_price)

    online_order.process()

    in_store_order = Order(
        order_id=456, order_type=OrderType.IN_STORE, customer_email="john@gmail.com"
    )

    in_store_order.process()


if __name__ == "__main__":
    main()