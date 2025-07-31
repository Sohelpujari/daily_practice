import pytest
from playwright.sync_api import sync_playwright,Browser,BrowserContext,Page


# Playwright for api
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    request = context.request
    url = ""
    headders = ""
    data = ""
    responce = request.post(url=url,headers=headders,data=data)
    json = responce.json()
    code = json["response"]
    assert "200" == responce.status

#play wright UI
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("give the link")
    page.locator("give user id locater").wait_for(state="visible")
    page.locator("give user id locater").fill("userID")
    page.locator("give paw id locater").wait_for(state="visible")
    page.locator("give paw id locater").fill("pasw")
    page.locator("give login butten locater").click()



# Pytest and POM
class Login:

    _inp_user = "locater of user"
    _inp_pas = "locater of pass"
    _btn_login = "loacter of login btn"

    def __init__(self, page:Page):
        self.page = page

    def login_page(self, user_name, password):
        self.page.locator(self._inp_pas).fill(user_name)

        self.page.locator(self._inp_pas).fill(password)
        self.page.locator(self._btn_login).click()


#pytes
class Test:

    @pytest.fixture()
    def setup(self,page:Page):
        self.page = page
        self.user_name = ""
        self.password = ""
    def test_login(self):
        login = Login(self.page)
        login.login_page(self.user_name,self.password)



#conftest.py and fixture
@pytest.fixture(scope="session")
def playwright_instants():
    with sync_playwright() as playwright:
        yield playwright

def browser(playwright_instants):
    browser : Browser = playwright_instants.chromium.launch(headless=False)
    yield browser
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png")
        print(f"\n[Screenshot Taken] Test failed: {request.node.name}")
    browser.close()

@pytest.fixture(scope="function")
def context(browser:Browser):
    context : BrowserContext = browser.new_context()

    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context:BrowserContext):
    page:Page = context.new_page()
    yield page