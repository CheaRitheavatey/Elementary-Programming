"""
A shopping cart that stores products together with their quantities.
"""

from product import Product


class ShoppingCart:

    def __init__(self):
        self._items: dict[Product, int] = {}
        # Essentially the same as self._items = {}, but with type annotations.

    def add_item(self, product: Product, quantity: int) -> None:
        """
        Adds a product to the shopping cart.
        If the product is already in the cart, the quantity is increased.

        Args:
            product: the product to add
            quantity: the quantity to add; it must be a positive integer

        Raises:
            TypeError: if product is not a Product instance or quantity is not an integer
            ValueError: if product is None or quantity <= 0
        """
        if product is None:
            raise ValueError("Product cannot be None")
        if not isinstance(product, Product):
            raise TypeError("Expected Product instance")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        current_quantity = self._items.get(product, 0)
        self._items[product] = current_quantity + quantity

    def remove_item(self, product: Product) -> None:
        """
        Removes a product from the shopping cart.

        Args:
            product: the product to remove

        Raises:
            TypeError: if product is not a Product instance
            ValueError: if product is None or if the product is not in the cart
        """
        if product is None:
            raise ValueError("Product cannot be None")
        if not isinstance(product, Product):
            raise TypeError("Expected Product instance")
        if product not in self._items:
            raise ValueError("Product not in cart")

        del self._items[product]

    def get_total(self) -> int:
        """Returns the total value of the shopping cart in HUF."""
        total = 0
        for product, quantity in self._items.items():
            total += product.price * quantity
        return total

    def get_item_count(self) -> int:
        """Returns the total number of items in the shopping cart."""
        count = 0
        for quantity in self._items.values():
            count += quantity
        return count

    def clear(self) -> None:
        """Empties the shopping cart."""
        self._items.clear()

    def is_empty(self) -> bool:
        """Returns whether the shopping cart is empty."""
        return len(self._items) == 0