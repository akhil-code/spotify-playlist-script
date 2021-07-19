from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# timeouts
search_page_wait_time = 1
add_to_library_wait_time = 1

window_close_time_after_execution = 100

# files
songs_list_file = "C:/Users/guttu/Desktop/songs.txt"
failed_songs_file = "C:/Users/guttu/Desktop/failed_songs.txt"

# Chrome driver
chrome_driver_executable = "C:/Users/guttu/Desktop/chromedriver.exe"
chrome_driver_address = "localhost:9222"

# URLs
song_search_prefix_url = "https://open.spotify.com/search/"

# css selectors
like_button_css_selector = '#searchPage > div > div > section._7bf1862b8e096cebdaf4acbcfbec2d4e-scss > div._5aac821edb25f0e281f50522021abbe4-scss > div > div > div > div:nth-child(2) > div:nth-child(1) > div > div.b9f411c6b990949776c8edf3daeb26ad-scss > button._07bed3a434fa59aa1852a431bf2e19cb-scss.d12d20a78fbc13787860287d10063d04-scss'


def search_song(driver, song):
    # Search for the song
    query_string =  song_search_prefix_url + song
    # print('querying with query string: ' + query_string)
    driver.get(query_string)
    sleep(search_page_wait_time)

def like_song(driver):
    like_button = driver.find_element_by_css_selector(like_button_css_selector)
    like_button.click()
    sleep(add_to_library_wait_time)


def execute_transfer(driver):
    songs_list = open(songs_list_file, mode="r",  encoding="mbcs")
    failed_songs = open(failed_songs_file, "w")
    for song in songs_list:
        try:
            search_song(driver, song)
            like_song(driver)
        except:
            print("Unable to like the song" + song)
            failed_songs.write(song)

    songs_list.close()
    failed_songs.close()


def init_chrome_driver():
    # options to open in debugging mode
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", chrome_driver_address)
    driver = webdriver.Chrome(executable_path=chrome_driver_executable,options=chrome_options)
    print("chrome driver started")
    return driver


# opening spotify site
chrome_driver = init_chrome_driver()
execute_transfer(chrome_driver)

# Hold the window for sometime
sleep(window_close_time_after_execution)
chrome_driver.close()
