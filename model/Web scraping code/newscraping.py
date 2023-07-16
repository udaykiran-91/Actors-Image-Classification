import bs4
import requests
from selenium import webdriver
import os
import time

# creating a directory to save images
folder_name = "new anushka"
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)


def download_image(url, folder_name, num):

    # write image to file
    reponse = requests.get(url)
    if reponse.status_code == 200:
        with open(os.path.join(folder_name, str(num) + ".jpg"), "wb") as file:
            file.write(reponse.content)


chromePath = r"C:\Users\varun\Desktop\chromedriver.exe"
driver = webdriver.Chrome()

search_URL = "https://www.google.com/search?q=anushka+shetty+images&tbm=isch&sa=X&ved=2ahUKEwj-6oKO2r__AhX9amwGHdLuAYwQ0pQJegQIDRAB"
driver.get(search_URL)

# //*[@id="islrg"]/div[1]/div[1]
# //*[@id="islrg"]/div[1]/div[50]
# //*[@id="islrg"]/div[1]/div[25]
# //*[@id="islrg"]/div[1]/div[75]
# //*[@id="islrg"]/div[1]/div[350]


a = input("Waiting...")

# Scrolling all the way up
driver.execute_script("window.scrollTo(0, 0);")

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, "html.parser")
containers = pageSoup.findAll("div", {"class": "isv-r PNCib MSM1fd BUooTd"})


len_containers = len(containers)

print("no.of container found: " + str(len_containers))


# //*[@id="islrg"]/div[1]/div[3]

from selenium.webdriver.common.by import By

for i in range(1, 49):
    if i % 25 == 0:
        continue
    xPath = '//*[@id="islrg"]/div[1]/div[' + str(i) + "]"

    # //*[@id="islrg"]/div[1]/div[5]/a[1]/div[1]/img
    # //*[@id="islrg"]/div[1]/div[5]/a[1]/div[1]/img
    # //*[@id="islrg"]/div[1]/div[7]/a[1]/div[1]/img

    previewImageXPath = '//*[@id="islrg"]/div[1]/div[' + str(i) + "]/a[1]/div[1]/img"
    previewImageElement = driver.find_element(by=By.XPATH, value=previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src")

    driver.find_element(by=By.XPATH, value=xPath).click()
    print(i)
    timeStarted = time.time()

    while True:

        # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
        # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
        try:
            imageElement = driver.find_element(
                by=By.XPATH,
                value="""//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]""",
            )
            imageURL = imageElement.get_attribute("src")

            if imageURL != previewImageURL:
                # print("actual URL", imageURL)
                break
            else:
                # making a timeout if the full res image can't be loaded
                currentTime = time.time()

                if currentTime - timeStarted > 10:
                    print(
                        "Timeout! Will download a lower resolution image and move onto the next one"
                    )
                    break

        except:
            print(
                "Couldn't download an image %s, continuing downloading the next one"
                % (i)
            )
            break

    try:
        download_image(imageURL, folder_name, i)
        print(
            "Downloaded element %s out of %s total. URL: %s"
            % (i, len_containers + 1, imageURL)
        )
    except:
        print(
            "Couldn't download an image %s, continuing downloading the next one" % (i)
        )


for i in range(51, 104):
    if i % 25 == 0:
        continue
    xPath = '//*[@id="islrg"]/div[1]/div[51]/div[' + str(i - 50) + "]"

    # //*[@id="islrg"]/div[1]/div[51]/div[1]/a[1]/div[1]/img
    # //*[@id="islrg"]/div[1]/div[51]/div[2]/a[1]/div[1]/img
    # //*[@id="islrg"]/div[1]/div[51]/div[50]

    previewImageXPath = (
        '//*[@id="islrg"]/div[1]/div[51]/div[' + str(i - 50) + "]/a[1]/div[1]/img"
    )
    previewImageElement = driver.find_element(by=By.XPATH, value=previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src")

    driver.find_element(by=By.XPATH, value=xPath).click()
    print(i)
    timeStarted = time.time()

    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[2]

    while True:
        try:
            imageElement = driver.find_element(
                by=By.XPATH,
                value="""//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]""",
            )
            imageURL = imageElement.get_attribute("src")

            if imageURL != previewImageURL:
                # print("actual URL", imageURL)
                break
            else:
                # making a timeout if the full res image can't be loaded
                currentTime = time.time()

                if currentTime - timeStarted > 10:
                    print(
                        "Timeout! Will download a lower resolution image and move onto the next one"
                    )
                    break
        except:
            print(
                "Couldn't download an image %s, continuing downloading the next one"
                % (i)
            )
            break

    try:
        download_image(imageURL, folder_name, i)
        print(
            "Downloaded element %s out of %s total. URL: %s"
            % (i, len_containers + 1, imageURL)
        )
    except:
        print(
            "Couldn't download an image %s, continuing downloading the next one" % (i)
        )


##
##

for i in range(105, 208):
    if i % 25 == 0:
        continue
    xPath = '//*[@id="islrg"]/div[1]/div[52]/div[' + str(i - 104) + "]"

    # //*[@id="islrg"]/div[1]/div[51]/div[52]
    # //*[@id="islrg"]/div[1]/div[52]/div[1]
    # //*[@id="islrg"]/div[1]/div[52]/div[2]
    # //*[@id="islrg"]/div[1]/div[52]/div[3]
    # //*[@id="islrg"]/div[1]/div[52]/div[10]
    # //*[@id="islrg"]/div[1]/div[52]/div[20]
    # //*[@id="islrg"]/div[1]/div[52]/div[95]/a[1]/div[1]/img
    # //*[@id="islrg"]/div[1]/div[52]/div[79]/a[1]/div[1]/img

    previewImageXPath = (
        '//*[@id="islrg"]/div[1]/div[52]/div[' + str(i - 104) + "]/a[1]/div[1]/img"
    )
    previewImageElement = driver.find_element(by=By.XPATH, value=previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src")

    driver.find_element(by=By.XPATH, value=xPath).click()
    print(i)
    timeStarted = time.time()

    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[2]
    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
    #

    while True:
        try:
            imageElement = driver.find_element(
                by=By.XPATH,
                value="""//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]""",
            )
            imageURL = imageElement.get_attribute("src")

            if imageURL != previewImageURL:
                # print("actual URL", imageURL)
                break
            else:
                # making a timeout if the full res image can't be loaded
                currentTime = time.time()

                if currentTime - timeStarted > 10:
                    print(
                        "Timeout! Will download a lower resolution image and move onto the next one"
                    )
                    break
        except:
            print(
                "Couldn't download an image %s, continuing downloading the next one"
                % (i)
            )

    try:
        download_image(imageURL, folder_name, i)
        print(
            "Downloaded element %s out of %s total. URL: %s"
            % (i, len_containers + 1, imageURL)
        )
    except:
        print(
            "Couldn't download an image %s, continuing downloading the next one" % (i)
        )


a = input("Waiting again...")
driver.execute_script("window.scrollTo(0, 0);")
