from sklearn import tree
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd",
  database="bama"
)
cursor = mydb.cursor()
cursor.execute("SELECT model,karkard,price FROM pride")
my_data = cursor.fetchall()
print(my_data)
x = []
y = []
for car in my_data:
    x.append(car[0:2])
    y.append(car[2])
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
new_data = [[1397, 12500]]
answer = clf.predict(new_data)
print(answer[0])
