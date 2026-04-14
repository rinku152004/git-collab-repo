"""cart system using composition.
Requirements:
Create class Product → name, price, category
Create class Cart → contains list of Product objects
Implement methods:
add_product(product)
remove_product(product_name)
get_total_price()
apply_coupon(code)
Coupons:
"NEW10" → 10% off
"FLAT50" → ₹50 off
Show final bill with discount applied.
======================================================================================
# -------------------------------
# Cart System Using Composition
# -------------------------------
"""
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


class Cart:
    def __init__(self):
        self.products = []      # list of Product objects (Composition)
        self.discount = 0
        self.coupon_code = None

    def add_product(self, product):
        self.products.append(product)
        print(" Product Added:", product.name)

    def remove_product(self, product_name):
        if len(self.products) == 0:
            print("Cart is empty!")
            return

        for i in range(len(self.products)):
            if self.products[i].name.lower() == product_name.lower():
                removed = self.products[i]
                del self.products[i]
                print("Removed Product:", removed.name)
                return

        print(" Product not found in cart!")

    def get_total_price(self):
        total = 0
        for p in self.products:
            total = total + p.price
        return total

    def apply_coupon(self, code):
        total = self.get_total_price()

        if total == 0:
            print(" Cart is empty. Add products first!")
            return

        code = code.upper()
        self.discount = 0
        self.coupon_code = None

        if code == "NEW10":
            self.discount = total * 0.10   # 10% off
            self.coupon_code = "NEW10"
            print(" Coupon Applied: NEW10 (10% off)")

        elif code == "FLAT50":
            self.discount = 50             # flat ₹50 off
            self.coupon_code = "FLAT50"
            print(" Coupon Applied: FLAT50 (₹50 off)")
        elif code== "FLAT35":
            self.discount=35
            self.coupon_code="FLAT35"
            print(" Coupon Applied: FLAT35 (₹35 off)")

        else:
            print(" Invalid Coupon Code!")
            return

        # If discount becomes greater than total (just safety)
        if self.discount > total:
            self.discount = total

    def show_bill(self):
        if len(self.products) == 0:
            print(" Cart is empty!")
            return

        total = self.get_total_price()
        final_amount = total - self.discount

        print("\n=======================================")
        print("              FINAL BILL")
        print("=======================================")
        print("Items in Cart:")
        print("---------------------------------------")

        for i in range(len(self.products)):
            p = self.products[i]
            print(f"{i+1}. {p.name} ({p.category}) : ₹ {p.price}")

        print("---------------------------------------")
        print("Total Price     : ₹", total)

        if self.coupon_code is not None:
            print("Coupon Applied  :", self.coupon_code)
            print("Discount        : ₹",round(self.discount, 2))
        else:
            print("Coupon Applied  : None")
            print("Discount        : ₹0")

        print("---------------------------------------")
        print("Final Amount    : ₹", round(final_amount, 2))
        print("=======================================\n")


# -------------------------------
# Menu Driven Program
# -------------------------------
cart = Cart()

while True:
    print("\n========== SHOPPING CART MENU ==========")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Apply Coupon")
    print("4. Show Bill")
    print("5. Exit")
    print("=======================================")

    choice = input("Enter your choice (1-5): ")

    if choice == "1" or choice=="Add Product":
        name = input("Enter Product Name: ")
        category = input("Enter Product Category: ")

        try:
            price = float(input("Enter Product Price: "))
            if price <= 0:
                print(" Price must be greater than 0!")
                continue
        except:
            print(" Invalid price input!")
            continue

        product = Product(name, price, category)
        cart.add_product(product)

    elif choice == "2"or choice=="Remove Product":
        pname = input("Enter Product Name to remove: ")
        cart.remove_product(pname)

    elif choice == "3"or choice=="Apply Coupon":
        code = input("Enter Coupon Code (NEW10 / FLAT50/FLAT35): ")
        cart.apply_coupon(code)

    elif choice == "4"or choice=="Show Bill":
        cart.show_bill()

    elif choice == "5"or choice=="Exit":
        print("Thanks for shopping! Exiting...")
        break

    else:
        print(" Invalid choice! Enter only from options given (either number(1 to 5) or text options).")
