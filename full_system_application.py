# full_system_application.py

from abc import ABC, abstractmethod
from enum import Enum, auto
import typing

# ====================================================================
# 1. Product Module (Encapsulation / Immutability)
# ====================================================================
class Product:
    """
    Represents a product with immutable properties using encapsulation.
    Properties: product_id, name, price.
    """
    def __init__(self, product_id, name, price):
        self._product_id = product_id
        self._name = name
        self._price = price

    @property
    def product_id(self):
        """Getter for the immutable product_id."""
        return self._product_id

    @property
    def name(self):
        """Getter for the immutable name."""
        return self._name

    @property
    def price(self):
        """Getter for the immutable price."""
        return self._price

    def display_details(self):
        """Displays product details."""
        print(f"--- Product Details ---")
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

# ====================================================================
# 2. User Module (Inheritance)
# ====================================================================
class User:
    """Base class for all users."""
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def display_details(self):
        print(f"--- User Details ---")
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

class Admin(User):
    """Admin user class, inherits from User. Can view all orders."""
    def view_all_orders(self):
        print(f"Admin {self.name} is viewing all system orders.")

class Customer(User):
    """Customer user class, inherits from User. Can place orders."""
    def place_order(self, order_details):
        print(f"Customer {self.name} is placing an order: {order_details}")

# ====================================================================
# 3. Order Module (Composition)
# ====================================================================
class OrderStatus(Enum):
    """Enumeration for maintaining order status."""
    CREATED = auto()
    PAID = auto()
    CANCELLED = auto()

class Order:
    """
    Represents a customer order. Uses composition: an Order has a list of Products.
    """
    def __init__(self, order_id, customer_email):
        self.order_id = order_id
        self.customer_email = customer_email
        self._products: typing.List[Product] = []  # Composition link
        self.status = OrderStatus.CREATED

    def add_product(self, product: Product):
        """Adds a product to the order."""
        if self.status == OrderStatus.CREATED:
            self._products.append(product)
            print(f"Added '{product.name}' to Order {self.order_id}.")
        else:
            print(f"Cannot add products to an order that is {self.status.name}.")

    def calculate_total(self):
        """Calculates the total cost dynamically."""
        total = sum(product.price for product in self._products)
        return total

    def set_status(self, new_status: OrderStatus):
        """Updates the order status."""
        self.status = new_status
        # print(f"Order {self.order_id} status updated to {self.status.name}.")

    def display_order_summary(self):
        """Displays a summary of the order."""
        print(f"\n--- Order Summary (ID: {self.order_id}) ---")
        print(f"Status: {self.status.name}")
        print(f"Items: {[p.name for p in self._products]}")
        print(f"Total: ${self.calculate_total():.2f}")

# ====================================================================
# 4. Payment/Notification Modules & Order Service (Abstraction/DI/SRP)
# ====================================================================

# --- Payment Module (Abstraction + Polymorphism) ---
class PaymentMethod(ABC):
    """Abstract Base Class (ABC) defining the common interface."""
    @abstractmethod
    def process_payment(self, amount):
        pass

class UPIPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing UPI payment of ${amount:.2f}."

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing Credit Card payment of ${amount:.2f}."

class NetBankingPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing NetBanking payment of ${amount:.2f}."

# --- Notification Module (Polymorphism + Dependency Injection) ---
class Notifier(ABC):
    """Abstract interface for notification services."""
    @abstractmethod
    def send_notification(self, recipient, message):
        pass

class EmailNotifier(Notifier):
    def send_notification(self, recipient, message):
        print(f"[EMAIL Sent to {recipient}]: {message}")

class SMSNotifier(Notifier):
    def send_notification(self, recipient, message):
        print(f"[SMS Sent to {recipient}]: {message}")

# --- Order Service (System Design Focus / Single Responsibility) ---
class OrderHandler:
    """
    Handles order finalization using DI for payment and notification services.
    Acts as the 'Order Service' described in the NFRs.
    """
    def __init__(self, payment_service: PaymentMethod, notification_service: Notifier):
        # Dependency Injection: Services are provided externally
        self._payment_service = payment_service
        self._notification_service = notification_service

    def finalize_order(self, order: Order):
        """Finalizes the order using injected dependencies (polymorphism in action)."""
        amount = order.calculate_total()
        
        # Polymorphic call
        payment_status_message = self._payment_service.process_payment(amount)
        print(payment_status_message)
        
        # Use injected notifier to confirm
        order.set_status(OrderStatus.PAID)
        notification_message = f"Your order {order.order_id} for ${amount:.2f} has been paid and is confirmed."
        
        # Polymorphic call
        self._notification_service.send_notification(order.customer_email, notification_message)


# ====================================================================
# 5. Main Execution / Testing Workflow (as requested in images)
# ====================================================================
def run_test_workflow():
    print("--- Running Full System Test Workflow ---")

    # Storage for simulation (in-memory databases)
    products_db = {}
    users_db = {}
    orders_db = {}

    # 1. Create customer
    print("\n#### 1. Creating Customer")
    customer = Customer(user_id=1, name="Test Bob", email="bob@test.com")
    users_db[customer.user_id] = customer
    customer.display_details()

    # 2. Create products
    print("\n#### 2. Creating Products")
    p1 = Product(product_id=10, name="Widget A", price=19.99)
    p2 = Product(product_id=20, name="Widget B", price=45.50)
    products_db[p1.product_id] = p1
    products_db[p2.product_id] = p2
    p1.display_details()
    p2.display_details()

    # 3. Create order
    print("\n#### 3. Creating Order")
    order = Order(order_id=101, customer_email=customer.email)
    order.add_product(p1)
    order.add_product(p2)
    orders_db[order.order_id] = order
    order.display_order_summary()

    # 4. Select payment method dynamically (e.g., Credit Card)
    # 5. Process payment
    # 6. Send notification
    print("\n#### 4, 5, & 6. Selecting Payment, Processing, and Notifying")
    payment_service = CreditCardPayment()
    notification_service = EmailNotifier()
    
    handler = OrderHandler(payment_service, notification_service)
    handler.finalize_order(order)
    order.display_order_summary()

    # 7. Admin views order list
    print("\n#### 7. Admin Views Order List")
    admin_user = Admin(user_id=999, name="Super Admin", email="admin@test.com")
    admin_user.view_all_orders()
    
    print(f"\nTotal Orders in System: {len(orders_db)}")
    for o_id, o in orders_db.items():
        print(f"-> Order {o_id}: Status={o.status.name}, Total=${o.calculate_total():.2f}")

    print("\n--- Workflow Complete ---")


if __name__ == "__main__":
    run_test_workflow()
