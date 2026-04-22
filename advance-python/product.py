"""
Represents a product in the webshop.
"""


class Product:
    """
    A product with a name and a price.

    Args:
        name: the name of the product; it cannot be empty
        price: the price of the product in HUF; it cannot be negative

    Raises:
        TypeError: if the name is not a string or the price is not an integer
        ValueError: if the name is empty or the price is negative
    """

    def __init__(self, name: str, price: int):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name or name.isspace():
            raise ValueError("Product name cannot be empty")
        if not isinstance(price, int):
            raise TypeError("Price must be an integer")
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._name = name
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> int:
        return self._price