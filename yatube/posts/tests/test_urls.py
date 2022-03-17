from http import HTTPStatus
from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from posts.models import Post, Group


User = get_user_model()


class PostURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cls.user = User.objects.create_user(username='HasNoName')
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)
        cls.group = Group.objects.create(
            title='Тестовый тест',
            slug='test_slug',
            description='текстовоеполедлянаборатекста',
        )
        cls.post = Post.objects.create(
            text='Тестовый текс',
            group=PostURLTests.group,
            author=cls.user,
        )

    def test_url_all_user(self):
        """Страницы доступны любому пользователю"""
        url_adress_all = (
            '/',
            '/group/test_slug/',
            f'/posts/{self.post.id}/',
            f'/profile/{self.user.username}/',
        )
        for adress in url_adress_all:
            with self.subTest():
                response = self.guest_client.get(adress)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_non__url(self):
        response = self.guest_client.get('/unexisting_page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_url_authorized_user(self):
        """Страницы доступны авторизованному пользователю"""
        url_adress_logged = (
            '/create/',
            f'/posts/{self.post.id}/edit',
        )
        for adress in url_adress_logged:
            with self.subTest():
                response = self.authorized_client.get('/create/')
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон"""
        templane_url_named_auth = {
            '/': 'posts/index.html',
            '/group/test_slug/': 'posts/group_list.html',
            f'/profile/{self.user.username}/': 'posts/profile.html',
            f'/posts/{self.post.id}/': 'posts/post_detail.html',
            f'/posts/{self.post.id}/edit/': 'posts/create_post.html',
            '/create/': 'posts/create_post.html',
            '/unexisting_page/': '404.html',
        }
        template_url_named_non_auth = {
            f'/posts/{self.post.id}/edit/': 'users/login.html',
            '/create/': 'users/login.html',
        }

        for adress, template in templane_url_named_auth.items():
            with self.subTest(adress=adress):
                response = self.authorized_client.get(adress)
                self.assertTemplateUsed(response, template)

        for adress, template in template_url_named_non_auth.items():
            with self.subTest(adress=adress):
                response = self.guest_client.get(adress)
                if response.status_code == 302:
                    response = self.guest_client.get(response.url)
                self.assertTemplateUsed(response, template)
