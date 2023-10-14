import requests
import allure
from data.api import Marm3



token = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJhdXRoVHlwZVwiOlwiSU5URVJOQUxcIixcInVpZFwiOlwiMTEwN1wiLFwibG9naW5cIjpcImRldlwiLFwic2lkXCI6bnVsbCxcIm9wZXJhdG9ySWRcIjpudWxsLFwiZGlzcGxheU5hbWVcIjpcIkRFVi3QkNCU0JzQmNCd0J7QkiBERVYt0JDQlNCc0JjQnSBERVYt0JDQlNCc0JjQndCe0JLQmNCnXCIsXCJwZXJtaXNzaW9uc1wiOlt7XCJzdWJqZWN0XCI6XCLQnNCQ0KDQnDrQntCfLdCa0L7QvdGC0YDQvtC70YzQktC90LXRiNC90LjQtdCU0LDQvdC90YvQtVwiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQmNCd0J860J7Qny3QodC-0LfQtNCw0L3QuNC10JjQvdGE0L7RgNC80LDRhtC40L7QvdC90YvRhdCf0LjRgdC10LxcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0JzQkNCg0Jw60J7Qny3QntGC0YfQtdGC0YvQlNCw0L3QvdGL0LVcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwiWmFrYXpDaGVrb3ZLS1RfQUM60J7Qny3Ql9Cw0LrQsNC30KfQtdC60L7QslwiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQnNCQ0KDQnDrQntCfLdCa0L7QvdGC0YDQvtC70YzQktC90LXRiNC90LjQtdCU0LDQvdC90YvQtdCQ0LTQvNC40L3QuNGB0YLRgNC40YDQvtCy0LDQvdC40LVcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0JzQkNCg0Jw60J7Qny3QmtC-0L3RgtGA0L7Qu9GM0J_QvtC40YHQutCk0JRcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0JzQkNCg0Jw60J7Qny3QmtC-0L3RgtGA0L7Qu9GM0KHRgNC10LTQsNCa0JrQolwiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQn9Cf0KTQlDrQntCfLdCS0LjQtNC40LzQvtGB0YLRjNCf0J_QpNCUXCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCc0JDQoNCcOtCe0J8t0J7RgtGH0LXRgtGL0K3QutC-0L3QvtC80LjQutCwXCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCc0JDQoNCcOtCe0J8t0J_RgNC-0YHQvNC-0YLRgNCa0LDRgNGC0L7Rh9C10LrQmtCa0KJcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0JzQkNCg0Jw60J7Qny3QntGC0YfQtdGC0YvQotC10YHRgtC40YDQvtCy0LDQvdC40LVcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0JzQkNCg0Jw60J7Qny3Qn9GA0L7RgdC80L7RgtGA0JjQvdGE0L7Qs9GA0LDRhNC40LrQuFwiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQnNCQ0KDQnDrQntCfLdCa0L7QvdGC0YDQvtC70YzQmNC90YTQvtGA0LzQuNGA0L7QstCw0L3QuNC10J3Qn1wiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQn9Cf0KTQlDrQntCfLdCf0YDQvtGB0LzQvtGC0YDQn9GA0LjQtdC80J3QtdCS0LDQu9C40LTQvdGL0LXQn9Cw0YDRi1wiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQnNCQ0KDQnDrQntCfLdCe0YLRh9C10YLRi1wiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQn9Cf0KTQlDrQntCfLdCf0YDQvtGB0LzQvtGC0YDQlNC-0LPQvtCy0L7RgNGLXCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCf0J_QpNCUOtCe0J8t0J_RgNC-0YHQvNC-0YLRgNCa0JrQolwiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQnNCQ0KDQnDrQntCfLdCa0L7QvdGC0YDQvtC70YzQltCw0LvQvtCx0YtcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0JzQkNCg0Jw60J7Qny3QmtC-0L3RgtGA0L7Qu9GMXCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCf0J_QpNCUOtCe0J8t0J_RgNC-0YHQvNC-0YLRgNCf0YDQuNC10LzQndC10YLQlNC-0LPQvtCy0L7RgNCwXCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCY0J3QnzrQntCfLdCf0YDQvtGB0LzQvtGC0YDQmNC90YTQvtGA0LzQsNGG0LjQvtC90L3Ri9GF0J_QuNGB0LXQvFwiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQnNCQ0KDQnDrQntCfLdCa0L7QvdGC0YDQvtC70YzQoNGL0L3QutC4XCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCc0JDQoNCcOtCe0J8t0J_RgNC-0YHQvNC-0YLRgNCh0YLQsNGC0LjRgdGC0LjQutC4XCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCc0JDQoNCcOtCe0J8t0J_RgNC-0YHQvNC-0YLRgNCe0LHRitC10LrRgtC-0LLQndCw0JrQsNGA0YLQtVwiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCJaYWthekNoZWtvdktLVF9BQzrQntCfLdCX0LDQutCw0LfQkNCz0YDQtdCz0LDRgtC-0LJcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0JzQkNCg0Jw60J7Qny3QmtC-0L3RgtGA0L7Qu9GM0JDQstGC0L7QvdC-0LzQvdGL0LXQotC10YDRgNC40YLQvtGA0LjQuFwiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQnNCQ0KDQnDrQntCfLdCf0YDQvtGB0LzQvtGC0YDQodGC0LDRgtC40YHRgtC40LrQuNCd0J9cIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0JzQkNCg0Jw60J7Qny3QntGC0YfQtdGC0YvQmtC-0L3RgtGA0L7Qu9GMXCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCc0JDQoNCcOtCe0J8t0J7RgtGH0LXRgtGL0J_RgNC40LzQtdC90LXQvdC40LVcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0J_Qn9Ck0JQ60J7Qny3Qn9GA0L7RgdC80L7RgtGA0JzQvtC90LjRgtC-0YDQuNC90LNcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0J_Qn9Ck0JQ60J7Qny3Qn9GA0L7RgdC80L7RgtGA0JrQvtC70LjRh9C10YHRgtCy0L7Ql9Cw0YDQtdCz0LjRgdGC0YDQuNGA0L7QstCw0L3QvdGL0YXQmtCa0KJcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwiWmFrYXpDaGVrb3ZLS1RfQUM60J7Qny3Ql9Cw0LrQsNC30JLRi9Cz0YDRg9C30L7QutCR0LXQt9Ce0LPRgNCw0L3QuNGH0LXQvdC40LlcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0J_Qn9Ck0JQ60J7Qny3Qn9GA0L7RgdC80L7RgtGA0JrQvtC70LjRh9C10YHRgtCy0L7QpNCUXCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCc0JDQoNCcOtCe0J8t0J7RgtGH0LXRgtGL0KLQndCeXCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCf0J_QpNCUOtCe0J8t0J_RgNC-0YHQvNC-0YLRgNCe0KTQlFwiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQn9Cf0KTQlDrQntCfLdCf0YDQvtGB0LzQvtGC0YDQntGC0LrQsNC30JLQn9GA0LjQtdC80LVcIixcImFjdGlvbnNcIjpcIjAwMDBcIn0se1wic3ViamVjdFwiOlwi0J_Qn9Ck0JQ60J7Qny3Qn9GA0L7RgdC80L7RgtGA0KTQlFwiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQnNCQ0KDQnDrQntCfLdCa0L7QvdGC0YDQvtC70YzQn9GA0L7QstC10YDQutCw0KfQtdC60L7QslwiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQn9Cf0KTQlDrQntCfLdCf0YDQvtGB0LzQvtGC0YDQn9GA0LjQtdC80JTRgNGD0LPQuNC10J7RiNC40LHQutC4XCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCc0JDQoNCcOtCe0J8t0J7RgtGH0LXRgtGL0KDQtdCz0LjRgdGC0YDQsNGG0LjRj1wiLFwiYWN0aW9uc1wiOlwiMDAwMFwifSx7XCJzdWJqZWN0XCI6XCLQnNCQ0KDQnDrQntCfLdCS0LjQtNC40LzQvtGB0YLRjNCc0JDQoNCcXCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCf0J_QpNCUOtCe0J8t0J_RgNC-0YHQvNC-0YLRgNCh0LLQvtC00L3QsNGPXCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCc0JDQoNCcOtCe0J8t0K3QutC-0L3QvtC80LjQutCwXCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9LHtcInN1YmplY3RcIjpcItCc0JDQoNCcOtCe0J8t0JrQvtC90YLRgNC-0LvRjNCh0YDQtdC00LDQmtCa0KLQkNC00LzQuNC90LjRgdGC0YDQuNGA0L7QstCw0L3QuNC1XCIsXCJhY3Rpb25zXCI6XCIwMDAwXCJ9XX0iLCJleHAiOjE2OTcyNDEyNTJ9.sfJzqFG8EZBcxdwV3CqlEJghgA63FcUtP_GqYCDslJRIQ8proXD9RkvGsjfOhnUHMETcMVBxhJHCgdHDqY3rIw"  # Замените YOUR_TOKEN на ваш реальный токен авторизации
class TestApi:

    @classmethod
    def setup_class(cls):
        cls.token = token

    @allure.title("Проверка статус-кода")
    def test_status_code(self):
        for key, value in Marm3.__dict__.items():
            if key.startswith('INDICATORS_'):
                url = value["url"]
                response = requests.get(url, headers={"Authorization": f"Bearer {self.token}"})
                assert response.status_code == 200

    @allure.title("Проверка формата ответа")
    def test_response_format(self):
        for key, value in Marm3.__dict__.items():
            if key.startswith('INDICATORS_'):
                url = value["url"]
                response = requests.get(url, headers={"Authorization": f"Bearer {self.token}"})
                assert response.headers["Content-Type"] == "application/json"

    @allure.title("Проверка отправки запроса без авторизации")
    def test_unauthorized_request(self):
        for key, value in Marm3.__dict__.items():
            if key.startswith('URL_'):
                url = value["url"]
                response = requests.get(url)
                assert response.status_code == 401
