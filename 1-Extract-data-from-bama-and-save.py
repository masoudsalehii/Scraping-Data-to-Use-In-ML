import requests
from bs4 import BeautifulSoup
import re
from sklearn import tree
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd",
  database="bama"
)




for i in range(10):

    r = requests.get("https://bama.ir/car/pride/all-models/all-trims?province=tehran&company=saipa&body=passenger-car&manucountryid=9&page=%d" % i)
    soup = BeautifulSoup(r.text, 'html.parser')
    link_soup = BeautifulSoup(r.content, 'html.parser')
    element_for_loop = soup.find_all("li", attrs={"class": "car-list-item-li list-data-main"})
    model = soup.find_all("span", attrs={"itemprop": "releaseDate"})
    karkard = soup.find_all("div", attrs={"class": "car-func-details"})
    links = soup.find_all('a', attrs={"itemprop": "url"})
    print("Page : ", i+1)
    str_regex = r"(\d*\,*\d+\,*\d+)"
    cars = []
    X_ML = []
    Y_ML = []
    for car in range(len(element_for_loop)):
            Car_Arrey = []
            x = re.findall(str_regex, karkard[car].text)
            if x == []:
                y = None
            else:
                y = int((x[0]).replace(",", ""))

            Car_Arrey.append(int(model[car].text))
            Car_Arrey.append(y)
            web = requests.get(links[car].get("href"))
            soup_car_link = BeautifulSoup(web.text, 'html.parser')

            try:
                val_price = int(soup_car_link.find("span", {"style": "color: #333;"})['content'].replace(',', ''))
            except:
                val_price = None
            Car_Arrey.append(val_price)

            Car_Arrey.append(links[car].get("href"))
            cursor = mydb.cursor()
            cursor.execute("SELECT link FROM pride")
            myresult = cursor.fetchall()
            to_check_repeated = 0
            for i in myresult:
                if i[0] == links[car].get("href"):
                    to_check_repeated = 1
                    break

            if to_check_repeated == 0 and Car_Arrey[2] != None and Car_Arrey[1] != None:

                sql = "INSERT INTO pride (model, karkard,  price, link) VALUES (%s, %s, %s, %s)"
                val = (Car_Arrey[0], Car_Arrey[1], Car_Arrey[2], Car_Arrey[3])
                cursor.execute(sql, val)
                mydb.commit()



'''print(Car_Arrey)
                X_ML.append(Car_Arrey[0:2])
                Y_ML.append(Car_Arrey[2])



clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_ML, Y_ML)
new_data = [[1397, 12500]]
answer = clf.predict(new_data)
print(answer[0])
'''
