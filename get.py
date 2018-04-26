#-*- coding: utf-8 -*-

""" Python 抓圖範例 1，可以使用 """
# import urllib

# urllib.urlretrieve("http://www.xxx.tv/mediaPic/149990_v.jpg", "local-filename.jpg")

""" Python 抓圖範例 2，可以使用 """
# import csv
# import requests
 
# url="http://www.xxx.tv/mediaPic/149990_v.jpg"
# result = requests.get(url, stream=True)
# filename = "001.jpg"
# if result.status_code == 200:
#     image = result.raw.read()
#     open(filename,"wb").write(image)

""" Python 抓圖範例 3，可以使用 """
import csv
import requests
import time

with open('./csv/actress.csv') as csvfile:
    csvrows = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvrows:
        for col in row:
            if col:
                time.sleep(1)
                filename = col[col.rfind("/")+1:]
                url = col
                print(col)
                result = requests.get(url, stream=True)
                if result.status_code == 200:
                    image = result.raw.read()
                    open("./photos/" + filename,"wb").write(image)
