from main import Shopify
from nose.tools import assert_equal


class TestMain:
	def test_increment(self):
		shop = Shopify()
		shop.increment();
		assert_equal(2, shop.page)