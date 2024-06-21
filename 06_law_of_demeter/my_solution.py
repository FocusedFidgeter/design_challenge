from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discount_code: str | None = None


def main() -> None:
    # Create a shopping cart and add some items to it
    # I feel like there is a violation here as well.
    # There should be an `append` function inside `ShoppingCart` or something
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.5"), 10),
            Item("Banana", Decimal("2"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
    )

    # Update some items' quantity and price - Violation - turn into properties with getter/setter
    cart.items[0].quantity = 10
    cart.items[2].price = Decimal("3.50")

    # Remove an item - Violation - turn into a scoped function
    cart.items.remove(cart.items[1])
	# Violation - turn `total` into a scoped function inside `ShoppingCart`
	# Violation - turn the "inside-loop total" into a scoped function inside `item`
    total = sum(item.price * item.quantity for item in cart.items)

    # Print the cart - Violation - turn into a scoped function inside `ShoppingCart`
    print("Shopping Cart:")
    print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
    for item in cart.items:
        total_price = item.price * item.quantity
        print(
            f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${total_price:>7.2f}"
        )
    print("=" * 40)
    print(f"Total: ${total:>7.2f}")


if __name__ == "__main__":
    main()
