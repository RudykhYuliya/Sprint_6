import allure
import pytest

from data import QUESTIONS


@allure.feature('Вопросы о важном')
class TestQuestions:
    @allure.title('Открывается текст ответа на вопрос')
    @pytest.mark.parametrize('index, expected_text', QUESTIONS)
    def test_question_shows_expected_answer(self, main_page, index, expected_text):
        assert main_page.answer_text(index) == expected_text
