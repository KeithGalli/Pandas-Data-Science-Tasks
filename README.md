# Sales Analysis
We have a set of data of sales products of each month (given at `/Data/Raw`), and in this project we analyze this data to understand the sales behaviour

## Procedure
We start by cleaning our data. Tasks during this section include:
- Drop NaN values from DataFrame
- Removing rows based on a condition
- Change the type of columns (to_numeric, to_datetime)
- Parse the columns (date, address)
- Store the cleaned data into `/Data/Clean`

Once we have cleaned up our data a bit, we move to the data analysis part. In this part we explore 5 high level business questions related to our data:
- What was the best month for sales?
- What city sold the most product?
- When is good time to advertise?
- What products are most often sold together?
- What products sold the most, and why?
