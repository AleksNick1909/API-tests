from config.base_test import BaseTest


class TestUsers(BaseTest):

    def test_get_user(self):

        user = self.users_api.get_user()
        print(user)
