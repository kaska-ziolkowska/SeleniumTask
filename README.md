# Selenium Web Scraping README

## Introduction
This is my first hands-on attempt on Selenium Webdriver on its own.
I did research on which language is most commonly used for Web Scraping task and chose Python. I have never used it before either.
Here is my best effort so far.

## What the application should be doing
Using Selenium WebDriver, controlled by a language of your choice:
1. Navigate to https://www.medicines.org.uk/emc/browse-companies
2. For each page of the company browser
- Capture details about the ﬁrst, the third and the last company on the page.
- The details must include the company name, the logo and all contact information. Do not capture the information about the drugs related to that company
- Store the logo as an image in a folder
- Add the company details to an internal data structure. Include the ﬁlename of the image ﬁle
3. Output the internal data structure of the company details as a Json ﬁle and also as an XML ﬁle
4. Share your code using GitHub or similar.

## What it is actually doing
1. Navigates to https://www.medicines.org.uk/emc/browse-companies
2. For each page of the company browser
- Captures details about the ﬁrst and the third company on the page.
- The details include the company name, the logo and all contact information. The information about the drugs related to that company are not captured.
- Logo is not stored in a folder, the url is saved instead.
- The company details are not added to an internal data structure.
3. The outputs of the company details are saved in an XML ﬁle. XML file is not well-structured but it passes the validation: https://www.w3schools.com/xml/ . JSON file is not created.
4. Code is shared on GitHub: https://github.com/kaska-ziolkowska/SeleniumTask.git

## Technologies
- Python 3
- Selenium
- ChromeDriver
- Beautiful Soup

## How to run the application
1. Download and install Python 3 from https://www.python.org/
2. Install Selenium using pip:
```sh
$ pip install -U selenium
```
3. Install Beautiful Soup using pip:
```sh
$ pip install beautifulsoup4
```
4. Open SeleniumTask directory in the command prompt.
5. Execute the file using Python:
```sh
$ python SeleniumTask.py
```