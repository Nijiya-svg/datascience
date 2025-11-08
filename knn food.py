import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

food=pd.read_csv("food_data.csv")

x=food[["Sweetness","Crunchiness"]]
y=food["FoodType"]

scaler=MinMaxScaler()
x_scaled=scaler.fit_transform(x)

tomato=pd.DataFrame({"Sweetness":[3],"Crunchiness":[2]})
tomato_scaled=scaler.transform(tomato)

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_scaled,y)

prediction=knn.predict(tomato_scaled)
print("the predict food type of tomato is:",prediction[0])