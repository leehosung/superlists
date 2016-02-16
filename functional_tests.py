from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('drivers/chrome')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):
        # Edith 는 새로운 멋진 할일관리 싸이트에 대해서 들었습니다.
        # 홈페이지를 확인해 봅니다.
        self.browser.get('http://localhost:8000')

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # 여전히 텍스트 박스가 있습니다.
        # "Use peacock feathers to make a fly"를 입력합니다.
        self.fail('Finish the test!')

        # 다시 한번 페이지가 업데이트 됩니다. 그리고 두 항목 모두를 볼 수 있습니다.

        # Edith 는 싸이트가 그녀의 리스트를 기억하고 있는 지 궁금합니다.
        # 그녀는 싸이트가 유일한 URL을 만들어 둔것을 볼 수 있습니다.
        # 그 URL에 대한 적절한 설명을 볼 수 있습니다.

        # 그녀는 위 URL 을 방문합니다. 그녀가 입력한 항목들이 남아 있습니다.

        # 훌륭하네요. 자러 갑니다.
