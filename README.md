# Video Recommendation System
## Preprocessing of Data
1.	Cleaned the data in excel to fit the data structure of the columns defined in the CSV
2.	Used pandas library to read the data from csv file converting the datatype from object to the corresponding data types and then make a data frame for each of the files.
3.	Merge the data from different dataframes to form the training dataset by joining them on the common Column ID
4.	Drop the duplicate values from the dataset
5.	Replace the categorical data like language into numerical form
6.	Transform the dataset into a normalized version
7.	Drop the features which may cause any imbalance, for example ‘Type’ in lecture had majority of Lectures as compared to Events or Debates etc.
8.	K-fold sampling is used to sample the data
9.	And, cross validation was used to split the given data into test and train sets

## Models Used:
•	Coding Language:Python
•	Library and Packages used while coding
i.	Numpy 
ii.	Pandas
iii.SKlearn
iv.	Math
v.	Matplotlib
vi.	scipy.spatial
vii.scipy.stats

•	Recommendation Systems do not impose a binary question of classifying a video to fall into one category or another also we do not have labeled information in the given dataset of any type thus this prediction system requires Unsupervised learning.
•	The system demands a certain number of similar outputs produced using the known data about the item popularity or similarity with others.
## The Models used to identify similar products were:
1.	K-Means Clustering to identify the cluster from where the closest points can be identified.
To understand the data points better, this approach was chosen. The challenge was to figure out K. To identify K , Elbow method was used and from the curve the best K value was seen as 2.
 

Tried K Values:K=5 and K=2
Before plotting the data was made more suited for it using the Principal Component Analysis, which is used to reduce dimensionality of the dataset. 
For K=2 the separation was more clear
 
2.	K-Nearest Neighbors:
a.	Although KNN is mostly used to classify the unseen data to the class most of the labelled instances belongs in the training dataset, I have implemented this for this dataset in a different way. Instead of using the predict attribute which defines the class label of the unseen data. I utilized the attribute to get the 30- nearest neighbors found for the unseen dataset. 
b.	The data found was later transformed into the Lecture ID in the Recommendation Array of 30 Videos for each instance in the test data set.
c.	Distance Matrix Used in the model: Euclidian distance
 
3.	Hybrid approach incorporating Correlation Matrix (using Linear Regression)
In this approach, I produced a co-relation matrix utilizing every Lecture ID x Lecture ID Matrix.
On the basis of features like Language, category, author ID a correlation matrix was generated using PearsonR distance Metric

## Pearson’s correlation:

Pearson's correlation coefficient when applied to a population is referred as the population correlation coefficient or the population Pearson correlation coefficient. The formula for Pearson’s R is:


The list was then sorted in an ascending order to get the closest points on the top and then 30 top most videos were chosen and saved in the recommendation Rank Matrix

## Error Metrics:
### A confusion matrix for Precision and Recall.
Precision can be defined as the ratio of correctly classified data points over total classified data points by the classifier i.e. True Positive/ (True Positive +False Positive).

### Recall 
Recall can be defined as the ratio of correctly classified data points over the total correct data points present in the dataset i.e. True Positive/ (True Positive +False Negative).

F1 is the harmonic mean of precision and recall, which tends towards the value which is smaller between the two. 

F1=2*(Precision*Recall/Precision + Recall)

### ROC Curves:
Roc curves shows a trade-off between False positive rate and true positive rate. Below is the image of a perfect classifier, there will be no mistakes. ROC curves are also very helful in comparing different models by comparing their AUC scores. AUC score of a model is the area under its ROC Curve. The greater the area the better a model performs.

