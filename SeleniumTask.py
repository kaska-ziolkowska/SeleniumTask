from selenium import webdriver
import re

def is_a_browse_companies_link(href):
    return href and re.compile("emc/browse-companies/").search(href)

def is_a_company_link(href):
    return href and re.compile("emc/company/").search(href)

def extract_and_print_company_details():
    name = driver.find_element_by_tag_name("h1")
    details = driver.find_elements_by_class_name("gfdCompanyDetailsCol")
    logo = driver.find_element_by_class_name("img-responsive").get_attribute("src")
    f.write("<company>\n")
    f.write("<name>"+name.text.replace("&", "&amp;")+"</name>\n")
    for detail in details:
        f.write("<details>"+detail.text.replace("\n", " ").replace("&", "&amp;")+"</details>\n")
    f.write("<logo>"+logo+"</logo>\n")
    f.write("</company>\n")
    driver.execute_script("window.history.go(-1)")

def navigate_to_page(link):
	driver.find_element_by_link_text(link.text.rstrip()).click()

def select_companies():
    company_page_source = driver.page_source
    soup = BeautifulSoup(company_page_source, 'lxml')
    companies = soup.findAll(href = is_a_company_link)
    if len(companies) > 0:
        navigate_to_page(companies[0])
        extract_and_print_company_details()
        if len(companies) > 2:
            navigate_to_page(companies[2])
            extract_and_print_company_details()

# start webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.medicines.org.uk/emc/browse-companies")

# start Beautiful Soup
from bs4 import BeautifulSoup
browse_page_source = driver.page_source
soup = BeautifulSoup(browse_page_source, 'lxml')
links = soup.findAll(href = is_a_browse_companies_link)

# extract data into output file
f = open('output.xml', mode='wt', encoding='utf-8')
f.write("""<?xml version="1.0" encoding="UTF-8"?>\n""")
f.write("<companies>\n")
for link in links:
    navigate_to_page(link)
    select_companies()
f.write("</companies>")
f.close()
driver.quit()