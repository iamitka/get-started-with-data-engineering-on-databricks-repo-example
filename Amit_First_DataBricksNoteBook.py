# Databricks notebook source
# MAGIC %md
# MAGIC ### Creting my first databricks file

# COMMAND ----------

# Print "Hello, World!"
print("Hello, World!")

# COMMAND ----------

# Function to generate Fibonacci series
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage
n = 10
series = fibonacci_series(n)
print(series)
