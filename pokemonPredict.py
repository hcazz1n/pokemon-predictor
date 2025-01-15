import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib #has a method for saving and loading models

data = pandas.read_csv('pokemon.csv')
data.fillna('None', inplace=True)

# data.shape #returns the shape in (rows, columns)
# data.describe #describes the data in the dataset
# data.values #returns an array; each index corresponds to a row


#model has already been dumped and saved into a file, so lines 16-23 are not necessary anymore | only if the file is deleted will we use them again

# input = data.drop(columns=['Number','Name','Type1','Type2','Abilities','Generation']) #also standard to use X
# output = data.drop(columns=['UserAge','UserGender','Number','Name','Abilities','Generation']) #also standard to use y
# input_train, input_test, output_train, output_test = train_test_split(input, output, test_size=0.2) #test_size*100 = percent of data being used for testing. The remaining percent is being used for training the model.
#the more data the model is trained on, the more accurate it will be. the more complex the problem, the more data is necessary.

# model = DecisionTreeClassifier()
# model.fit(input_train, output_train)
#joblib.dump(model, 'pokemon-type-recommender.joblib') #use once to create the file

model = joblib.load('pokemon-type-recommender.joblib') #loads the model
predictions = model.predict([[40, 0]]) #this is the types of the pokemon that the model predicts a 40 year old woman would like
print(predictions)

