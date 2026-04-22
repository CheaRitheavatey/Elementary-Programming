"""
unit testing
"""
import pytest
from product import Product
from shopping_cart import ShoppingCart

class TestShoppingCart:
    
    @pytest.fixture # this run before each test, if the test request it
    def cart(self):
        return ShoppingCart() # constructor calling -> create instance
    
    @pytest.fixture
    def product1(self):
        return Product('Bread', 500)
    
    @pytest.fixture
    def product2(self):
        return Product('Milk', 400)
    
    # what are we testing?
    # 3 types: 
    # type 1: Happy path (normal behavior of function)
    # naming convention: must start with 'test_'+ <what it does>_<what happens> 
    # example, test_remove_item_removes_from_cart
    def test_new_cart_is_empty(self, cart):
        assert cart.is_empty()
    
    def test_add_item_increases_count(self, cart, product1):
        cart.add_item(product1,2)
        assert cart.get_item_count() == 2
        
        
    def test_get_total_calculates_correct_sum(self, cart, product1, product2):
        cart.add_item(product1, 2) # bread = 1000
        cart.add_item(product2, 3) # milk = 1200
        
        assert cart.get_total() == 2200
        

    def test_add_same_product_twice_accumulates_quantity(self, cart, product1):
        cart.add_item(product1, 2)
        cart.add_item(product1, 3)
        
        assert cart.get_item_count() == 5
        assert cart.get_total() == 2500
        
    def test_remove_item_removes_from_cart(self, cart, product1, product2):
        cart.add_item(product1,2)
        cart.add_item(product2,3)
        
        cart.remove_item(product1)
        assert cart.get_item_count() == 3
        assert cart.get_total() == 1200
        
        
    def test_clear_empties_cart(self, cart, product1, product2):
        cart.add_item(product1,2)
        cart.add_item(product2,1)
        cart.clear()
        
        assert cart.is_empty()
        assert cart.get_item_count() == 0
        
    def test_empty_cart_total_is_zero(self, cart):
        assert cart.get_total() == 0
        
    def test_empty_cart_item_count_is_zero(self,cart):
        assert cart.get_item_count() == 0
        
        
    # error case
    def test_add_none_product_raises(self, cart):
        with pytest.raises(ValueError):
            cart.add_item(None,1)
    
    def test_add_zero_quantity_raises(self, cart,product1):
        with pytest.raises(ValueError):
            cart.add_item(product1,0)
            
    def test_add_negative_quantity_raises(self, cart, product1):
        with pytest.raises(ValueError):
            cart.add_item(product1, -3)
            
    def test_add_non_product_raises(self, cart):
        with pytest.raises(TypeError):
            cart.add_item('Banana', 2)
            
    def test_remove_non_product_raises(self,cart):
        with pytest.raises(TypeError):
            cart.remove_item("Banana")
    def test_remove_nonexistent_product_raises(self,cart, product1):
        with pytest.raises(ValueError):
            cart.remove_item(product1)