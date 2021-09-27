from selenium import webdriver

chrome_driver_path = "/Users/tomoyukieguchi/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

upcoming_events = {}
driver.get("https://www.python.org/")
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

for n in range(len(event_times)):
    upcoming_events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(upcoming_events)

# driver.close()
driver.quit()