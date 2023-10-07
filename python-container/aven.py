import datetime
import calendar
import random
import numpy
import pandas as pd
import uuid

#weight -> golongan
#1 Obat Herbal
#2 Obat Jamu
#3 Obat Bebas
#4 Obat Bebas Terbatas
#5 Obat Keras

#configurasi, ooo SODAH JELASSS Ye Kan???
products = {
  'KOMIX G-FORM JERUK NIPIS 30S': [1400.0, 4],
  'Amoxicillin 500 Mg Kapsul Hexpharm': [500.0, 5],
  'CAPTOPRIL IF 25MG TAB': [2197.0, 5],
  'IBUPROFEN 400MG TAB': [594.0, 5],
  'ASAM MEFENAMAT BERNO 500MG': [423.0, 5],
  'Paracetamol 500 mg 10 Kaplet': [1500.0, 3],
  'CEFIXIME DEXA 100MG CAP 50S': [149.99, 5],
  'CEFADROXIL BERNO 500MG CAP': [1707.0, 5],
  'SIMVASTATIN DEXA 10MG TAB': [1151.0, 5],
  'COTRIMOXAZOLE BERNO 960MG TAB 100S': [782.0, 5],
  'LISINOPRIL 10MG TAB NOVELL': [780.0, 5],
  'Tremenza Sirup 60 ml': [22000.0, 4],
  'USB-C Charging Cable': [11.95, 30],
  'PONSTAN 500MG TAB': [3356.0, 5],
  'Ranitidine 150 mg 10 Tablet': [1800.0, 5],
  'Metformin 500 mg 10 Tablet': [2000.0, 5],
  'PROPANOLOL DEXA 10MG TAB': [117.0, 5],
  'ORALIT KIMIA FARMA 200 MG SACHET': [1000.0, 3],
  'ANTANGIN JRG ORIGINAL SACH': [38150.0, 2],
  'VEGETA HERBAL ANGGUR SACH': [17158.0, 2],
  'TENACE 10MG': [5971.0, 5],
  'DIABEMED CAP 24S': [39972.0, 2],
  'ITRACONAZOLE 100MG TAB BERNO': [6164.0, 5],
  'CERETON CAP': [6744.0, 5],
  'TENACE 10MG': [5971.0, 5],
  'ZINE 10MG FC TAB 30S': [5710.0, 3],
  'THERMOLYTE MAXIMUS 30S': [54384.0, 3],
  'Biosan 275 mg 6 Tablet': [100000.0, 1],
  'TRENTAL 400MG TAB': [17055.0, 5],
  'PROPYLTHIOURACIL DEXA 100MG TAB': [649.0, 5],
  'MERIT SACH 30S': [45615.0, 2],  
  'Nitrokaf Retard 2.5 mg 10 Kapsul': [28000.0, 5]
}
#index
columns = ['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date', 'Purchase Address']

def generate_random_time(month):
  day = generate_random_day(month)
  if random.random() < 0.5:
    date = datetime.datetime(2020, month, day,12,00)
  else:
    date = datetime.datetime(2020, month, day,20,00)
  time_offset = numpy.random.normal(loc=0.0, scale=180)
  final_date = date + datetime.timedelta(minutes=time_offset)
  return final_date.strftime("%m/%d/%y %H:%M")

#configurasi tanggal
def generate_random_day(month):
  day_range = calendar.monthrange(2020,month)[1]
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

#semacam denyut, untuk membuat freq+quantity menjadi tinggi
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
    df.to_csv(f"Sales_{month_name}_2020.csv", index=False) #sIv Fail To name, diganti 
    print(f"{month_name} Complete")


"""
  Perlo Di ingat Ini adalah Cuman Template dataGenerat synthet, Blom sepenohnya UInput, ato sebisa jalanya lah 
"""