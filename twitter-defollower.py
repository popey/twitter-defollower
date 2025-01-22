from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (TimeoutException, 
    ElementClickInterceptedException, StaleElementReferenceException)
import time
import random

def human_like_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))

def random_sleep(min_seconds=2, max_seconds=4):
    time.sleep(random.uniform(min_seconds, max_seconds))

def scroll_to_element(driver, element):
    """Scroll element into middle of viewport"""
    driver.execute_script("""
        var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
        var elementTop = arguments[0].getBoundingClientRect().top;
        window.scrollBy(0, elementTop - (viewPortHeight / 2));
    """, element)
    random_sleep(1, 2)

def login_to_twitter(driver, username, password, email_or_phone):
    driver.get("https://x.com/i/flow/login")
    random_sleep(3, 5)
    
    try:
        # Wait for and fill in username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 
                'input[autocomplete="username"]'))
        )
        username_field.click()
        random_sleep()
        human_like_typing(username_field, username)
        random_sleep(1, 2)
        
        # Click Next after username
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 
                'button[style*="background-color: rgb(239, 243, 244)"] div[dir="ltr"] span span'))
        )
        next_button.click()
        random_sleep(2, 3)
        
        # Handle unusual activity check
        try:
            # Look for the email/phone input field
            verify_field = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 
                    'input[data-testid="ocfEnterTextTextInput"]'))
            )
            print("Additional verification required...")
            verify_field.click()
            random_sleep()
            human_like_typing(verify_field, email_or_phone)
            random_sleep(1, 2)
            
            # Click Next after email/phone
            verify_next = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 
                    'button[data-testid="ocfEnterTextNextButton"]'))
            )
            verify_next.click()
            random_sleep(2, 3)
        except TimeoutException:
            print("No additional verification required")
        
        # Wait for and fill in password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 
                'input[autocomplete="current-password"]'))
        )
        password_field.click()
        random_sleep()
        human_like_typing(password_field, password)
        random_sleep(1, 2)
        
        # Click Login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 
                'button[data-testid="LoginForm_Login_Button"]'))
        )
        login_button.click()
        random_sleep(5, 7)
        
        # Check if we're on the home page
        current_url = driver.current_url
        if "x.com/home" in current_url:
            print("Successfully logged in!")
            return True
        else:
            print(f"Login might have failed. Current URL: {current_url}")
            return False
            
    except TimeoutException as e:
        print(f"Login failed: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error during login: {str(e)}")
        return False
    
def remove_followers(username, password, email_or_phone):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"')
    chrome_options.add_argument('--force-device-scale-factor=0.75')
    
    driver = webdriver.Chrome(options=chrome_options)
    processed_count = 0
    batch_count = 0  # Counter for followers processed in current batch
    
    try:
        if not login_to_twitter(driver, username, password, email_or_phone):
            print("Failed to login, exiting...")
            return
            
        while True:  # Loop forever until manually stopped
            print("Loading followers page...")
            driver.get(f"https://x.com/{username}/followers")
            random_sleep(5, 7)
            
            try:
                # Find the More buttons within the followers list
                menu_buttons = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 
                        'button[aria-label="More"][aria-haspopup="menu"]'))
                )
                
                if not menu_buttons:
                    print("No followers found, might be done!")
                    break
                
                print(f"Found {len(menu_buttons)} followers to process")
                
                for button in menu_buttons:
                    try:
                        # Scroll button into view and click
                        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
                        random_sleep(1, 2)
                        
                        # Retry click up to 3 times
                        for attempt in range(3):
                            try:
                                button.click()
                                break
                            except (ElementClickInterceptedException, StaleElementReferenceException):
                                if attempt == 2:
                                    print("Failed to click menu button after 3 attempts, skipping...")
                                    continue
                                random_sleep(1, 2)
                                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
                        
                        random_sleep(1, 2)
                        
                        remove_option = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, 
                                'div[data-testid="removeFollower"]'))
                        )
                        remove_option.click()
                        random_sleep(1, 2)
                        
                        confirm_button = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, 
                                'button[data-testid="confirmationSheetConfirm"]'))
                        )
                        confirm_button.click()
                        
                        processed_count += 1
                        batch_count += 1
                        print(f"Successfully removed follower. Total processed: {processed_count}")
                        
                        random_sleep(2, 3)
                        
                        # Refresh page after every 10 followers
                        if batch_count >= 10:
                            print("Processed 10 followers, refreshing page...")
                            batch_count = 0  # Reset batch counter
                            break  # Break out of the button loop to refresh the page
                            
                    except TimeoutException:
                        print("Couldn't remove a follower, moving to next one")
                        continue
                    except Exception as e:
                        print(f"Error processing follower: {str(e)}")
                        continue
                
            except TimeoutException:
                print("Page took too long to respond, refreshing...")
                random_sleep(5, 7)
                continue
            except Exception as e:
                print(f"Unexpected error: {str(e)}")
                print("Refreshing page...")
                random_sleep(5, 7)
                continue
                
    finally:
        print(f"Script ending. Total followers processed: {processed_count}")
        driver.quit()

if __name__ == "__main__":
    username = "your_username"
    password = "your_password"
    email_or_phone = "your_email_address_or_phone"  # Add this for verification
    remove_followers(username, password, email_or_phone)
