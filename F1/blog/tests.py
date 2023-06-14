from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

from .models import Post, Tag, Author, Comment

fixtures = ['test_Post_fixture.json']
current_date = datetime.now().strftime('%Y-%m-%d')
txt_for_post = "Lorem ipsum dolor sit amet. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."


class BlogMainTests(TestCase):  # pass
    def test_url_exists_at_correct_location(self):
        url = reverse("blog_main_page")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # pass
        url = reverse("blog_main_page")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "blog/index.html")

    def test_template_content(self):  # pass
        url = reverse("blog_main_page")
        response = self.client.get(url)
        self.assertContains(response, "<h2>Our Latest Posts</h2>")
        self.assertNotContains(response, "Not on the page")


class PostModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='Jey123',
                                   email='jay@op.pl',
                                   password='Pies123!')
        author = Author.objects.create(f_name='Test01 f_Author',
                                       l_name='Test01 l_Author',
                                       pseudonym='Test Pseudonym 01',
                                       email='testautor01@test.pl')
        tag1 = Tag.objects.create(caption='Tag1')
        tag2 = Tag.objects.create(caption='Tag2')

        cls.post = Post.objects.create(
            title='PostTestowy 01',
            excerpt='Excerpt testowy 01, Excerpt testowy 01, Excerpt testowy 01',
            image='posts/F1.png',
            date=datetime.now().strftime('%Y-%m-%d'),
            txt=txt_for_post,
            slug='post-testowy-01',
            user=user,
            author=author
        )

        cls.post.tags.set([tag1, tag2])

    def test_post_str_representation(self):  # pass
        self.assertEqual(str(self.post), 'post-testowy-01')

    def test_post_fields(self):  # pass
        self.assertEqual(self.post.title, 'PostTestowy 01')
        self.assertEqual(self.post.excerpt,
                         'Excerpt testowy 01, Excerpt testowy 01, Excerpt testowy 01')
        self.assertEqual(self.post.image, 'posts/F1.png')
        self.assertEqual(str(self.post.date), current_date)
        self.assertEqual(self.post.txt, txt_for_post)
        self.assertEqual(self.post.slug, 'post-testowy-01')
        self.assertEqual(self.post.user.username, 'Jey123')
        self.assertEqual(self.post.author.f_name, 'Test01 f_Author')

        tag_list = [tag.caption for tag in self.post.tags.all()]

        self.assertCountEqual(tag_list, ['Tag1', 'Tag2'])

    def test_post_default_image(self):  # pass
        self.assertEqual(self.post.image.path,
                         r"D:\programowanie\DYSK Z\2023\F1_end_project\F1\uploads\posts\F1.png")


class CommentModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='Jey123',
                                   email='jay@op.pl',
                                   password='Pies123!')

        post = Post.objects.create(
            title='Test Post',
            excerpt='Test excerpt, Test excerpt, Test excerpt, Test excerpt',
            image='posts/F1.png',
            date=current_date,
            txt=txt_for_post,
            user=user,
            slug='test-post'
        )

        cls.comment = Comment.objects.create(
            user_name='Nothing Nothing',
            user_email='johndoe@example.com',
            txt=txt_for_post[:50],
            post=post
        )

    def test_comment_fields(self): #pass
        comment = Comment.objects.get(pk=1)
        self.assertEqual(comment.user_name, 'Nothing Nothing')
        self.assertEqual(comment.user_email, 'johndoe@example.com')
        self.assertEqual(comment.txt, txt_for_post[:50])
        self.assertEqual(comment.post.title, 'Test Post')
        self.assertEqual(comment.post.excerpt,
                         'Test excerpt, Test excerpt, Test excerpt, Test excerpt')
        self.assertEqual(comment.post.image, 'posts/F1.png')
        self.assertEqual(str(comment.post.date), current_date)
        self.assertEqual(comment.post.txt, txt_for_post)
        self.assertEqual(comment.post.slug, 'test-post')
        self.assertEqual(comment.post.comments.count(), 1)
        self.assertEqual(comment.post.comments.first(), comment)

    def test_comment_str_representation(self):
        comment = Comment.objects.get(pk=1)
        expected_str = f"{comment.user_name} - {comment.user_email}"
        self.assertEqual(str(comment), expected_str)

# class PostModelTestCaseFixture(TestCase):
#     fixtures = 'test_Post_fixture.json'
#
#     def test_post_str_representation(self):
#         post = Post.objects.get(pk=1)
#         self.assertEqual(str(post), 'post-testowy-01')
#
#     def test_post_fields(self):
#         post = Post.objects.get(pk=1)
#         self.assertEqual(post.title, 'PostTestowy 01')
#         self.assertEqual(post.excerpt,
#                          'Excerpt testowy 01, Excerpt testowy 01, Excerpt testowy 01')
#         self.assertEqual(post.image, 'posts/F1.png')
#         self.assertEqual(str(post.date), '2023-06-13')
#         self.assertEqual(post.txt,
#                          "Lorem ipsum dolor sit amet. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
#         self.assertEqual(post.slug, 'post-testowy-01')
#         self.assertEqual(post.user.username, 'Jey123')
#         self.assertEqual(post.author.f_name, 'Test01 f_Author')
#         self.assertEqual(post.author.l_name, 'Test01 l_Author')
#         self.assertEqual(post.author.pseudonym, 'Test Pseudonym 01')
#         self.assertEqual(post.author.email, 'testautor01@test.pl')
#         self.assertCountEqual(post.tags.values_list('caption', flat=True),
#                               ['Tag1', 'Tag2'])
#
#     def test_post_default_image(self):
#         post = Post.objects.get(pk=1)
#         self.assertEqual(post.image.path, 'posts/F1.png')
