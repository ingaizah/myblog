import datetime
from django.test import TestCase
from django.utils import timezone

from myblog.models import Post
# Create your tests here.

class PostMethodTests(TestCase):
    def test_recent_post_with_future_post(self):
        '''Print ONLY Posts in the Last 30 Days.'''
        time=timezone.now()+datetime.timedelta(days=30)
        future_post=Post(published_date=time)
        self.assertEqual(future_post.recent_post(),False)
