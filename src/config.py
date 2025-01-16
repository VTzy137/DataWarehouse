
from pyspark.sql.types import StructType, StructField, StringType

rename_swiggy = {
  "Area": "Area swiggy",
  "City": "Restaurant city swiggy", 
  "Restaurant": "Restaurant swiggy",
  "Avg ratings": "Ratings swiggy",
  "Address": "Customer address swiggy",
  "Price": "Price swiggy",
  "Total": "Total ratings swiggy",
  "Food type": "Food type swiggy",
  "Delivery time" : "Delivery time swiggy",
}

rename_zomato = {
  "Restaurant Name": "Restaurant zomato",
  "Rate (out of 5)": "Ratings zomato",
  "Num of ratings": "Total ratings zomato",
  "Avg cost (two people)": "Price zomato",
  "Cuisines type": "Food type zomato",
  "Area": "Area zomato",
  "Local address": "Address zomato",
}

rename_reviews = {
  "Business_name": "Restaurant",
}

schema = StructType([
    StructField("id", StringType(), True),
    StructField("restaurant", StringType(), True),
    StructField("rating", StringType(), True)
])