import requests
from bs4 import BeautifulSoup as bs
import random

def get_free_proxy_list():
    url = "https://free-proxy-list.net/"
    soup = bs(requests.get(url).content, "html.parser")
    
    proxies = [str(tr.find_all("td")[0].text.strip()) + ":" + str(tr.find_all("td")[1].text.strip()) 
               for tr in soup.find('tbody').find_all('tr')]
    
    return proxies
    
def get_random_proxy():
    proxy = random.choice(get_free_proxy_list())
    
    return proxy

print(get_random_proxy())

# def is_proxy_working(proxy, url):
#     try:
#         # Configure Chrome WebDriver to use the proxy
#         chrome_options = webdriver.ChromeOptions() 
#         chrome_options.add_argument(f"--proxy-server={proxy}")

#         # Initialize the WebDriver with the proxy settings
#         driver = webdriver.Chrome(options=chrome_options)

#         # Open the target URL
#         driver.get(url)

#         # Give the page some time to load
#         time.sleep(3)

#         # Get the body text to see the response
#         body_text = driver.find_element(By.TAG_NAME, "body").text

#         # Check if the response contains the expected proxy IP address
#         print(f"Proxy {proxy}: Response from {url} -> {body_text}")
        
#         driver.quit()

#         # Return True if the proxy is working, else False
#         if proxy.split(":")[0] in body_text:
#             return True
#         return False

#     except Exception as e:
#         print(f"Proxy {proxy} failed: {e}")
#         return False

# def main():
#     url = "https://httpbin.org/ip" # this website returns the ip address of the request
#     proxy_list = get_free_proxy_list()
    
#     for proxy in proxy_list[:10]:
#         print(f"Trying proxy: {proxy}")
#         if is_proxy_working(proxy, url):
#             print(f"Proxy {proxy} is working!")
#             break  # Exit once a working proxy is found
#         else:
#             print(f"Proxy {proxy} is not working. Trying the next one...")
    
# main()