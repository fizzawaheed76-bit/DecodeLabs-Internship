# Project 3 - AI Recommendation System

movies = {
    "Inception": ["Sci-Fi", "Thriller"],
    "The Dark Knight": ["Action", "Crime"],
    "Interstellar": ["Sci-Fi", "Drama"],
    "Toy Story": ["Animation", "Comedy"],
    "Avengers": ["Action", "Sci-Fi"],
    "The Conjuring": ["Horror", "Thriller"],
    "Titanic": ["Romance", "Drama"],
    "Jumanji": ["Adventure", "Comedy"],

    # More Movies
    "Iron Man": ["Action", "Sci-Fi"],
    "Spider-Man": ["Action", "Adventure"],
    "Black Panther": ["Action", "Adventure"],
    "Doctor Strange": ["Action", "Fantasy"],
    "Guardians of the Galaxy": ["Action", "Sci-Fi"],
    "Jurassic Park": ["Adventure", "Sci-Fi"],
    "Avatar": ["Action", "Sci-Fi"],
    "The Matrix": ["Sci-Fi", "Action"],
    "Mission Impossible": ["Action", "Thriller"],
    "John Wick": ["Action", "Crime"],
    "The Hangover": ["Comedy"],
    "Home Alone": ["Comedy", "Family"],
    "Finding Nemo": ["Animation", "Adventure"],
    "Frozen": ["Animation", "Romance"],
    "The Lion King": ["Animation", "Drama"],
    "The Notebook": ["Romance", "Drama"],
    "La La Land": ["Romance", "Drama"],
    "It": ["Horror", "Thriller"],
    "A Quiet Place": ["Horror", "Thriller"],
    "The Pursuit of Happyness": ["Drama"],
    "Forrest Gump": ["Drama", "Romance"],
    "Pirates of the Caribbean": ["Adventure", "Action"],
    "The Hobbit": ["Adventure", "Fantasy"]
}


print("===================================")
print("     MOVIE RECOMMENDATION SYSTEM")
print("===================================")


genres = [
    "Action",
    "Sci-Fi",
    "Comedy",
    "Horror",
    "Romance",
    "Drama",
    "Adventure",
    "Animation",
    "Thriller",
    "Crime",
    "Fantasy",
    "Family"
]


# Continuous search
while True:

    print("\nAvailable Genres:")

    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre}")

    choice = input(
        "\nEnter your favorite genre "
        "(or type 'exit' to quit): "
    ).strip().lower()


    # Exit
    if choice == "exit":
        print("\nThank you for using Movie Recommendation System! 🎬")
        break


    recommendations = []


    # Find matching movies
    for movie, movie_genres in movies.items():

        for genre in movie_genres:

            if genre.lower() == choice:

                recommendations.append(movie)

                break


    # Display recommendations
    if recommendations:

        print("\n🎬 Recommended Movies:")

        for movie in recommendations:
            print("•", movie)

    else:

        print("\n❌ No matching movies found.")


    # Ask if user wants another search
    again = input(
        "\nDo you want to search another genre? (yes/no): "
    ).strip().lower()


    if again != "yes":

        print("\nThank you for using Movie Recommendation System! 🎬")
        break