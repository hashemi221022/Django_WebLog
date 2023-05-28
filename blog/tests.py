from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your tests here.
class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post = Post.objects.create(
            title='post1',
            text='this is a test for website',
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user,
        )
        cls.post2 = Post.objects.create(
            title= 'post2',
            text='this is for druft status',
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user,

        )


    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_on_blog_list_page_text(self):
        response = self.client.get(reverse('posts_list'))
        # self.assertContains(response, 'post1')
        self.assertContains(response, self.post.text)

    def test_post_list_on_blog_list_page_title(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post.title)

    def test_post_list_on_blog_list_page_author(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post.author)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_datail_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_blog_detail_page_title(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertContains(response, self.post.title)

    def test_post_details_on_blog_detail_page_author(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertContains(response, self.post.author)

    def test_post_details_on_blog_detail_page_text(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertContains(response, self.post.text)

    # def test_post_details_on_blog_detail_page_status(self):
    #     response = self.client.get(reverse('post_detail', args=[self.post.id]))
    #     self.assertContains(response, self.post.status)
    def test_status_404_if_post_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_post_list_template(self):
        response = self.client.get(reverse('posts_list'))
        self.assertTemplateUsed(response, '_base.html')

    def test_post_list_template(self):
        response = self.client.get(reverse('posts_list'))
        self.assertTemplateUsed(response, 'blog/posts_list.html')

    def test_post_detail_template(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertTemplateUsed(response, '_base.html')

    def test_post_detail_template(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_list_on_blog_list_page_status_publishd_or_druft(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'some title',
            'text': 'this is some title',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)

    def test_post_create_view_check_detials(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'some title 2',
            'text': 'this is some title 2',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(Post.objects.last().title, 'some title 2')
        self.assertEqual(Post.objects.last().text, 'this is some title 2')
        self.assertEqual(Post.objects.last().status, 'pub')
        self.assertEqual(Post.objects.last().author, self.user)

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'some title update',
            'text': 'this is some title update',
            'status': 'pub',
            'author': self.post2.author.id,
        })
        self.assertEqual(response.status_code, 302)

    def test_post_update_view_details(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'some title update 2',
            'text': 'this is some title update 2',
            'status': 'pub',
            'author': self.post2.author.id,
        })
        self.assertEqual(Post.objects.last().title, 'some title update 2')
        self.assertEqual(Post.objects.last().text, 'this is some title update 2')
        self.assertEqual(Post.objects.last().status, 'pub')
        self.assertEqual(Post.objects.last().author, self.user)


    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)
