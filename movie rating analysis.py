import pandas as pd
import numpy as np

# Movie dataset
data = {
    "Movie": ["Avatar", "Inception", "Titanic", "Interstellar", "Joker", "Dangal"],
    "Rating": [8.5, 8.8, 7.9, 8.6, 8.4, 8.3],
    "Year": [2009, 2010, 1997, 2014, 2019, 2016],
    "Views": [95, 88, 92, 85, 90, 80]
}

df = pd.DataFrame(data)

print("Movie Dataset:")
print(df)

# Average rating
average_rating = np.mean(df["Rating"])

# Highest rated movie
highest = df.loc[df["Rating"].idxmax()]

# Most viewed movie
most_viewed = df.loc[df["Views"].idxmax()]

# Movies rated above average
above_average = df[df["Rating"] > average_rating]

print("\nAverage Rating:", round(average_rating, 2))

print("\nHighest Rated Movie:")
print(highest["Movie"], "-", highest["Rating"])

print("\nMost Viewed Movie:")
print(most_viewed["Movie"], "-", most_viewed["Views"], "million views")

print("\nMovies Above Average Rating:")
print(above_average[["Movie", "Rating"]])