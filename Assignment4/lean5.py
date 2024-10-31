def load_sales_data(product_type, years):
    sales_data = {}
    for year in years:
        sales_data[year] = load(f"data/{product_type}_sales_{year}.csv")
    return sales_data

# List of years
years = [2022, 2023, 2024]

# Get all the sales data by product type
book_sales = load_sales_data("book", years)
game_sales = load_sales_data("game", years)

# Calculate the total sales for each year
total_sales = {year: sum_sales(book_sales[year], game_sales[year]) for year in years}
