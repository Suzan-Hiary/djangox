from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Roses
from django.urls import reverse

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='suzan',
            email='suze@admin.com',
            password='0000'
        )

        self.post = Roses.objects.create(
            title='apples',
            description='healthy food',
            purchaser=self.user
        )

    
    def test_string_representation(self):
        post = Roses(title='title')
        self.assertEqual(str(post), post.title)

    def test_all_fields(self):
        
        self.assertEqual(str(self.post), 'apples')
        self.assertEqual(f'{self.post.purchaser}', 'suzan')
        self.assertEqual(self.post.description, 'healthy food')

    def test_blog_list_view(self):
        response = self.client.get(reverse('roses'))
        self.assertEqual(response.status_code, 200)

    def test_blog_details_view(self):
        response = self.client.get(reverse('detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_blog_update_view(self):
        response = self.client.post(reverse('update', args='1'), {
            'title': 'chips',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'chips')

    def test_home_status(self):
        expected = 200
        url = reverse('roses')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
        
    def test_home_template(self):
        url = reverse('roses')
        response = self.client.get(url)
        actual = 'roses/list_view.html'
        self.assertTemplateUsed(response, actual)
    
    def test_create_view(self):
        response = self.client.post(reverse('create'), {
            'title': 'chips',
            'purchaser': self.user,
            'description' :'healthy food',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'chips')
        self.assertContains(response, 'healthy food')
        self.assertContains(response, 'suzan')

    def test_delete_view(self):
        response = self.client.get(reverse('delete', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure you want to delete?')

        post_response = self.client.post(reverse('delete', args='1'))
        self.assertRedirects(post_response, reverse('roses'), status_code=302)


    