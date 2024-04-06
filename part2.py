from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def get_product_category_pairs(df_products, df_categories):
	joined_df = df_products.join(df_categories, 'product_id', 'inner').select('product_name', 'category_name')

	products_with_no_category = df_products.join(df_categories, 'product_id', 'left_anti').select('product_name')

	return joined_df.unionAll(products_with_no_category.withColumn('category_name', col('product_name')).select('product_name', 'category_name'))

if __name__ == "__main__":
	spark = SparkSession.builder \
		.appName("Categorize") \
		.getOrCreate()

	products_data = [("prod1", 1), ("prod2", 2), ("prod3", 3), ("prod4", 4), ("prod5", 5)]
	categories_data = [(1, "cat1"), (2, "cat2"), (5, "cat5")]

	df_products = spark.createDataFrame(products_data, ["product_name", "product_id"])
	df_categories = spark.createDataFrame(categories_data, ["product_id", "category_name"])

	result_df = get_product_category_pairs(df_products, df_categories)
	result_df.show()

	spark.stop()
