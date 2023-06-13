from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Post, Tag, Author

fixtures = ['test_Post_fixture.json']


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
            date='2023-06-13',
            txt="Lorem ipsum dolor sit amet. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            slug='post-testowy-01',
            user=user,
            author=author
        )

        cls.post.tags.set([tag1, tag2])

    def test_post_str_representation(self):
        self.assertEqual(str(self.post), 'post-testowy-01')

    def test_post_fields(self):
        self.assertEqual(self.post.title, 'PostTestowy 01')
        self.assertEqual(self.post.excerpt, 'Excerpt testowy 01, Excerpt testowy 01, Excerpt testowy 01')
        self.assertEqual(self.post.image, 'posts/F1.png')
        self.assertEqual(str(self.post.date), '2023-06-13')
        self.assertEqual(self.post.txt, "Lorem ipsum dolor sit amet. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
        self.assertEqual(self.post.slug, 'post-testowy-01')
        self.assertEqual(self.post.user.username, 'testuser')
        self.assertEqual(self.post.author.name, 'Test Author')
        self.assertCountEqual(self.post.tags.all(), ['Tag1', 'Tag2'])

    def test_post_default_image(self):
        self.assertEqual(self.post.image.path, 'posts/F1.png')



class PostModelTestCase2(TestCase):
    fixtures = fixtures[0]

    def test_post_str_representation(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(str(post), 'post-testowy-01')

    def test_post_fields(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.title, 'PostTestowy 01')
        self.assertEqual(post.excerpt, 'Excerpt testowy 01, Excerpt testowy 01, Excerpt testowy 01')
        self.assertEqual(post.image, 'posts/F1.png')
        self.assertEqual(str(post.date), '2023-06-13')
        self.assertEqual(post.txt, "Lorem ipsum dolor sit amet. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
        self.assertEqual(post.slug, 'post-testowy-01')
        self.assertEqual(post.user.username, 'Jey123')
        self.assertEqual(post.author.f_name, 'Test01 f_Author')
        self.assertEqual(post.author.l_name, 'Test01 l_Author')
        self.assertEqual(post.author.pseudonym, 'Test Pseudonym 01')
        self.assertEqual(post.author.email, 'testautor01@test.pl')
        self.assertCountEqual(post.tags.values_list('caption', flat=True),
                              ['Tag1', 'Tag2'])

    def test_post_default_image(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.image.path, 'posts/F1.png')