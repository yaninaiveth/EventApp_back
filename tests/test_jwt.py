from accounts.utils import generateToken
from django.test import TestCase


class JWT_Tests(TestCase):
    def test_token(self):
        target_to_encode = {"token":"secrets"}
        result = generateToken(target_to_encode)
        
        self.assertEqual(result, target_to_encode)

