from sklearn.linear_model import LinearRegression
hours=[[3],[4],[5],[6],[7]]
marks=[20,30,40,50,60]
model=LinearRegression()
model.fit(hours,marks)
print("Predicted Marks for 8 hours is : ",model.predict([[8]]))