from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity

    def set_price(self, price: Decimal) -> None:
        self.price = price

    def total_price(self) -> Decimal:
        return self.price * self.quantity

    def display(self) -> str:
        total_price = self.total_price()
        return f"{self.name:<12}${self.price:>7.2f}{self.quantity:>7}     ${total_price:>7.2f}"


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discount_code: str | None = None

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def update_item_quantity(self, item_name: str, quantity: int) -> None:
        for item in self.items:
            if item.name == item_name:
                item.set_quantity(quantity)

    def update_item_price(self, item_name: str, price: Decimal) -> None:
        for item in self.items:
            if item.name == item_name:
                item.set_price(price)

    def remove_item(self, item_name: str) -> None:
        self.items = [item for item in self.items if item.name != item_name]

    def calculate_total(self) -> Decimal:
        return sum(item.total_price() for item in self.items)

    def print_cart(self) -> None:
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self.items:
            print(item.display())
        print("=" * 40)
        print(f"Total: ${self.calculate_total():>7.2f}")


def main() -> None:
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.5"), 10),
            Item("Banana", Decimal("2"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
    )

    cart.update_item_quantity("Apple", 10)
    cart.update_item_price("Pizza", Decimal("3.50"))
    cart.remove_item("Banana")
    
    cart.print_cart()


if __name__ == "__main__":
    main()