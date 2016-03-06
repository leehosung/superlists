import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                print(cls.server_url)
                return
            super().setUpClass()
            cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Chrome('drivers/chrome')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retreive_it_later(self):
        # Edith 는 새로운 멋진 할일관리 싸이트에 대해서 들었습니다.
        # 홈페이지를 확인해 봅니다.
        self.browser.get(self.server_url)

        # 페이지의 제목이 할일관리인 것을 확인 합니다.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 바로 할일 항목을 입력 하도록 초대 받았습니다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # "Buy peacock feathers"를 할일 항목에 추가합니다.
        # (그녀의 취미는 루어 낚시 미끼를 매는 것입니다.)
        inputbox.send_keys('Buy peacock feathers')

        # 그녀가 엔터를 치면 페이지가 업데이트 되고 리스트에서
        # "1: Buy peacock feathers" 를 볼 수 있습니다.
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 여전히 텍스트 박스가 있습니다.
        # "Use peacock feathers to make a fly"를 입력합니다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 다시 한번 페이지가 업데이트 됩니다. 그리고 두 항목 모두를 볼 수 있습니다.
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # 새로운 사용자 Francis 가 싸이트에 들어 옵니다.
        ## 새로운 브라우저를 띄웁니다.
        ## 쿠키등으로 인해 Edith 의 정보가 남아 있지 않게 하기 위함입니다.
        self.browser.quit()
        self.browser = webdriver.Chrome('drivers/chrome')

        # Francis 는 홈페이지를 방문합니다. 홈페이지에는 Edith 의 흔적이 없어야 합니다.
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis 는 새 아이템을 입력합니다.
        # 그는 Edith 보다는 관심이 크지 않습니다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis 는 고유한 URL 을 받습니다.
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 다시 Edith의 흔적이 없는지를 확인합니다.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # 훌륭하네요. 자러 갑니다.
        # self.fail('Finish the test!')

    def test_layout_and_styling(self):

        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # 입력박스는 가운데 정렬이 되어 있습니다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5)

        # 그녀는 새로운 항목을 입력합니다. 그리고 가운데 정렬이 잘 되어 있는지를 확인합니다.
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5)
