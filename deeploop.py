from selenium.webdriver.common.keys import Keys
import deephelpers

def search_and_extract_links(driver, search_query, result_file):
    driver.get("http://example.onion")  # Página inicial da busca
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    while True:
        result_links = driver.find_elements_by_css_selector(".result a")
        for link in result_links:
            link_url = link.get_attribute("href")
            print(link_url)
            deephelpers.append_to_file(result_file, link_url)  # Adicionar o link ao arquivo
            driver.get(link_url)  # Acessar o link e buscar mais resultados

# Implement other functions if needed
