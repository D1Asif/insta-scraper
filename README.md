# Insta Scraper
This is an instagram scraper. The scraper logs in with instagram username and password and then searches the keywords in the search input box. Upon search result, the scraper scrolls through and collect the image urls. Finally exports the images to a csv file.

## Technologies
Python, Selenium, Pandas etc

## How to run
> Warning: Scraping too much may lead to your account ban by Instagram!

create a virtual enviroment using the followig commands:
```
virtualenv myenv # this will create a virtual environment named myenv
```
activate virutal environment:
```
.\myenv\Scripts\activate
```
install the dependencies with the following command:
```
pip install -r requirements.txt
```
Create a .env file in the root
```
INSTA_USERNAME=<Your Insta Username>
INSTA_PASSWORD=<Your Insta Password>
```
Finally run the command:
```
python app.py
```
