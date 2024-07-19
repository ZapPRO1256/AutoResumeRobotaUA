# Import all library's
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Driver settings
def init_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Use if you need to work without a graphical interface
    driver = webdriver.Chrome(options=options)
    return driver


def main():
    # Initializing the web driver
    driver = init_driver()
    try:
        # Reading data from a file
        data_list = []
        with open("data.txt", "r") as file:
            data_list = file.readlines()

        # Writing user login data to a variable
        temp_data = data_list[0].replace("\n", '').split("=")
        username = temp_data[1]

        # Writing user password data to a variable
        temp_data = data_list[1].replace("\n", '').split("=")
        password = temp_data[1]

        # Writing user time data to a variable
        temp_data = data_list[2].replace("\n", '').split("=")
        timer_update = int(temp_data[1])

        # Go to the login page
        driver.get('https://robota.ua/auth/login')
        print("Successful login on login menu")

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'otp-username')))
        print("Successful update login page")

        # Search and enter a login
        username_input = driver.find_element(By.ID, 'otp-username')
        username_input.send_keys(username)
        print("Successful type username")

        # Search and enter a password
        input_css_selector = 'input[type="password"]'
        # Entering a delay due to the features of the site to find the password input field
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, input_css_selector)))
        print("Element password input found")
        # Enter password
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        password_input.send_keys(password)
        print("Successful type password")
        # Creating a delay for the correct operation of the program
        time.sleep(2)

        # Click on the login button, login to the account
        driver.find_element(By.TAG_NAME, 'santa-button').click()
        print("Successful login in profile")
        # Creating a delay for the correct operation of the program
        time.sleep(2)

        #  Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Let's go to the page with resumes
        driver.get('https://robota.ua/my/resumes')
        print("Page resumes found")

        #  Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'resume-title')))
        print("Resumes page load")

        # find the first Update resume button
        button_selector = 'button[class="additional-no-x-indent santa-block santa-typo-regular-bold"]'
        update_resume = driver.find_element(By.CSS_SELECTOR, button_selector)

        update_counter = 0  # CV update counter
        # A cycle for constantly updating resumes once every timer_update seconds
        while True:
            try:
                update_resume.click()
                update_counter += 1
                print(f"Resume updated - {update_counter}")
                time.sleep(timer_update)
            except Exception as e:
                print(f"Window are closed or except any error\n{e}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Closing the browser
        driver.quit()


if __name__ == "__main__":
    main()
