from dataclasses import dataclass, field
from decimal import Decimal
from abc import ABC, abstractmethod
from typing import List, Optional


class ItemNotFoundException(Exception):
    pass


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity


@dataclass
class ShoppingCart:
    items: List[Item] = field(default_factory=list)
    discount_strategy: Optional['DiscountStrategy'] = None

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        found_item = self.find_item(item_name)
        self.items.remove(found_item)

    def find_item(self, item_name: str) -> Item:
        for item in self.items:
            if item.name == item_name:
                return item
        raise ItemNotFoundException(f"Item '{item_name}' not found.")

    @property
    def subtotal(self) -> Decimal:
        return Decimal(sum(item.subtotal for item in self.items))

    @property
    def discount(self) -> Decimal:
        if self.discount_strategy:
            return self.discount_strategy.calculate_discount(self.subtotal)
        return Decimal("0")

    @property
    def total(self) -> Decimal:
        return self.subtotal - self.discount

    def display(self) -> None:
        # Print the cart
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self.items:
            print(
                f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}"
            )
        print("=" * 40)
        print(f"Subtotal: ${self.subtotal:>7.2f}")
        print(f"Discount: ${self.discount:>7.2f}")
        print(f"Total:    ${self.total:>7.2f}")


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, subtotal: Decimal) -> Decimal:
        pass


class Save10Discount(DiscountStrategy):
    def calculate_discount(self, subtotal: Decimal) -> Decimal:
        return subtotal * Decimal("0.1")


class FiveBucksOffDiscount(DiscountStrategy):
    def calculate_discount(self, subtotal: Decimal) -> Decimal:
        return Decimal("5.00")


class FreeShippingDiscount(DiscountStrategy):
    def calculate_discount(self, subtotal: Decimal) -> Decimal:
        return Decimal("2.00")


class BlackFridayDiscount(DiscountStrategy):
    def calculate_discount(self, subtotal: Decimal) -> Decimal:
        return subtotal * Decimal("0.2")


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.50"), 10),
            Item("Banana", Decimal("2.00"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
        discount_strategy=Save10Discount()
    )

    cart.display()

    # Change the discount strategy
    cart.discount_strategy = BlackFridayDiscount()
    print("\nAfter applying Black Friday discount:")
    cart.display()


if __name__ == "__main__":
    main()
