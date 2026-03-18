
import pandas as pd
#LOAD DATA
samsung = pd.read_csv('samsung_global_sales_dataset.csv')
pd.read_csv("samsung_global_sales_dataset.csv", encoding="ISO-8859-1")


#EXPLORE DATA
#1.How many total rows and columns are in the dataset?#
#print(samsung.shape)

#2.What are the unique countries in the dataset?#
unique_countries = samsung['country'].unique()
#print(unique_countries)

#3.How many unique products are sold?#
many_country = samsung['country'].nunique()
#print(many_country)

#4.What are the different product categories?#
different_column = samsung["product_name"].unique()
#print(different_column)

#5.What are the different payment methods used?#
payment_methods = samsung["payment_method"].unique()
#print(payment_methods)

#6.How many sales channels exist?#
sales_exist = samsung["sales_channel"].nunique()
#print(sales_exist)

#7.What are the unique customer segments?#
customer = samsung["customer_segment"].unique()
#print(customer)

#8.What are the different customer age groups?#
customer_age = samsung["customer_age_group"].unique()
#print(customer_age)

#9.How many transactions are 5G phones vs non-5G phones?#
is_5g = samsung ["is_5g"].value_counts()
#print(is_5g)

#10.Which currencies appear in the dataset?#
currency_type = samsung["currency"].value_counts()
#print(currency_type)

#11.What is the total revenue generated?#
total_revenue= samsung["revenue_local_currency"].sum()
#print(total_revenue)

#12.Which country generates the highest revenue?
country_revenue = samsung.groupby("country")["revenue_local_currency"].sum().sort_values(ascending=False).head(1)
#print(country_revenue)

#13.Which city has the highest sales?
city_sales = samsung.groupby("city")["revenue_local_currency"].sum().sort_values(ascending=False).head(1)
#print(city_sales)

#14.Which product_name sells the most units?
product_units = samsung.groupby("product_name")["units_sold"].sum().sort_values(ascending=False).head(1)
#print(product_units)

#15.Which category generates the highest revenue?
category_highest = samsung.groupby ("category") ["revenue_usd"].sum().sort_values(ascending=False)
#print(category_highest)

#16.What is the average unit price of products?
average_unit_price = samsung.groupby("product_name") ["unit_price_usd"].mean().sort_values(ascending=False)
#print(average_unit_price)

#17.Which storage variant sells the most (128GB, 256GB etc.)?
storage = samsung.groupby("storage")["units_sold"].sum().sort_values(ascending=False)
#print(storage)

#18.Which color is most popular?
colour = samsung.groupby("color")["units_sold"].sum().sort_values(ascending=False)
#print(colour)

#19.Which sales channel generates the most revenue?
sales_chanel = samsung.groupby ("sales_channel") ["revenue_usd"].sum().sort_values(ascending=False)
#print(sales_chanel)

#20.Which payment method is used the most?
payment = samsung["payment_method"].value_counts()
#print(payment)

#21.What is the average discount percentage given?
discount = samsung["discounted_price_usd"].mean()
#print(discount)

#22.Which product has the highest average discount?
product_discount = samsung.groupby ("product_name") ["discounted_price_usd"].mean().sort_values(ascending=False).head(1)
#print(product_discount)

#23.Which category gets the highest discounts?
category_discount = samsung.groupby ("category") ["discounted_price_usd"].mean().sort_values(ascending=False).head(1)
#print(category_discount)

#24.Which country receives the highest discounts?
country_discount = samsung.groupby ("country") ["discounted_price_usd"].mean().sort_values(ascending=False).head(1)
#print(country_discount)

#25.Compare revenue before and after discounts.
samsung["revenue_before_discount"] = samsung["unit_price_usd"] * samsung["units_sold"]
samsung["revenue_after_discount"] = samsung["discounted_price_usd"] * samsung["units_sold"]
before = samsung["revenue_before_discount"].sum()
after = samsung["revenue_after_discount"].sum()
#print("Revenue Before Discount:", before)
#print("Revenue After Discount:", after)

#26.Create column total price of product
samsung["Total_price_product"] = samsung["unit_price_usd"] * samsung["units_sold"]
#print(samsung["Total_price_product"])

#27.Does higher discount increase units sold?
high_sold = samsung["discounted_price_usd"].corr(samsung["units_sold"])
#print(high_sold)

#28.Which products sell well even with low discounts?
low_discount = samsung[samsung["discount_pct"] <=5]
discount_sale = low_discount.groupby ("product_name") ["units_sold"].sum().sort_values(ascending=False).head(11)
#print(discount_sale)

#29.What is the price range of products sold?
#print(samsung["unit_price_usd"].min())
#print(samsung["unit_price_usd"].max())

#30.Which price range generates the most revenue?
bins = [0,100, 500, 1000, 10000, 40000, 45000 ]
labels = ["Budget", "Mid-range", "Upper Mid-range", "Premium", "Ultra", "Pro"]
samsung ["price_range"] = pd.cut(samsung["unit_price_usd"], bins=bins, labels=labels)
#price_high = samsung.groupby("price_range") ["revenue_usd"].sum().sort_values(ascending=False)
#print(price_high)

#31.Which customer segment buys the most products?
customer_product = samsung.groupby ("customer_segment") ["units_sold"].sum().sort_values(ascending=False)
#print(customer_product)

#32.Which age group buys the most phones?
filter_phones = samsung[samsung["category"]=="Galaxy S"].head(10)
#print(filter_phones)
table_age = filter_phones.groupby ("customer_age_group") ["units_sold"].sum()
#print(table_age)

#33.Which age group generates the highest revenue?
age_revenue = samsung.groupby ("customer_age_group") ["revenue_usd"].mean().sort_values(ascending=False).head(6)
#print(age_revenue)

#34.Do younger customers prefer 5G phones?
young_phone = pd.pivot_table(
    samsung,
    values="units_sold",
    index="customer_age_group",
    columns="is_5g",
    aggfunc="sum"
)
#print(young_phone)

#35.Which payment method is preferred by each age group?
age_payment = pd.pivot_table(
    samsung,
    values = "units_sold",
    index = "payment_method",
    columns = "customer_age_group",
    aggfunc = "sum"
)
#print(age_payment)

#36.Which customer segment prefers online vs offline sales channels?
ecom = samsung[samsung["sales_channel"] == "E-commerce Platform"]
online_offline = ecom.groupby ("customer_segment") ["units_sold"].sum()
#print(online_offline)

#37.Which age group buys the most expensive phones?
filter_phone = samsung[samsung["category"]=="Galaxy A"].head(10)
expensive_phones = filter_phone.groupby ("customer_age_group") ["units_sold"].mean().sort_values(ascending=False).head(11)
#print(expensive_phones)

#38.Which customer segment has the highest average spending?
customer_average = samsung.groupby ("customer_segment") ["units_sold"].mean().sort_values(ascending=False)
#print(customer_average)

#39.Which product category is most popular among young customers?
category_young = pd.pivot_table(
    samsung,
    values = "units_sold",
    index = "category",
    columns = "customer_age_group",
    aggfunc = "sum"
)
#print(category_young)

#40.What is the average customer rating for each product?
customer_rating_product = samsung.groupby("product_name") ["customer_rating"].mean()
#print(customer_rating_product)

#41.Which country should Samsung focus marketing on?
company_marketing = samsung.groupby ("country") ["revenue_usd"].sum().sort_values(ascending=False)
#print(company_marketing)

#42.Which product has the highest revenue but lowest rating?
result = samsung.groupby ("product_name") [["revenue_usd","customer_rating"]].agg({
    "revenue_usd" : "sum",
    "customer_rating" : "mean"
})
low_rate = result.sort_values(by=["revenue_usd", "customer_rating"], ascending=[False, True]).head(11)
#print(low_rate)

#43.Which product has the highest return rate?
high_return = pd.pivot_table(
    samsung,
    values = "units_sold",
    index = "product_name",
    columns = "return_status",
    aggfunc = "mean"
)
#print(high_return)

return_filter = samsung[samsung["return_status"] == "Returned"]
high_returned = return_filter.groupby ("product_name") ["units_sold"].mean()
#print(high_returned)

#44.Which category has the most returns?
category_retun = return_filter.groupby ("category") ["units_sold"].sum().sort_values(ascending=False)
#rint(category_retun)

#45. delete columns
samsung.drop("year", axis=1, inplace=True)
samsung.drop("quarter", axis=1, inplace=True)
samsung.drop("month", axis=1, inplace=True)


#46. replacing nulls
samsung["previous_device_os"] = samsung["previous_device_os"].replace("", None).fillna("Nil")
samsung["customer_rating"] = samsung["customer_rating"].replace("", None).fillna("Nil")
samsung["storage"] = samsung["storage"].replace("", None).fillna("Nil")

#47.In which country and which city are the most products purchased?
high_purchase = samsung.groupby (["country", "city"]) ["units_sold"].mean().sort_values(ascending=False)
#print(high_purchase)

#47.which product has 5g?
filter_fiveG = samsung[samsung["is_5g"]=="Yes"]
product_fiveG = filter_fiveG.groupby("category") ["units_sold"].sum().sort_values(ascending=False)
#print(product_fiveG)

#48.which products have purchased in which sales channel?
sales_product = pd.pivot_table(
    samsung,
    values = "units_sold",
    index = "sales_channel",
    columns = "product_name",
    aggfunc = "sum"
)
#print(sales_product)

#49.separating
samsung["integer_part"] = samsung["revenue_local_currency"].astype(str).str.split(".").str[0]
samsung["decimal_part"] = samsung["revenue_local_currency"].astype(str).str.split(".").str[1]
#print(samsung["integer_part"])
#print(samsung["decimal_part"])
samsung.drop("decimal_part", axis=1, inplace=True)

#50.how many missing values?
miss = samsung.isnull().sum()
#print(miss)

#51.Combining revenue_usd with currency
samsung["revenue_usd_currency"] = samsung["revenue_usd"].astype(str) + " " + samsung["currency"]
#print(samsung["revenue_usd_currency"])

#52. string operations
samsung.columns = samsung.columns.str.capitalize()
#print(samsung.columns)

#53.replacing
samsung["Customer_age_group"] = samsung["Customer_age_group"].astype(str)
samsung["Customer_age_group"] = samsung["Customer_age_group"].str.replace("â€“", "-", regex=False)
#print(samsung["Customer_age_group"])

samsung.drop("Revenue_usd", axis=1, inplace=True)
samsung.drop("Currency", axis=1, inplace=True)


#samsung.to_csv("clean_samsung_dataset.csv")