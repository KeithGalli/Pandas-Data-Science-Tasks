import datetime
import calendar
import random
import numpy
import pandas as pd
import uuid

products = {
  'iPhone': [700, 10],
  'Google Phone': [600, 8],
  'Vareebadd Phone': [400, 3],
  '20in Monitor': [109.99,6],
  '34in Ultrawide Monitor': [379.99, 9],
  '27in 4K Gaming Monitor': [389.99,9],
  '27in FHD Monitor': [149.99, 11],
  'Flatscreen TV': [300, 7],
  'Macbook Pro Laptop': [1700, 7],
  'ThinkPad Laptop': [999.99, 6],
  'AA Batteries (4-pack)': [3.84, 30],
  'AAA Batteries (4-pack)': [2.99, 30],
  'USB-C Charging Cable': [11.95, 30],
  'Lightning Charging Cable': [14.95, 30],
  'Wired Headphones': [11.99, 26],
  'Bose SoundSport Headphones': [99.99, 19],
  'Apple Airpods Headphones': [150, 22],
  'LG Washing Machine': [600.00, 1],
  'LG Dryer': [600.00, 1]
}

columns = ['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date', 'Purchase Address']

def generate_random_time(month):
  day = generate_random_day(month)
  if random.random() < 0.5:
    date = datetime.datetime(2019, month, day,12,00)
  else:
    date = datetime.datetime(2019, month, day,20,00)
  time_offset = numpy.random.normal(loc=0.0, scale=180)
  final_date = date + datetime.timedelta(minutes=time_offset)
  return final_date.strftime("%m/%d/%y %H:%M")

def generate_random_day(month):
  day_range = calendar.monthrange(2019,month)[1]
  return random.randint(1,day_range)

def generate_random_address():
  street_names = ['Main', '2nd', '1st', '4th', '5th', 'Park', '6th', '7th', 'Maple', 'Pine', 'Washington', '8th', 'Cedar', 'Elm', 'Walnut', '9th', '10th', 'Lake', 'Sunset', 'Lincoln', 'Jackson', 'Church', 'River', '11th', 'Willow', 'Jefferson', 'Center', '12th', 'North', 'Lakeview', 'Ridge', 'Hickory', 'Adams', 'Cherry', 'Highland', 'Johnson', 'South', 'Dogwood', 'West', 'Chestnut', '13th', 'Spruce', '14th', 'Wilson', 'Meadow', 'Forest', 'Hill', 'Madison']
  cities = ['San Francisco', 'Boston', 'New York City', 'Austin', 'Dallas', 'Atlanta', 'Portland', 'Portland', 'Los Angeles', 'Seattle']
  weights = [9,4,5,2,3,3,2,0.5,6,3]
  zips = ['94016', '02215', '10001', '73301', '75001', '30301', '97035', '04101', '90001', '98101']
  state = ['CA', 'MA', 'NY', 'TX', 'TX', 'GA', 'OR', 'ME', 'CA', 'WA']

  street = random.choice(street_names)
  index = random.choices(range(len(cities)), weights=weights)[0]

  return f"{random.randint(1,999)} {street} St, {cities[index]}, {state[index]} {zips[index]}"

def create_data_csv():
  pass

def write_row(order_number, product, order_date, address):
  product_price = products[product][0]
  quantity = numpy.random.geometric(p=1.0-(1.0/product_price), size=1)[0]
  output = [order_number, product, quantity, product_price, order_date, address]
  return output

if __name__ == '__main__':
  order_number = 141234
  for month in range(1,13):
    if month <= 10:
      orders_amount = int(numpy.random.normal(loc=12000, scale=4000))
    elif month == 11:
      orders_amount = int(numpy.random.normal(loc=20000, scale=3000))
    else: # month == 12
      orders_amount = int(numpy.random.normal(loc=26000, scale=3000))

    product_list = [product for product in products]
    weights = [products[product][1] for product in products]

    df = pd.DataFrame(columns=columns)
    print(orders_amount)

    i = 0
    while orders_amount > 0:

      address = generate_random_address()
      order_date = generate_random_time(month)

      product_choice = random.choices(product_list, weights)[0]
      df.loc[i] = write_row(order_number, product_choice, order_date, address)
      i += 1

      # Add some items to orders with random chance
      if product_choice == 'iPhone':
        if random.random() < 0.15:
          df.loc[i] = write_row(order_number, "Lightning Charging Cable", order_date, address)
          i += 1
        if random.random() < 0.05:
          df.loc[i] = write_row(order_number, "Apple Airpods Headphones", order_date, address)
          i += 1

        if random.random() < 0.07:
          df.loc[i] = write_row(order_number, "Wired Headphones", order_date, address)
          i += 1 

      elif product_choice == "Google Phone" or product_choice == "Vareebadd Phone":
        if random.random() < 0.18:
          df.loc[i] = write_row(order_number, "USB-C Charging Cable", order_date, address)
          i += 1
        if random.random() < 0.04:
          df.loc[i] = write_row(order_number, "Bose SoundSport Headphones", order_date, address)
          i += 1
        if random.random() < 0.07:
          df.loc[i] = write_row(order_number, "Wired Headphones", order_date, address)
          i += 1 

      if random.random() <= 0.02:
        product_choice = random.choices(product_list, weights)[0]
        df.loc[i] = write_row(order_number, product_choice, order_date, address)
        i += 1

      if random.random() <= 0.002:
        df.loc[i] = columns
        i += 1

      if random.random() <= 0.003:
        df.loc[i] = ["","","","","",""]
        i += 1

      order_number += 1
      orders_amount -= 1

    month_name = calendar.month_name[month]
    df.to_csv(f"Sales_{month_name}_2019.csv", index=False)
    print(f"{month_name} Complete")