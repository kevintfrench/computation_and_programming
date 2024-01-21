# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV 
netflix_df = pd.read_csv("netflix_data.csv")

# Filter to movies
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter to relevant columns
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# Filter to less than 60 minutes
short_movies = netflix_movies[netflix_movies.duration < 60]

# Define an empty list (I don't recall this from class)
colors = []

# Provide genre colors
for label, row in netflix_movies.iterrows() :
    if row["genre"] == "Children" :
        colors.append("red")
    elif row["genre"] == "Documentaries" :
        colors.append("blue")
    elif row["genre"] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")
        
# Check first 10     
colors[:10]

# Gave up on the remainder.  Set the figure style and initalize a new figure
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)

# Create a title and axis labels
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()

# Are we certain that movies are getting shorter?
answer = "no"
