from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Information need to add
YOUR_COLLECTION_NAME = ""
YOUR_COLLECTION_ID = ""

# Read the movie list from file
with open("YOUR_MOVIE_LIST.txt", "r", encoding="utf-8") as file:
    movie_list = [line.strip() for line in file.readlines()]

# Collection name and ID
collection_name = YOUR_COLLECTION_NAME
collection_id = YOUR_COLLECTION_ID

# Selectors
ADD_TO_LIST_SELECTOR = "a.lnk-doulist-add"
TOP_100_MOVIES_SELECTOR = f"label[for='{collection_id}']"
SAVE_BUTTON_SELECTOR = "input.doulist_submit"

# Initialize browser
driver = webdriver.Chrome()
driver.get("https://www.douban.com/")

# Manual login
input("Please log in to Douban in the browser, then press Enter to continue...")

# Navigate to Douban Movies
driver.get("https://movie.douban.com/")

print(f"Ensure you have created a collection named '{collection_name}' on Douban.")
input("Press Enter to continue after confirming the collection exists...")

# Record successful and failed movies
success_count = 0
failed_movies = []

# Process each movie
for index, movie in enumerate(movie_list):
    print(f"Processing movie: {movie} ({index + 1}/{len(movie_list)})")
    try:
        search_box = driver.find_element(By.NAME, "search_text")
        search_box.clear()
        search_box.send_keys(movie)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        try:
            first_movie = driver.find_element(By.CSS_SELECTOR, ".title a")
            first_movie.click()
            time.sleep(3)

            try:
                add_to_list_button = driver.find_element(By.CSS_SELECTOR, ADD_TO_LIST_SELECTOR)
                driver.execute_script("arguments[0].click();", add_to_list_button)
                time.sleep(2)

                try:
                    wait = WebDriverWait(driver, 5)
                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".dui-dialog")))

                    try:
                        collection_option = wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, TOP_100_MOVIES_SELECTOR)))
                    except:
                        collection_option = wait.until(
                            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), '{collection_name}')]")))

                    driver.execute_script("arguments[0].click();", collection_option)

                    try:
                        save_button = wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, SAVE_BUTTON_SELECTOR)))
                        driver.execute_script("arguments[0].click();", save_button)
                        print(f"Movie '{movie}' has been added to the collection '{collection_name}'.")
                        success_count += 1
                        time.sleep(2)
                    except:
                        save_button = wait.until(
                            EC.element_to_be_clickable((By.XPATH, "//input[@value='Save']")))
                        driver.execute_script("arguments[0].click();", save_button)
                        print(
                            f"Movie '{movie}' has been added to the collection '{collection_name}' (alternative method).")
                        success_count += 1
                        time.sleep(2)
                except TimeoutException:
                    print("Timeout while waiting for collection selection popup.")
                    failed_movies.append(movie)
                except Exception as e:
                    print(f"Error selecting collection: {str(e)}")
                    failed_movies.append(movie)
            except NoSuchElementException:
                print(f"Movie '{movie}' does not have an 'Add to list' button available.")
                failed_movies.append(movie)

            driver.back()
            time.sleep(2)
        except NoSuchElementException:
            print(f"Movie '{movie}' not found in search results.")
            failed_movies.append(movie)
        except Exception as e:
            print(f"Error processing movie details page for '{movie}': {str(e)}")
            failed_movies.append(movie)
            driver.get("https://movie.douban.com/")
            time.sleep(2)
    except Exception as e:
        print(f"An error occurred while processing '{movie}': {str(e)}")
        failed_movies.append(movie)
        driver.get("https://movie.douban.com/")
        time.sleep(2)

# Completion report
print("\n===== Process Completion Report =====")
print(f"Successfully added: {success_count}/{len(movie_list)} movies.")

if failed_movies:
    print("Movies that failed to be added:")
    for i, failed_movie in enumerate(failed_movies):
        print(f"  {i + 1}. {failed_movie}")

    with open("failed_movies.txt", "w", encoding="utf-8") as f:
        for movie in failed_movies:
            f.write(f"{movie}\n")
    print("Failed movies list saved to 'failed_movies.txt'.")

# Close the browser
driver.quit()
