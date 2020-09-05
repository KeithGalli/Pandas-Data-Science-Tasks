# Pandas-Data-Science-Tasks
Set of real world data science tasks completed using the Python Pandas library.

## Setup

To access all of the files I recommend you fork this repo and then clone it locally. Instructions on how to do this can be found here: https://help.github.com/en/github/getting-started-with-github/fork-a-repo

The other option is to click the green "clone or download" button and then click "Download ZIP". You then should extract all of the files to the location you want to edit your code.

Installing Jupyter Notebook: https://jupyter.readthedocs.io/en/latest/install.html <br/>
Installing Pandas library: https://pandas.pydata.org/pandas-docs/stable/install.html 

## Background Information:

This repo goes with [my video](https://youtu.be/eMOA1pPVUc4) on "Solving real world data science videos with Python Pandas!". Here is some information on that video.

In this video we use Python Pandas & Python Matplotlib to analyze and answer business questions about 12 months worth of sales data. The data contains hundreds of thousands of electronics store purchases broken down by month, product type, cost, purchase address, etc. 

We start by cleaning our data. Tasks during this section include:
- Drop NaN values from DataFrame
- Removing rows based on a condition
- Change the type of columns (to_numeric, to_datetime, astype)

Once we have cleaned up our data a bit, we move the data exploration section. In this section we explore 5 high level business questions related to our data:
- What was the best month for sales? How much was earned that month?
- What city sold the most product?
- What time should we display advertisemens to maximize the likelihood of customer’s buying product?
- What products are most often sold together?
- What product sold the most? Why do you think it sold the most?

To answer these questions we walk through many different pandas & matplotlib methods. They include:
- Concatenating multiple csvs together to create a new DataFrame (pd.concat)
- Adding columns
- Parsing cells as strings to make new columns (.str)
- Using the .apply() method
- Using groupby to perform aggregate analysis
- Plotting bar charts and lines graphs to visualize our results
- Labeling our graphs

Check out the first video I did on Pandas: <br/>
https://youtu.be/vmEHCJofslg 

Check out the videos I did on Matplotlib: <br/>
https://youtu.be/DAQNHzOcO5A <br/>
https://youtu.be/0P7QnIQDBJY
