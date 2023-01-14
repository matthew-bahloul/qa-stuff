from playwright.sync_api import sync_playwright


def before_all(context):
    from playwright.sync_api import sync_playwright


    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")

def after_all(context):
    browser.close()
    playwright.stop()




def before_feature(context, feature):
    pass

def after_feature(context, feature):
    pass




def before_scenario(cotnext, scenario):
    pass


def after_scenario(context, scenario):
    pass