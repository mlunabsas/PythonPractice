from PageObjects.ParentPage import ParentPage
import pytest

class BaseTest:
    @pytest.fixture()
    def setUp(self):
        # print("setup")
        yield "resource"
        # print("teardown")
        ParentPage.close(ParentPage)
