# Team-Project-19

## Topic 1 - Chess Opening Recommender 

### Introduction
With the recent quarantine, there has been a massive chess boom as a result of people having more free time and taking to the internet for fun pastimes. We propose a chess opening recommender system that will give anyone who has a keen interest to improve in chess the best openings to use for them at their current skill level.

### Abstract
At the core, we will be analyzing various chess data/databases to understand the best particular openings at each rating range. The system will then collect user input such as their current rating (or skill level) and the pieces desired (white/black) so that the system can recommend the top 3 openings to the user that would statistically be the best for their current rating. As the user improves in rating, they can keep using the system to receive new opening recommendations and keep improving their chess knowledge and skill.

### Approach
First, we will be analyzing various chess data/databases to understand the best particular openings at each rating range. This will involve a lot of data processing and analysis, and could either be a rule-based process or ML based process (undecided at this time). 

Next, the system will then collect user input. The input will include their current rating (or skill level), the pieces desired (white/black), and possibly other fields (such as perhaps how unique the user wants to be with their opening style) to make the recommendations more interesting. The system will then recommend the top 3 openings to the user that would statistically be the best for their current rating.  

Furthermore, with the user understanding the particular openings they should focus on in order to improve, the system can then search up recent professional games of these particular recommended chess openings in which the player won and provide the games to the user for studying and analyzing purposes. 

### Persona
For any chess player, beginners or advanced.

The form that the system will take will perhaps be a web application.

### Possible Dataset links
https://www.kaggle.com/mysarahmadbhat/online-chess-games

https://www.kaggle.com/liury123/chess-game-from-12-top-players?select=game_data.csv

https://www.kaggle.com/milesh1/35-million-chess-games

https://www.chess.com/games

https://database.chessbase.com/

https://www.365chess.com/


## Topic 2 - Attendance System using Face Recognition

### Introduction
Instead of going through the tiring process of taking attendance during a class, it would get a lot easier for the schools and professors if the time taken for this activity was reduced by using some automation. By the result of automation, professors would get some more time to complete their respective syllabus. One of the ways automation can be carried out is by performing face recognition whenever students enter the classroom. In this way, time can be saved by automating the process of mechanically taking attendance in the classroom.

### Abstract
Face recognition can be implemented by getting data from a webcam on the entrance of a classroom. This expression can be captured and various machine learning techniques can be applied onto that data in order to recognize a particular student and mark his/her attendance. First of all, data needs to be collected so that a machine learning model can be trained on top of it. This data should consist of images of students in various expressions like anger, happy, sad, excited, fear, etc. to increase the accuracy of the recognition system. 

### Approach
After the data is collected, it would be ready to get trained into a machine learning model. Techniques like k Nearest Neighbour can be used in order to train the machine learning model on the expression data. The k Nearest Neighbor classifier gives diverse exactness of grouping for various mixes of preparing and testing dataset. Another way to implement face recognition is Support Vector Machine technique. The client might give a capacity, like a line, polynomial, or sigmoid bend, to the SVM, which chooses support vectors along the outer layer of this capacity.

### Persona
Different schools, offices, and universities can be considered as the target audience of this project.

### Possible Dataset links
https://www.kaggle.com/apollo2506/facial-recognition-dataset

## Topic 3 - Ingredients based Recipe Recommender

### Introduction
Almost two years into the pandemic, many cooks from home have come back with new recipes in their arsenal. Cooking sometimes is a problem for some people and hobby for some. However, you can always find tips and recipes for cooking. Being a novice in cooking, it is always a hard decision to decide what to eat for lunch or dinner. Sometimes faced with limited ingredients, it is always a time-consuming task to decide what to cook. So to solve this issue we propose a system that can recommend recipes based on interests and available ingredients.

### Abstract
At the core, we will be analyzing various recipes to understand the ingredients, recipes and cuisine. The system will then collect user input such as their available ingredients and the desired cuisine so that the system can recommend the top relevant recipes to the user based on their cooking expertise. As the user improves in cooking skills, they can be recommended complex recipes that would help them in trying new recipes.

### Approach
First, we will be collecting and analyzing various recipes to understand the attributes like names, ingredients and cuisines. We will have to re-process the recipes by using NLP techniques to drop unnecessary information and format the data.

Next, the system will collect user input. The input will include their current choice of cuisine, ingredients, course, etc. Then the system would suggest various recipes, similar ingredients and complementary ingredients provide users with the functionality of identifying substitutable ingredients and alternate recipes.

To suggest recipes we can use Term Frequency Inverse Document Frequency (TF-IDF) and Cosine Similarity to recommend the most similar recipes, we pass the results of the TF-IDF model for every recipe and use the similarities function - MatrixSimilarity, to get the cosine similarity between recipes. Also, we can use the Jaccard String Similarity model to compute the similarity of two recipe names based on the words. For all the recipes in the dataset, we can calculate the string similarity for each pair of recipes and stored the top 8 similar recommendations for each recipe in the Database.

For ingredient recommender for substitution in a recipe, as a first step, we check the related ingredient list obtained from the dataset. If a similar ingredient could not be found, then we could use the Word2Vec model to provide a substitute. However, more study is required to come up with an appropriate solution.

### Persona
Anyone who wants to cook can be considered as the target audience of this project.  
Amateur work from home professionals.  
Decent cooks with some cooking experience.

### Possible Dataset links
https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions

https://www.kaggle.com/kanishk307/6000-indian-food-recipes-dataset

https://www.kaggle.com/sarthak71/food-recipes

https://www.kaggle.com/sooryaprakash12/cleaned-indian-recipes-dataset

Scrap data from websites like BBC Food