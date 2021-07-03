import bot
import get_data
import time

def main():
    four_hours = 4*60*60 #seconds
    while True:
        text, url , more = bot.get_random_post() #get data
        if more:
            bot.tweet_image(text, url)
            time.sleep(four_hours)
        else:
            get_data.run()

if __name__ == "__main__":
    main()