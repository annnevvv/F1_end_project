from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.test import Client

from .models import Post, Tag, Author, Comment

fixtures = ['test_Post_fixture.json']
current_date = datetime.now().strftime('%Y-%m-%d')
txt_for_post = "Lorem ipsum dolor sit amet. Lorem Ipsum is simply dummy " \
               "text of the printing and typesetting industry. Lorem " \
               "Ipsum has been the industry's standard dummy text ever " \
               "since the 1500s, when an unknown printer took a galley of type " \
               "and scrambled it to make a type specimen book. It has survived " \
               "not only five centuries, but also the leap into electronic " \
               "typesetting, remaining essentially unchanged. It was popularised " \
               "in the 1960s with the release of Letraset sheets containing " \
               "Lorem Ipsum passages, and more recently with desktop publishing " \
               "software like Aldus PageMaker including versions of Lorem Ipsum."


class BlogMainUrlTest(TestCase):  # pass
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


class CommentModelTestCase(TestCase):  # pass
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

    def test_comment_fields(self):  # pass
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

    def test_comment_str_representation(self):  # pass
        comment = Comment.objects.get(pk=1)
        expected_str = f"{comment.user_name} - {comment.user_email}"
        self.assertEqual(str(comment), expected_str)


class AuthorModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(
            f_name='Nobody',
            l_name='Nothing',
            pseudonym='NN',
            email='nothing@noreply.com'
        )

    def test_author_full_name(self):
        expected_full_name = 'Nobody Nothing'
        self.assertEqual(self.author.full_name(), expected_full_name)

    def test_author_str_representation_with_pseudonym(self):
        expected_str = 'NN'
        self.assertEqual(str(self.author), expected_str)

    def test_author_str_representation_without_pseudonym(self):
        self.author.pseudonym = ''
        expected_str = 'Nobody Nothing'
        self.assertEqual(str(self.author), expected_str)

    def test_author_fields(self):
        self.assertEqual(self.author.f_name, 'Nobody')
        self.assertEqual(self.author.l_name, 'Nothing')
        self.assertEqual(self.author.pseudonym, 'NN')
        self.assertEqual(self.author.email, 'nothing@noreply.com')


class BlogMainPageViewTest(TestCase):  # pass
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='Jey123',
                                   email='jay@op.pl',
                                   password='Pies123!')

        author = Author.objects.create(
            f_name='Nobody',
            l_name='Nothing',
            pseudonym='NN',
            email='nothing@noreply.com'
        )

        cls.post1 = Post.objects.create(
            title='Post 1',
            excerpt=5 * 'Excerpt 1',
            image='posts/F1.png',
            date=current_date,
            txt=10 * 'Lorem ipsum dolor sit amet.',
            slug='post-1',
            user=user,
            author=author
        )
        cls.post2 = Post.objects.create(
            title='Post 2',
            excerpt=5 * 'Excerpt 2',
            image='posts/F1.png',
            date=current_date,
            txt=10 * 'Lorem ipsum dolor sit amet.',
            slug='post-2',
            user=user,
            author=author
        )

    def setUp(self):
        self.client = Client()
        self.url = reverse('blog_main_page')

    def test_blog_main_page_view(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')
        self.assertEqual(list(response.context['posts']), [
            self.post1, self.post2
        ])
        self.assertEqual(response.context['posts'].ordered, True)
        self.assertEqual(
            response.context['posts'].query.order_by, ('-date',)
        )
        self.assertContains(response, 'Post 1')
        self.assertContains(response, 'Post 2')
        self.assertNotContains(response, 'Post 3')
