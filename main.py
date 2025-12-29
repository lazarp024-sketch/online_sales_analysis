from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()

    p1 = Product("Laptop", 1000, 3)
    p2 = Product("Miš", 20, 10)
    p3 = Product("Tastatura", 50, 5)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    print("Proizvodi:")
    manager.display_products()

    print("\nUkupna vrednost inventara:", manager.total_value())


if __name__ == "__main__":
    main()
