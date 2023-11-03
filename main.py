""""
Importing necessary libraries:
"""

import pandas as pd
import matplotlib.pyplot as plt


def linebreak():
    print("\n\n")


def linebreak_single():
    print()


# Setting labels for y-axis of scatter plots

values = []

for i in range(0, 290 + 1, 10):
    values.append(i)
print("values for y-axis of scatter plots: ", values)

y_scale = values

linebreak_single()


# Task 1 #
"""Netflix! What started in 1997 as a DVD rental service has since exploded into the largest entertainment/media company
by market capitalization, boasting over 200 million subscribers as of January 2021. Given the large number of movies and
series available on the platform, it is a perfect opportunity to flex our data manipulation skills and dive into the
entertainment industry. Our friend has also been brushing up on their Python skills and has taken a first crack at a CSV
file containing Netflix data. For their first order of business, they have been performing some analyses, and they 
believe that the average duration of movies has been declining. As evidence of this, they have provided us with the 
following information:

For the years from 2011 to 2020, the average movie durations are 103, 101, 99, 100, 100, 95, 95,
96, 93, and 90, respectively. If we're going to be working with this data, we know a good place to start would be to 
probably start working with pandas. But first we'll need to create a dictionary from scratch and convert it to a
Pandas DataFrame!"""

# Years:
years = list(range(2011, 2021))
print("Years: ", years)

# Duration:
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
print("Duration: ", durations)

# dictionary:
movie_dict = {"years": years,
              "durations": durations}
print("Movies: ", movie_dict)

linebreak()


# Task 2 #
"""
To convert our dictionary movie_dict to a pandas DataFrame, we will first need to import the library under its usual 
alias. We'll also want to inspect our DataFrame to ensure it was created correctly.
"""

durations_df = pd.DataFrame(movie_dict)
print("Durations DataFrame: \n")
print(durations_df)

linebreak()


# Task 3 #
"""
Alright, we now have a pandas DataFrame, the most common way to work with tabular data in Python. Now back to the task
at hand. We want to follow up on our friend's assertion that movie lengths have been decreasing over time. A great place
to start will be a visualization of the data. Given that the data is continuous, a line plot would be a good choice,
with the dates represented along the x-axis and the average length in minutes along the y-axis. This will allow us to
easily spot any trends in movie durations. There are many ways to visualize data in Python, but matplotlib.pyplot is one
 of the most common packages to do so.

Note: In order for us to correctly test your plot, you will need to initialize a matplotlib.pyplot Figure object. 
You can continue to create your plot as you have learned in Intermediate Python.
"""

fig = plt.figure(figsize=(10, 10))

line_plot = fig.add_subplot(111)

line_plot.plot(years, durations, label="movie length")
line_plot.scatter(years, durations)
line_plot.grid(True)
line_plot.set_title("Line Plot")
line_plot.set_xlabel("Release Years")
line_plot.set_ylabel("Durations")
line_plot.legend()

plt.title("Netflix Movie Durations 2011-2020")
plt.show()

linebreak()


# Task 4:

"""
Well, it looks like there is something to the idea that movie lengths have decreased over the past ten years! But
equipped only with our friend's aggregations, we're limited in the further explorations we can perform. There are a few
questions about this trend that we are currently unable to answer, including:

    1. What does this trend look like over a longer period of time?
    2. Is this explainable by something like the genre of entertainment?

Upon asking our friend for the original CSV they used to perform their analyses, they gladly oblige and send it. We now 
have access to the CSV file, available at the path "datasets/netflix_data.csv". Let's create another DataFrame, this 
time with all of the data. Given the length of our friend's data, printing the whole DataFrame is probably not a good 
idea, so we will inspect it by printing only the first five rows.
"""

netflix_df = pd.read_csv("datasets/netflix_data.csv")
netflix_df = pd.DataFrame(netflix_df)
print(netflix_df.iloc[0:5])

linebreak()


# Task 5:
"""
Okay, we have our data! Now we can dive in and start looking at movie lengths.

Or can we? Looking at the first five rows of our new DataFrame, we notice a column type. Scanning the column, it's clear
 there are also TV shows in the dataset! Moreover, the duration column we planned to use seems to represent different 
 values depending on whether the row is a movie or a show (perhaps the number of minutes versus the number of seasons)?

Fortunately, a DataFrame allows us to filter data quickly, and we can select rows where type is Movie. While we're at 
it, we don't need information from all of the columns, so let's create a new DataFrame netflix_movies containing only 
title, country, genre, release_year, and duration.

Let's put our data subsetting skills to work!
"""

netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]
print(netflix_df_movies_only)

linebreak_single()

netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year", "duration"]]
print(netflix_movies_col_subset.iloc[0:5])

linebreak()


# Task 6:
"""
Okay, now we're getting somewhere. We've read in the raw data, selected rows of movies, and have limited our DataFrame 
to our columns of interest. Let's try visualizing the data again to inspect the data over a longer range of time.

This time, we are no longer working with aggregates but instead with individual movies. A line plot is no longer a good
choice for our data, so let's try a scatter plot instead. We will again plot the year of release on the x-axis and the
movie duration on the y-axis.
"""

release_year = netflix_movies_col_subset["release_year"].tolist()
# release_year = sorted(release_year, reverse=True)
# release_year = sorted(release_year, reverse=False)
print(release_year)

duration = netflix_movies_col_subset["duration"].tolist()
duration = sorted(duration, reverse=True)
# duration = sorted(duration, reverse=False)
print(duration)

plt.style.use("ggplot")
fig = plt.figure(figsize=(12, 8))

scatter_plot = fig.add_subplot(111)

scatter_plot.scatter(release_year, duration, label="Movie Length", c="green")
scatter_plot.grid(True)
scatter_plot.set_title("Scatter Plot")
scatter_plot.set_xlabel("Release Years")
scatter_plot.set_yticks(y_scale)
scatter_plot.set_ylabel("Durations (min)")
scatter_plot.legend()

plt.title("Movie Duration by Year of Release")

plt.show()

linebreak()

# Task 7:
"""
This is already much more informative than the simple plot we created when our friend first gave us some data. We can 
also see that, while newer movies are overrepresented on the platform, many short movies have been released in the past 
two decades.

Upon further inspection, something else is going on. Some of these films are under an hour long! Let's filter our 
DataFrame for movies with a duration under 60 minutes and look at the genres. This might give us some insight into what 
is dragging down the average.
"""

# Task 7:
netflix_movies_col_subset.loc[:, "duration"] = netflix_movies_col_subset["duration"].astype(int)
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]
print(short_movies.iloc[0:20])
linebreak_single()
print("Full Short Movies:", short_movies)

linebreak()


# Task 8:
"""
Interesting! It looks as though many of the films that are under 60 minutes fall into genres such as 
"Action & Adventure", "Dramas", and "Documentaries". This is a logical result, as these types of films are probably 
often shorter than  90 minute Hollywood blockbuster.

We could eliminate these rows from our DataFrame and plot the values again. But another interesting way to explore the 
effect of these genres on our data would be to plot them, but mark them with a different color.

In Python, there are many ways to do this, but one fun way might be to use a loop to generate a list of colors based on 
the contents of the genre column. We can then pass this list to our plotting function in a later step to color all 
non-typical genres in a different color!
"""

colors = []

for index, row in netflix_movies_col_subset.iterrows():
    genre = row["genre"]

    if genre == "Children":
        colors.append("red")

    elif genre == "Documentaries":
        colors.append("blue")

    elif genre == "Stand-Up":
        colors.append("green")

    else:
        colors.append("purple")

print(colors[0:10])
print(colors)


# Task 9:
"""
Lovely looping! We now have a colors list that we can pass to our scatter plot, which should allow us to visually 
inspect whether these genres might be responsible for the decline in the average duration of movies.

This time, we'll also spruce up our plot with some additional axis labels and a new theme with plt.style.use().

"""
plt.style.use("ggplot")

fig = plt.figure(figsize=(12, 8))

scatter_plot = fig.add_subplot(111)
release_year = sorted(release_year, reverse=True)
scatter_plot.scatter(release_year, duration, label="Movie Length", c=colors)
scatter_plot.grid(True)
scatter_plot.set_title("Scatter Plot")
scatter_plot.set_xlabel("Release Years")
scatter_plot.set_yticks(y_scale)
scatter_plot.set_ylabel("Durations (min)")
scatter_plot.legend()

plt.title("Movie Duration by Year of Release")
plt.show()

linebreak()

# Task 10:

"""
Well, as we suspected, non-typical genres such as children's movies and documentaries are all clustered around the 
bottom half of the plot. But we can't know for certain until we perform additional analyses. 
"""

# Are we certain that movies are getting shorter?
are_movies_getting_shorter = """It has been observed through disorganized scatter plots that other than occasional 
fluctuations within some genres, durations of most movies experience slight increases the next year compared to the 
present."""

print(f"""Observation:\n{are_movies_getting_shorter}""")
