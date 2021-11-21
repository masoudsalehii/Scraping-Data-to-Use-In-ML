# Scraping-Data-to-Use-In-ML

In the final project of the course "Advanced Python Programming", I scraped Bama website(https://bama.ir) to extract the mileage, year of production, and prices of an spicial car(according to the input). After saving this data in a MySQL DB, I used the scikit-learn library to predict the price of a new car.
The challenge of the project was with Web-Scraping. Because in this web site the prices of the some ads are blurred (due to the irrational price), and I wanted to have even this data imported in my DB. And I you could see in my code all prices are extracted.

This code has two parts:
In the first part I extract the data and save it into my local DB.
In the second part I use this data to predict a new car's price which we know its mileage and producation year. I used a scikit-learn library in this code.
