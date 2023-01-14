# Starting Point

## Make your own branch from here (DO NOT WORK ON THE "MAIN" BRANCH)

## python
Most important stuff:
- install python3.8
- set up a virtual enviroment and install requirements
- object oriented programming
- writing functions
- regular expressions using the re library

My recommendation for a good python foundation is [this udemy course](https://www.udemy.com/course/the-modern-python3-bootcamp/). It's pretty comprehensive, so it doesn't go by quickly.


## gherkin
Most important stuff:
- Write readable tests in gherkin
- Know when to use "Backgrounds" and "Scenario Outlines"
- Make steps resusable if possible

Gherkin is format for writing tests in a human-readable way. Look into what gherkin is and test writing conventions
- [link to gherkin documentation](https://cucumber.io/docs/gherkin/reference/)

## behave 
Behave is a tool used to run tests. look into behave setup, running tests by file, filepath, tags, etc

- [link to behave documentation](https://behave.readthedocs.io/en/stable/)

## playwright
understand what a browser driver is/does
look at playwright and how it works
- [link to playwright documentation](https://playwright.dev/python/docs/api/class-playwright)

## tools
Try to set this up to work with vscode and pycharm (community)
- [pycharm](https://www.jetbrains.com/pycharm/download)
- [vscode](https://code.visualstudio.com/download)
- 
## Extra stuff
- a very common interview question is [fizz buzz](https://www.geeksforgeeks.org/fizz-buzz-implementation/) and variations/extensions of it.


# Tasks
Write a tests in the `../features` directory of this repo and automate it. You should attempt the following:
1. Write a test to navigate to the google home page, then confirm that the url is "https://google.com"
2. Write a test that navigates to duckduckgo.com, searches for any search term you like, then click the first result
3. Write a test to go to this site "https://www.saucedemo.com". Pick a random username and password in the page footer to log in. After logging in, confirm that you reached the products page.
4. Log into "https://www.saucedemo.com", add any time to the cart. Then complete the checkout flow. Confirm that a success message is displayed.


## What to do for help
Create an issue in github, I'll get to it as soon as I can.