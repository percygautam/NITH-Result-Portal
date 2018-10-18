# NITH-Result-Portal 

This is a simple Data Mining project based on web automation using selenium supported by interactive GUI.
This will provide an easy way for students to view their CGPI, SGPI and class rank in an interactive format, also supported with 'compare' feature.
Database till results even semester 2018 has already been created as database1.txt. If you want to create again use dataextractor.py file to create another database. Please notice that it requires uninterrupted and fast internet connection for database creation.

Selenium is used mainly for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) be automated as well.
Selenium has the support of some of the largest browser vendors who have taken (or are taking) steps to make Selenium a native part of their browser. It is also the core technology in countless other browser automation tools, APIs and frameworks.

# Features!

  - Know your result in an interactive manner providing your progress over past semesters along with your current class rank.
  - Compare your progress with other students of same year semester-wise. 

  
### Requirements

* [Python 3+](https://www.python.org/download/releases/3.0/?) - Pyhton 3.6+ verion
* [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium for web automation
* [Kivy](https://kivy.org/doc/stable/) - for GUI
*  Data visualisation libraries such as Seaborn and Matplotlib.
*  Data processing library - Pandas

### Installation

Step 1: Install all the libraries using overall.sh file or separately
```sh
$ sh overall.sh
```

Step 2: Selenium requires a driver to interface with the chosen browser.
> For [Click for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
> For [Click for FireFox](https://github.com/mozilla/geckodriver/releases)
> For [Click for safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10)

Step 3: Extract the downloaded driver onto a project folder and enter the path to driver in dataextractor.py file.

Step 4: Set path variable to the environment. Paste this command to the terminal
```sh
$ export PATH=$PATH:/home/path/to/the/driver/folder/ # optional if error occurs
```
Step 5: run details.py using Python3
```sh
$ python3 details.py
```
Step 6: Enter the name of the group and the participants you want to add in that group, then press Submit

Step 7: When the browser is opened web.whatsapp.com will be opened and will ask to scan a QR code when you it first time

Step 8: After Scanning the QR code, you will be asked to press Enter Key in the terminal.

### Note

Compare feature doesn't work with inter-year comparisions and cuurently it only works for CGPI comparisions.
It requires uninterrupted and fast internet connection for database creation using dataextractor.py
The dataextractor.py file needs to be modified according to semester and branches if changed in coming years.
