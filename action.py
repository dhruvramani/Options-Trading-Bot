from selenium import webdriver
import time
import pyautogui

profile = webdriver.FirefoxProfile()
profile.set_preference('dom.disable_beforeunload', True)
browser=webdriver.Firefox(profile)

def get_element_by_class_name(element):
	try:
		el=browser.find_element_by_class_name(element)
		return el
	except:
		time.sleep(3)
		print("Searching for element "+element)
		get_element_by_class_name(element)

def get_elements_by_class_name(element):
	try:
		el=browser.find_elements_by_class_name(element)
		return el
	except:
		time.sleep(3)
		print("Searching for element "+element)
		get_element_by_class_name(element)

def click(image):
	x, y = pyautogui.locateCenterOnScreen(image)
	pyautogui.click(x, y)

def init():
	browser.get("https://iqoption.com/traderoom")

def login(email,password):
	browser.get("https://iqoption.com/en/traderoom")
	get_element_by_class_name("Navbar__login").click()
	get_elements_by_class_name("iqInput")[0].send_keys(email)
	get_elements_by_class_name("iqInput")[1].send_keys(password)
	get_element_by_class_name("Button_success").click()	
	time.sleep(3)

def call():
	a=1
def put():
	a=2

login("mohit7rulez@gmail.com","Helloiamchubakabra@01")
init()
time.sleep(50)
click("change_amount.png")