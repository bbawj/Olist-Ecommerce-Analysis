import pandas as pd

#data1 = pd.read_csv("olist_customers_dataset.csv")
data2 = pd.read_csv("olist_order_items_dataset.csv")
data3 = pd.read_csv("olist_order_payments_dataset.csv")
data4 = pd.read_csv("olist_order_reviews_dataset.csv")
data5 = pd.read_csv("olist_orders_dataset.csv")
data6 = pd.read_csv("olist_products_dataset.csv")
data7 = pd.read_csv("product_category_name_translation.csv")

new = pd.merge(data2, data3, on='order_id')
new1 = pd.merge(new, data4, on='order_id')
new2 = pd.merge(new1, data5, on='order_id')
new3 = pd.merge(new2, data6, on='product_id')
print(len(data2.order_id.unique()))

# translate category names to english
translate = data7.set_index('product_category_name').to_dict()[
    'product_category_name_english']

new3['product_category_name'].replace(translate, inplace=True)

print(new3["product_category_name"])
