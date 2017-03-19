from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

# from django.core.urlresolvers import resolve
# from django.test import TestCase
# from lists.views import home_page 
# from django.http import HttpRequest 

# class HomePageTest(TestCase):

#     def test_root_url_resolves_to_home_page_view(self):
#         found = resolve('/')  
#         self.assertEqual(found.func, home_page)  

#     def test_home_page_returns_correct_html(self):
#         request = HttpRequest()  
#         response = self.client.get('/')  
#         html = response.content.decode('utf8')  
#         self.assertIn('<title>To-Do lists</title>', html)  
#         self.assertTrue(html.endswith('</html>'))  
#         self.assertTemplateUsed(response ,'home.html')
