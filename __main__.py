import bot
import time

def main():
    four_hours = 4*60*60 #seconds
    while True:
        text, url , more = bot.get_random_post() #get data
        if not more: break
        bot.tweet_image(text, url)
        time.sleep(four_hours)

if __name__ == "__main__":
    main()