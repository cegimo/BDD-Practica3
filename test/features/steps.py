from lettuce import *
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager


@step('Search tweet box')
def find_element_by_name(step, tweet):
    world.tweet = find_element_by_name("tweet")

@step('Write the tweet')
def send_keys(step, text):
    world.tweet_text = find_element_by_name(tweet)
    world.write_tweet = world.tweet_text.send_keys("Hola! Estoy usando Selenium para mostrar este tweet!")

@step('Public tweet')
def public_tweet(write_tweet, expected):
    expected = find_element_by_css_selector("selector").click
    assert world.text_tweet == expected, \
        "Hola! Estoy usando Selenium para mostrar este tweet!"


def tweet(tweet):
    return "Hola! Estoy usando Selenium para mostrar este tweet!"