from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import datetime
import time
import random

prev_post = []
prev_name = []


def tym():
    return datetime.datetime.now().strftime("%H:%M:%S")


# noinspection PyDeprecation
class InstagramBot:
    def __init__(self, username, password, input_comments):
        self.username = username
        self.password = password
        self.comment_list = [input_comments]
        self.bot = webdriver.Chrome("chromedriver.exe")
        self.commented = 0

    # Login and popup...
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com')
        print(tym(), ": Opening webpage")
        time.sleep(4)

        try:
            # Username....
            bot.find_element(By.NAME, 'username').send_keys(self.username)
            time.sleep(1)
            print(tym(), ": Typing username")

            # password...
            bot.find_element(By.NAME, 'password').send_keys(self.password + Keys.RETURN)
            print(tym(), ": Typing password and loging in")
            time.sleep(15)

            # popup not now button...
            bot.find_element(By.XPATH,
                             "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button").click()
            print(tym(), ": Not now")

            time.sleep(8)

        except NoSuchElementException:
            for error in range(4):
                if error == 3:
                    break
                login_error = bot.find_element(By.XPATH,
                                               "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[2]/p").text
                if login_error == "We couldn't connect to Instagram. Make sure you're connected to the internet and " \
                                  "try again.":
                    print(tym(), ": Login Error")
                    insta.login()

        try:
            # popup not now button...
            bot.find_element(By.XPATH,
                             '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
            print(tym(), ": Not now")
            time.sleep(8)

        except NoSuchElementException:
            bot.find_element(By.XPATH,
                             "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div["
                             "3]/div/div[1]/div/a/svg").click()
            time.sleep(8)

    # noinspection PyGlobalUndefined
    def comment(self):
        global post
        bot = self.bot
        z = 0
        # Put comments in the comment_list
        rand_time = [15, 20, 25]
        rand_time = random.choice(rand_time)

        # Check the time of the first 4 comments if it is between (1-15 minutes) or (1-60 seconds)
        for x in range(1, 4):
            def try_post():
                try:
                    text_area_1 = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[" \
                                  "2]/section/main/div[1]/section/div/div[3]/div[1]/div/article[{0}]/div/div[" \
                                  "3]/div/div/section[3]/div/form/div/textarea".format(
                        str(x))
                    text_area_2 = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[" \
                                  "2]/section/main/div[1]/section/div/div[3]/div[2]/div/article[{0}]/div/div[" \
                                  "3]/div/div/section[3]/div/form/div/textarea".format(
                        str(x))

                    try:
                        z = 0
                        bot.find_element(By.XPATH, text_area_1).click()
                        time.sleep(rand_time)

                        ran_comments = random.choice(self.comment_list)

                        bot.find_element(By.XPATH, text_area_1).send_keys(
                            ran_comments)
                        print(tym(), ': c1@@@@@@@@@@')
                        time.sleep(3)
                        bot.find_element(By.XPATH, text_area_1).send_keys(
                            Keys.RETURN)

                        time.sleep(2)

                        try:
                            fail = bot.find_element(By.CLASS_NAME, "tA2fc ").text
                            if fail == "Couldn't post comment.\n" \
                                       "Retry":
                                print(fail)
                                bot.quit()
                            else:
                                self.commented += 1
                                print(tym(), ":", self.commented)
                                time.sleep(rand_time)

                        except NoSuchElementException:
                            self.commented += 1
                            print(tym(), ":", self.commented)
                            time.sleep(rand_time)

                    except NoSuchElementException:
                        bot.find_element(By.XPATH, text_area_2).click()
                        time.sleep(rand_time)

                        ran_comments = random.choice(self.comment_list)

                        bot.find_element(By.XPATH, text_area_2).send_keys(
                            ran_comments)
                        print(tym(), ': c1@@@@@@@@@@')
                        time.sleep(3)
                        bot.find_element(By.XPATH, text_area_2).send_keys(
                            Keys.RETURN)

                        time.sleep(2)

                        try:
                            fail = bot.find_element(By.CLASS_NAME, "tA2fc ").text
                            if fail == "Couldn't post comment.\n" \
                                       "Retry":
                                print(fail)
                                bot.quit()
                            else:
                                self.commented += 1
                                print(tym(), ":", self.commented)
                                time.sleep(rand_time)

                        except NoSuchElementException:
                            self.commented += 1
                            print(tym(), ":", self.commented)
                            time.sleep(rand_time)

                except:
                    z = +1
                    if z < 4:
                        bot.refresh()
                        time.sleep(3)
                        insta.comment()
                    else:
                        bot.close()

            def except_post():
                try:
                    text_area_1_2 = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[" \
                                    "2]/section/main/div[1]/section/div/div[3]/div[1]/div/article[{0}]/div/div[" \
                                    "3]/div/div/section[2]/div/form/div/textarea".format(
                        str(x))
                    text_area_2_2 = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[" \
                                    "2]/section/main/div[1]/section/div/div[3]/div[2]/div/article[{0}]/div/div[" \
                                    "3]/div/div/section[2]/div/form/div/textarea".format(
                        str(x))
                    try:
                        z = 0
                        bot.find_element(By.XPATH, text_area_1_2).click()
                        time.sleep(rand_time)

                        ran_comments = random.choice(self.comment_list)

                        bot.find_element(By.XPATH, text_area_1_2).send_keys(ran_comments)

                        print(tym(), ': c2@@@@@@@@@@')
                        time.sleep(3)

                        bot.find_element(By.XPATH, text_area_1_2).send_keys(Keys.RETURN)
                        time.sleep(2)
                        try:
                            fail = bot.find_element(By.CLASS_NAME, "tA2fc ").text
                            if fail == "Couldn't post comment.\n" \
                                       "Retry":
                                print(fail)
                                bot.quit()
                            else:
                                self.commented += 1
                                print(tym(), ":", self.commented)
                                time.sleep(rand_time)

                        except NoSuchElementException:
                            self.commented += 1
                            print(tym(), ":", self.commented)
                            time.sleep(rand_time)

                    except NoSuchElementException:
                        bot.find_element(By.XPATH, text_area_2_2).click()
                        time.sleep(rand_time)

                        ran_comments = random.choice(self.comment_list)

                        bot.find_element(By.XPATH, text_area_2_2).send_keys(
                            ran_comments)

                        print(tym(), ': c2@@@@@@@@@@')
                        time.sleep(3)

                        bot.find_element(By.XPATH, text_area_2_2).send_keys(
                            Keys.RETURN)
                        time.sleep(2)
                        try:
                            fail = bot.find_element(By.CLASS_NAME, "tA2fc ").text
                            if fail == "Couldn't post comment.\n" \
                                       "Retry":
                                print(tym(), ":", fail)
                                bot.quit()
                            else:
                                self.commented += 1
                                print(tym(), ":", self.commented)
                                time.sleep(rand_time)

                        except NoSuchElementException:
                            self.commented += 1
                            print(tym(), ":", self.commented)
                            time.sleep(rand_time)

                except:
                    z = +1
                    if z < 4:
                        bot.refresh()
                        time.sleep(3)
                        insta.comment()
                    else:
                        bot.close()

            # Check the time of the post
            try:
                try:
                    post_time = bot.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section"
                                                            "/main/div[1]/section/div/div[3]/div[1]/div/article[{0}]/div/div[1]/div/header"
                                                            "/div[2]/div[1]/div[2]/div/div/time".format(
                                                    str(x))).text
                        

                    for dtm in range(14):
                        if (post_time == str(dtm) + "m") or (post_time == "1m"):
                            # Post name and title to check if post is already commented or not
                            try:
                                post = bot.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section"
                                                                "/main/div[1]/section/div/div[3]/div[1]/div/article[{0}]/div/div[3]/div/div/div/div"
                                                                "/div[1]/div/span[2]/h1".format(str(x))).text

                                # if not commented then add the post name and tittle in the pre_post list and  randomly
                                # comment on the post
                                if post not in prev_post:
                                    prev_post.append(post)
                                    print(tym(), ": [1]", post_time)
                                    print(tym(), ': p1#########')  # print(prev_post)
                                    try:
                                        try_post()
                                    except:
                                        except_post()

                                else:
                                    pass
                            except NoSuchElementException:
                                name = bot.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section"
                                                                "/main/div[1]/section/div/div[3]/div[1]/div/article[{0}]/div/div[1]/div/header/div[2]"
                                                                "/div[1]/div[1]/div/div/div/div/span/a".format(str(x))).text

                                if name not in prev_name:
                                    prev_name.append(name)
                                    print(tym(), ": [1]", post_time)
                                    print(tym(), ': n1#########')
                                    try:
                                        try_post()
                                    except:
                                        except_post()

                                else:
                                    pass

                    for dts in range(10, 61):
                        if post_time == str(dts) + "s":
                            try:
                                post = bot.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section"
                                                                "/main/div[1]/section/div/div[3]/div[1]/div/article[{0}]/div/div[3]/div/div/div/div"
                                                                "/div[1]/div/span[2]/h1".format(str(x))).text

                                if post not in prev_post:
                                    prev_post.append(post)
                                    print(tym(), ": [1]", post_time)
                                    print(tym(), ': p1#########')  # print(prev_post)
                                    try:
                                        try_post()
                                    except:
                                        except_post()

                                else:
                                    pass

                            except NoSuchElementException:
                                name = bot.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section"
                                                                "/main/div[1]/section/div/div[3]/div[1]/div/article[{0}]/div/div[1]/div/header/div[2]"
                                                                "/div[1]/div[1]/div/div/div/div/span/a".format(str(x))).text

                                if name not in prev_name:
                                    prev_name.append(name)
                                    print(tym(), ": [1]", post_time)
                                    print(tym(), ': n1#########')
                                    try:
                                        try_post()
                                    except:
                                        except_post()

                                else:
                                    pass

                except NoSuchElementException:
                    post_time = bot.find_element(By.XPATH,
                                                "/html/body/div[\2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[3]/div[2]/div/article[{0}]/div/div[1]/div/header/div[2]/div[1]/div[2]/div/div/time".format(
                                                    str(x))).text
                        

                    for dtm in range(14):
                        if (post_time == str(dtm) + "m") or (post_time == "1m"):
                            # Post name and title to check if post is already commented or not
                            try:
                                post = bot.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section"
                                                                "/main/div[1]/section/div/div[3]/div[2]/div/article[{0}]/div/div[3]/div/div/div/div"
                                                                "/div[1]/div/span[2]/h1".format(str(x))).text

                                # if not commented then add the post name and tittle in the pre_post list and  randomly
                                # comment on the post
                                if post not in prev_post:
                                    prev_post.append(post)
                                    print(tym(), ": [2]", post_time)
                                    print(tym(), ': p2#########')  # print(prev_post)
                                    try:
                                        except_post()
                                    except:
                                        try_post()

                                else:
                                    pass
                            except NoSuchElementException:
                                name = bot.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section"
                                                                "/main/div[1]/section/div/div[3]/div[2]/div/article[{0}]/div/div[1]/div/header/div[2]"
                                                                "/div[1]/div[1]/div/div/div/div/span/a".format(str(x))).text

                                if name not in prev_name:
                                    prev_name.append(name)
                                    print(tym(), ": [2]", post_time)
                                    print(tym(), ': n2#########')
                                    try:
                                        except_post()
                                    except:
                                        try_post()

                                else:
                                    pass

                    for dts in range(10, 61):
                        if post_time == str(dts) + "s":
                            try:
                                post = bot.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section"
                                                                "/main/div[1]/section/div/div[3]/div[2]/div/article[{0}]/div/div[3]/div/div/div/div"
                                                                "/div[1]/div/span[2]/h1".format(str(x))).text

                                # if not commented then add the post name and tittle in the pre_post list and  randomly
                                # comment on the post
                                if post not in prev_post:
                                    prev_post.append(post)
                                    print(tym(), ": [2]", post_time)
                                    print(tym(), ': p2#########')  # print(prev_post)
                                    try:
                                        except_post()
                                    except:
                                        try_post()

                                else:
                                    pass
                            except NoSuchElementException:
                                name = bot.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section"
                                                                "/main/div[1]/section/div/div[3]/div[2]/div/article[{0}]/div/div[1]/div/header/div[2]"
                                                                "/div[1]/div[1]/div/div/div/span/a".format(str(x))).text

                                if name not in prev_name:
                                    prev_name.append(name)
                                    print(tym(), ": [2]", post_time)
                                    print(tym(), ': n2#########')
                                    try:
                                        except_post()
                                    except:
                                        try_post()

                                else:
                                    pass
            except:
                    pass

    def refresh(self):
        bot = self.bot
        for n in range(6):
            if self.commented >= 10:
                print(tym(), ": stop")
                self.commented = self.commented * 0
                time.sleep(600)
                print(tym(), ": start")
                prev_post.clear()
                insta.refresh()
            if n == 5:
                time.sleep(200)
                prev_post.clear()
                insta.refresh()
            else:
                bot.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(2)
                bot.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(8)
                insta.comment()
                time.sleep(10)
                bot.refresh()
                time.sleep(6)


# Your username and password
input_username = input("Enter your Instagram username: ")
input_password = input("Enter your password: ")
input_comments = input("Enter the comments: ")
insta = InstagramBot(input_username, input_password, input_comments)
insta.login()
insta.refresh()
