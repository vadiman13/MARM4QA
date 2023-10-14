from datetime import datetime, timedelta

today = datetime.today()
one_month_ago = today - timedelta(days=30)
formatted_date = one_month_ago.strftime('%Y-%m-%d %H:%M:%S').replace(' ', '%20')


class Marm3:
    INDICATORS_EXPENSERELEVANCEINDICATOR = {
        "url": "https://marm.nalog.gov.ru:9085/marm3/api/v1/indicators/profitrelevanceindicator",
    }
    INDICATORS_PROFITRELEVANCEINDICATOR = {
        "url": "https://marm.nalog.gov.ru:9085/marm3/api/v1/indicators/profitrelevanceindicator",
    }
    URL_USERS = {
        "url": f"https://marm.nalog.gov.ru:9085/marm3/api/v1/indicators/foodindicator?month={formatted_date}",
        "params": {
            "month": f"{formatted_date}"

        }
    }





