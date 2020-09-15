import allure


class TestSearch:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('第一步')
    def test_01(self):
        print('\n test001')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_02(self):
        print('\n test001')

    @allure.severity(allure.severity_level.NORMAL)
    def test_03(self):
        print('\n test001')

    @allure.severity(allure.severity_level.MINOR)
    def test_04(self):
        print('\n test001')

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_05(self):
        print('\n test001')
        assert False
