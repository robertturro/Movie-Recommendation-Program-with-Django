# Movie-Recommendation-Program-with-Django
A Django Program where a user enters his/her favorite movie and the release year and gets recommended another movie

For this project I made a movie recommendation app that takes a movie title and a release year as input and outputs a similar movie. The algorithm for the recommendation process follows a rule based approach. I tried various other methods such as kmeans clustering and found that given the data I had access to a rules based method was the best to go. I got the original dataset from Kaggle.com and it consists of around 300,000 different movies from various years and various countries. The dataset also includes features such as the popularity of each movie, the IMDB average ratings and number of ratings, the release date, the original language, the genre, and an overview of the movie. I decided to recommend movies based on genre, language, release year, and popularity. Since many movies have many different genres I decided to limit the number of genres for each movie to two in order to prevent very popular movies with many genres being recommended the majority of the time. I then converted the movie dataset into a dictionary and pickled it so that it may be quickly loaded and the Django program may run faster. 
Once a user inputs a movie title and release date the program finds the movie and its index within the movie data dictionary. If the movie title cannot be found or if the release date is incorrect the program will output “Movie Not Found. Make Sure Spelling And Release Date Are Correct”. The release date of the movie is needed because there are many movies with the same title, the release date helps ensure that the correct movie is found within the movie dictionary. Once the movie index is found the genres and original language of the movie are also found. 
Next the program begins the rules based approach of recommending a movie. All movies with the same genre as the input movie are found and stored in a list. Then the movies are filtered based on the release year in which movies with a similar release year are added to a second list. Next the movies are filtered on language in which only the movies with the same original language are added to a third list. Lastly the remaining movies are added to a dictionary and sorted by popularity. The movie with the highest popularity, given it is not the input movie, is returned to the user along with an overview of the movie.
