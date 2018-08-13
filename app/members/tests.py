from django.contrib.auth import get_user_model
from django.urls import path
from rest_framework import status
from rest_framework.test import APITestCase

from members.tokens import account_activation_token

User = get_user_model()

dummy_user = {
    'username': 'dummy_username@test.com',
    'first_name': 'user',
    'last_name': 'test',
    'birthday': '000000',
    'password': 'test1234'
}


class UserListTest(APITestCase):
    """
    User List 요청에 관한 테스트
    """
    URL = '/members/userlist/'

    def test_not_admin_status_code_403(self):
        """
        superuser가 아닌 일반 유저일 경우에 요청 결과의 HTTP 상태코드가 403인지 확인
        :return:
        """
        # user 회원가입 시키기 & 이메일 인증 True로 바꾸고 저장
        user = User.objects.create_django_user(**dummy_user)
        user.activate = True
        user.save()

        # 로그인을 그냥 바로 시켜버림!
        self.client.force_authenticate(user)

        response = self.client.get(self.URL)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UserSignUpTest(APITestCase):
    """
    User SignUp 에 관한 테스트
    """
    URL = '/members/signup/'

    def test_user_sign_up_succeed_status_code_201(self):
        """
        user 회원가입 정보가 정상적으로 요청되었을 때 요청 결과의 HTTP 상태코드가 201인지 확인
        json으로 요청하고 201 상태코드를 받아옴
        :return:
        """

        response = self.client.post(self.URL, data=dummy_user, format='json', )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserEmailActivateCheckTest(APITestCase):
    """
    User SignUp 시에 Email 인증 관련 테스트
    """
    URL = '/members/activate/<str:uidb64>/<str:token>/'

    def test_check_user_email_token_equal(self):
        """
        user 회원가입 후 발송되는 인증 확인 이메일 token값과 DB에 저장되는 이메일 token 값이 같은지 확인
        :return:
        """
        # user 회원가입 시키기 & 이메일 인증 True로 바꾸고 저장
        user = User.objects.create_django_user(**dummy_user)
        user.activate = True
        user.save()

        # user email token 값과 DB상의 토큰 값 비교
        token = account_activation_token.make_token(user)
        self.assertTrue(account_activation_token.check_token(user, token))

