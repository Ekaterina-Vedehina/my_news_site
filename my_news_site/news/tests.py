import datetime
from unittest import skip

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import News


# Create your tests here.

def create_new(title, content, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return News.objects.create(title=title, content=content, creation_date=time)


class NewsModelTests(TestCase):
    def test_new_was_published_recently_or_long_ago(self):
        time = timezone.now() - datetime.timedelta(days=7, seconds=1)
        very_old_new = News(creation_date=time)
        self.assertIs(very_old_new.was_published_recently(), False)

    def test_new_was_published_recently(self):
        time = timezone.now() - datetime.timedelta(days=6, minutes=59, seconds=59)
        recent_new = News(creation_date=time)
        self.assertIs(recent_new.was_published_recently(), True)

    @skip
    def test_past_new(self):
        create_new(title='Past news.', content='Past news.', days=-30)
        response = self.client.get(reverse('news:index'))
        self.assertQuerysetEqual(response.context['latest_news'], ['<News: Past news.>'])
