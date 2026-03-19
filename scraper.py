from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
import random

print("Booting up the Selenium WebDriver for eFinancialCareers...")

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

master_job_list = []

# THE PAGINATION LOOP: Let's scrape the first 5 pages
print("-----------------------------------")
print("Starting the multi-page scrape...")
print("-----------------------------------")

for page_num in range(1, 6):
    # Notice the &page= at the end of the URL
    url = f"https://www.efinancialcareers.com/search/?q=data%20analyst&page={page_num}"
    
    print(f"Navigating to Page {page_num}...")
    driver.get(url)
    
    # Human-like delay to let the page load and avoid bot detection
    sleep_time = random.uniform(5.0, 8.0)
    time.sleep(sleep_time)
    
    # Grab all links on this page
    all_links = driver.find_elements(By.TAG_NAME, "a")
    
    for link in all_links:
        try:
            href = link.get_attribute("href")
            title = link.text.strip()
            
            # -----------------------------------------
            # THE FILTERING LOGIC
            # -----------------------------------------
            
            # 1. Skip if link or title is empty
            if not href or not title:
                continue
                
            # 2. Skip "Action Buttons" that have the right URL but the wrong text
            junk_titles = ['apply now', 'save', 'save job', 'share']
            if title.lower() in junk_titles:
                continue
                
            # 3. THE GOLDEN RULE: Must contain '.id' in the URL to be a real job
            if ".id" not in href.lower():
                continue
                
            # If it survives the gauntlet, save it!
            job_dictionary = {
                "Job Title": title,
                "Job URL": href
            }
            master_job_list.append(job_dictionary)
                
        except:
            continue

driver.quit()
print(f"Browser closed. Extracted a raw total of {len(master_job_list)} jobs.")

print("Cleaning data and building the CSV...")
df = pd.DataFrame(master_job_list)

# We drop duplicates based on the URL. If a job appeared twice, we only keep one row.
df = df.drop_duplicates(subset=['Job URL'])

file_name = "efc_clean_job_links.csv"
df.to_csv(file_name, index=False)

print("-----------------------------------")
print(f"SUCCESS! Clean data saved to {file_name}.")
print(f"Total unique, validated jobs ready for analysis: {len(df)}")
print("-----------------------------------")