Feature: Post tweet
    In order to have more note
    as nicemusic
    We post a tweet

    Scenario: public tweet
        Given I go to "https://www.twitter.com"
        When I fill in field with name "tweet" with "Hola! Estoy usando Selenium para mostrar este tweet!"
        Then I should see "Hola! Estoy usando Selenium para mostrar este tweet!"
