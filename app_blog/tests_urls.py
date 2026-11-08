from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail

class UrlsTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)
        
    def test_articles_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_articles_list_url_resolves(self):
        view = resolve('/articles/')
        self.assertEqual(view.func.view_class, ArticleList)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('test-category',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_category_url_resolves(self):
        view = resolve('/articles/category/test-category/')
        self.assertEqual(view.func.view_class, ArticleCategoryList)


    def test_article_detail_url_resolves(self):
        view = resolve('/articles/2026/11/8/test-article/')
        self.assertEqual(view.func.view_class, ArticleDetail)