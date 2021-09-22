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

