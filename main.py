import yaml
import schedule
import time
from scraper import Scraper
from twitter_bot import TwitterBot

def main():
    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)

    scraper = Scraper(config)
    twitter_bot = TwitterBot(config, scraper)

    # Schedule the bot to run every X minutes
    schedule.every(config["schedule"]["interval"]).minutes.do(twitter_bot.run)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
