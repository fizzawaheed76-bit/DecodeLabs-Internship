# 🎬 Project 3 - AI Recommendation System

## 📌 Project Overview

This project is part of the **DecodeLabs Internship** and demonstrates a
simple AI recommendation system based on user preferences.

The system asks the user to enter a favorite movie genre and matches
that preference with movie genres stored in the program. It then
displays matching movies.

## 🎯 Project Goal

The project demonstrates:

-   Taking user input
-   Matching user preferences with item attributes
-   Displaying recommended items
-   Allowing the user to search again
-   Exiting the program

## 🚀 Features

-   Movie recommendation system
-   Multiple movie genres
-   Genre-based pattern matching
-   Search for another genre
-   Exit option
-   Beginner-friendly Python logic

## 🎞️ Genres

-   Action
-   Sci-Fi
-   Comedy
-   Horror
-   Romance
-   Drama
-   Adventure
-   Animation
-   Thriller
-   Crime
-   Fantasy
-   Family

## 🎬 Movies Included

The system includes movies such as:

-   Inception
-   The Dark Knight
-   Interstellar
-   Toy Story
-   Avengers
-   The Conjuring
-   Titanic
-   Jumanji
-   Iron Man
-   Spider-Man
-   Black Panther
-   Doctor Strange
-   Guardians of the Galaxy
-   Jurassic Park
-   Avatar
-   The Matrix
-   Mission Impossible
-   John Wick
-   The Hangover
-   Home Alone
-   Finding Nemo
-   Frozen
-   The Lion King
-   The Notebook
-   La La Land
-   It
-   A Quiet Place
-   The Pursuit of Happyness
-   Forrest Gump
-   Pirates of the Caribbean
-   The Hobbit

## 🧠 How It Works

Each movie is stored with one or more genres.

``` python
"Inception": ["Sci-Fi", "Thriller"]
```

When the user enters a genre, the program checks each movie's genres. If
a matching genre is found, that movie is added to the recommendation
list.

``` text
User Preference
       ↓
Compare with Movie Genres
       ↓
Find Matching Movies
       ↓
Display Recommendations
```

## 🔄 Search Again

The program uses a `while` loop so the user can search for another
genre.

``` text
Do you want to search another genre? (yes/no): yes
```

Entering `yes` starts another search. Entering `no` ends the program.
The user can also type `exit` at the genre prompt.

## 🛠️ Technologies Used

-   Python
-   Dictionaries
-   Lists
-   `for` loops
-   `while` loop
-   `if / else`
-   User input
-   String methods
-   Pattern matching
-   Basic recommendation logic

## ▶️ How to Run

Make sure Python is installed.

Open the project in VS Code and run:

``` bash
python project3_recommendation.py
```

## 💻 Example

``` text
===================================
     MOVIE RECOMMENDATION SYSTEM
===================================

Available Genres:
1. Action
2. Sci-Fi
3. Comedy
4. Horror
5. Romance
...

Enter your favorite genre: action

🎬 Recommended Movies:
• The Dark Knight
• Avengers
• Iron Man
• Spider-Man

Do you want to search another genre? (yes/no): yes
```

## 📚 Skills Learned

-   Logic building
-   Pattern matching
-   User input handling
-   Dictionaries
-   Lists
-   Loops
-   Conditional statements
-   Basic recommendation concepts

## 🔮 Future Improvements

-   Allow users to select genres using numbers
-   Allow multiple genre preferences
-   Add recommendation scores
-   Sort movies by matching scores
-   Add movie ratings
-   Create a Gradio web interface
-   Add a larger movie dataset

## 👩‍💻 Project Information

**Internship:** DecodeLabs\
**Project:** Project 3 - AI Recommendation System\
**Topic:** Recommendation Logic / Pattern Matching
