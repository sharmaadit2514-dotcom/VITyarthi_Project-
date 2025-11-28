# ---------- products data ----------
PRODUCTS = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Phone", "price": 25000},
    3: {"name": "Headphones", "price": 2000},
    4: {"name": "Keyboard", "price": 1500},
    5: {"name": "Mouse", "price": 800},
}


def show_products():
    print("\n==== PRODUCT LIST ====")
    for pid, info in PRODUCTS.items():
        print(f"{pid}. {info['name']} - Rs.{info['price']}")
    print("======================\n")


# ---------- shopping cart class ----------
class ShoppingCart:
    def __init__(self):
        # items will be {product_id: qty}
        self.items = {}

    def add_item(self, product_id, qty):
        if product_id not in PRODUCTS:
            print("Invalid product id!")
            return
        if qty <= 0:
            print("Quantity must be positive!")
            return
        self.items[product_id] = self.items.get(product_id, 0) + qty
        print(f"Added {qty} x {PRODUCTS[product_id]['name']} to cart.")

    def remove_item(self, product_id, qty=None):
        if product_id not in self.items:
            print("Item not in cart!")
            return
        if qty is None or qty >= self.items[product_id]:
            removed_qty = self.items.pop(product_id)
            print(f"Removed {removed_qty} x {PRODUCTS[product_id]['name']} from cart.")
        else:
            self.items[product_id] -= qty
            print(f"Removed {qty} x {PRODUCTS[product_id]['name']} from cart.")

    def view_cart(self):
        if not self.items:
            print("\nCart is empty.\n")
            return
        print("\n===== YOUR CART =====")
        total = 0
        for pid, qty in self.items.items():
            name = PRODUCTS[pid]["name"]
            price = PRODUCTS[pid]["price"]
            subtotal = price * qty
            total += subtotal
            print(f"{name} (x{qty}) - Rs.{price} each -> Rs.{subtotal}")
        print(f"TOTAL: Rs.{total}")
        print("=====================\n")

    def get_total(self):
        total = 0
        for pid, qty in self.items.items():
            total += PRODUCTS[pid]["price"] * qty
        return total

    def print_bill(self):
        if not self.items:
            print("\nCart is empty. No bill to print.\n")
            return

        print("\n=========== FINAL BILL ===========")
        print("Item                Qty    Price    Subtotal")
        print("--------------------------------------------")

        total = 0
        for pid, qty in self.items.items():
            name = PRODUCTS[pid]["name"]
            price = PRODUCTS[pid]["price"]
            subtotal = price * qty
            total += subtotal
            # format name to max 18 chars for alignment
            name_str = name[:18].ljust(18)
            print(f"{name_str} {str(qty).rjust(3)}  Rs.{str(price).rjust(6)}  Rs.{str(subtotal).rjust(7)}")

        print("--------------------------------------------")
        print(f"TOTAL AMOUNT TO PAY: Rs.{total}")
        print("Thank you for shopping with us!")
        print("============================================\n")


# ---------- main menu loop ----------
def main():
    cart = ShoppingCart()

    while True:
        print("==== ONLINE SHOPPING MART ====")
        print("1. Show products")
        print("2. Add to cart")
        print("3. Remove from cart")
        print("4. View cart")
        print("5. Checkout and print bill")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            show_products()

        elif choice == "2":
            show_products()
            try:
                pid = int(input("Enter product id to add: "))
                qty = int(input("Enter quantity: "))
                cart.add_item(pid, qty)
            except ValueError:
                print("Please enter valid numbers!")

        elif choice == "3":
            if not cart.items:
                print("Cart is empty, nothing to remove.")
                continue
            cart.view_cart()
            try:
                pid = int(input("Enter product id to remove: "))
                qty_input = input("Enter quantity to remove (leave blank to remove all): ")
                if qty_input.strip() == "":
                    cart.remove_item(pid)  # remove all of that item
                else:
                    qty = int(qty_input)
                    cart.remove_item(pid, qty)
            except ValueError:
                print("Please enter valid numbers!")

        elif choice == "4":
            cart.view_cart()

        elif choice == "5":
            # print detailed bill and exit
            cart.print_bill()
            break

        else:
            print("Invalid choice, please try again.")

        input("Press Enter to continue...\n")


if __name__ == "__main__":
    main()
