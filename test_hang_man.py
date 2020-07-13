from game_setup.models import Game, Guess


def test_landing_page(driver, live_server):
    driver.get(live_server.url)
    assert 'hangman' in driver.page_source.lower()
    assert driver.find_element_by_css_selector('[data-test="log-in"]')


def test_login(driver, live_server, user, log_in):
    new_user = user('User', 'passcode')
    log_in(new_user.username, 'passcode')
    assert driver.current_url == live_server + '/game'
    assert driver.find_element_by_css_selector('[data-test="play-game"]')
    assert new_user.username in driver.page_source


def test_create_game(driver, live_server, user, log_in):
    new_user = user('User', 'passcode')
    log_in(new_user.username, 'passcode')
    play_button = driver.find_element_by_css_selector('[data-test="play-game"]')
    play_button.click()
    assert 'game 1' in driver.page_source.lower()
    assert driver.find_element_by_css_selector('[data-test="user-guess"]')
    assert driver.find_element_by_css_selector('[data-test="submit-guess"]')
    game = Game.objects.all().last()
    assert game
    assert game.user == new_user


def test_make_guess(driver, live_server, user, log_in, make_guess):
    new_user = user('User', 'passcode')
    log_in(new_user.username, 'passcode')
    new_game = Game.objects.create(user=new_user, winning_word="Hello")
    driver.get(live_server.url + f'/game/{new_game.pk}')
    make_guess('r')
    latest_guess = Guess.objects.all().last()
    recent_game = Game.objects.all().last()
    assert latest_guess.game == recent_game
    assert recent_game.attempts_left == 5
    assert recent_game.in_progress is True
    wrong_guesses = driver.find_element_by_css_selector('[data-test="wrong-guess"]')
    assert 'r' in wrong_guesses.text
