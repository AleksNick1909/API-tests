import json
import allure


class Helper:

    def attach(self, name: str, body):
        result = json.dumps(body, indent=4)
        allure.attach(
            body=result,
            name=name,
            attachment_type=allure.attachment_type.JSON
        )
