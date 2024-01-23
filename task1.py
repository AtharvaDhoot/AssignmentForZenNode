PRODUCTS_STORE = [
    {"name": "Coldrink", "price": 20},
    {"name": "Bulb", "price": 40},
    {"name": "Headphones", "price": 50},
]

def calculate_flat_10_discount(total_sum):
  if (total_sum > 200):
    return 10
  return 0

def calculate_bulk_5_discount(quantities = [], prices = []):
  bulk_5_discount = 0
  for quantity, price in zip(quantities, prices):
    if quantity > 10:
      discount = (price * quantity) * 0.05
      bulk_5_discount += discount
  return bulk_5_discount

def calculate_bulk_10_discount(total_quantity, total_sum):
  if(total_quantity > 20):
    return (total_sum * 0.10)
  return 0

def calculate_tiered_50_discount(quantities, prices):
  discount = 0
  if sum(quantities) > 30:
    for quantity, price in zip(quantities, prices):
      if quantity > 15:
        remaining_quantity = quantity - 15
        new_price = (price * 0.5)
        product_discount = (remaining_quantity * new_price)
        discount += product_discount
  return discount

def calculate_gift_wrap_fee(is_wrapped, total_quantity):
  return total_quantity if is_wrapped else 0

def calculate_shipping_fee(total_quantity):
  bags = total_quantity // 10
  if(total_quantity % 10 != 0):
    bags += 1

  return bags * 5

def get_max_discount(total_sum, total_quantity, prices, quantities):
    discounts = [
        ("Flat 10", calculate_flat_10_discount(total_sum)),
        ("Bulk 5", calculate_bulk_5_discount(quantities, prices)),
        ("Bulk 10", calculate_bulk_10_discount(total_quantity, total_sum)),
        ("Tiered 50", calculate_tiered_50_discount(quantities, prices)),
    ]
    return max(discounts, key=lambda discount_item: discount_item[1])

def calculate_final_price(total_sum, discount_amount, shipping_fee, wrapping_fee):
    return (total_sum - discount_amount) + shipping_fee + wrapping_fee

def take_order(products):
    order = []
    for product in products:
        product_name = product["name"]
        price = product["price"]
        quantity = int(input(f"Enter quantity for {product_name}: "))
        is_wrapped = input(f"Do you want {product_name} to be gift wrapped(Y/N)? ").lower() == "y"
        order.append({"name": product_name, "price": price, "quantity": quantity, "is_wrapped": is_wrapped})
    return order

def display_order_summary(order, total_sum, discount_name, discount_amount, shipping_fee, wrapping_fee):
    print("\nProduct Details:")
    for order_item in order:
        product_name, quantity, price = order_item["name"], order_item["quantity"], order_item["price"]
        total = price * quantity
        print(f"{product_name}: Quantity- ${quantity}, Total- ${total}")

    print(f"\nTotal Sum: {total_sum}")
    print(f"Discount offer applied: {discount_name}")
    print(f"Discount amount applied: ${discount_amount}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${wrapping_fee}")

    final_price = calculate_final_price(total_sum, discount_amount, shipping_fee, wrapping_fee)
    print("\nFinal Price:", final_price)

def main():
    print("Welcome to EaziShopping!")

    products = PRODUCTS_STORE
    order = take_order(products)

    total_sum, total_wrapping_fee = 0, 0
    quantities, prices = [], []

    for order_item in order:
        quantity, price, is_wrapped = order_item["quantity"], order_item["price"], order_item["is_wrapped"]
        total_amount = price * quantity
        wrapping_fee = calculate_gift_wrap_fee(is_wrapped, quantity)

        prices.append(price)
        quantities.append(quantity)
        total_sum += total_amount
        total_wrapping_fee += wrapping_fee

    total_quantity = sum(quantities)
    shipping_fee = calculate_shipping_fee(total_quantity)

    discount_name, discount_amount = get_max_discount(total_sum, total_quantity, prices, quantities)
    display_order_summary(order, total_sum, discount_name, discount_amount, shipping_fee, total_wrapping_fee)

if __name__ == "__main__":
    main()
