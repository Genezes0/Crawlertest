from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import deephelpers
import deeploop

def main():
    options, driver = deephelpers.setup_tor_browser()

    result_file = "results.txt"
    deephelpers.create_or_clear_file(result_file)

    try:
        while True:
            search_query = input("Enter your search query (type 'exit' to stop): ")
            if search_query.lower() == "exit":
                break

            deeploop.search_and_extract_links(driver, search_query, result_file)

    except KeyboardInterrupt:
        print("Search loop stopped by user.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
