'''
Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format



You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.



Each new record should be added to the end of file. Commit file in git for review.

'''

from datetime import datetime


class Publisher:
    def __init__(self):
        self.file_opened = open("News_file", "a+")
        self.inital_write()

    def inital_write(self):
        content=self.file_opened.read()
        if ("News feed:") not in content:
            self.file_opened.writelines("News feed:")
            self.file_opened.writelines("\n\n")
    def user_input(self):
        a = "y"
        while (a == "y" or a == "Y"):
            print("############# Publisher Tool##############")
            print("Select the option you want to publish on newspaper")
            print("1.) News")
            print("2.) Private Ad")
            print("3.) Joke of the day")
            self.option = input("Enter your value")
            match self.option:
                case '1':
                    print("one")
                    self.news()
                case '2':
                    print("Two")
                    self.private_ad()
                case '3':
                    print("Three")
                    self.joke_of_day()
            a = input("Do you want to continue or not(Y/N)")
        self.file_opened.close()

    def news(self):
        news_detail = input("Enter the news detail")
        city = input("Enter the city")
        now = datetime.now()
        news_date = now.strftime("%Y-%m-%d %H:%M:%S")
        print(news_date)
        self.data_into_file(news_detail, city=city, news_date=news_date)

    def data_into_file(self, Details=None, **kwargs):
        self.file_opened.writelines("\n")
        if (self.option == "1"):
            self.file_opened.writelines("\nNews -----------------------------")
            self.file_opened.writelines("\n" + Details)
            self.file_opened.writelines("\n" + kwargs.get('city') + "," + kwargs.get('news_date'))
        elif (self.option == "2"):
            self.file_opened.writelines("\nPrivate Ad -----------------------------")
            self.file_opened.writelines("\n" + Details)
            self.file_opened.writelines("\nActual until: " + str(kwargs.get('tmp_expired_date'))
                                        + "," + str(kwargs.get("days"))+" days left")
        else:
            self.file_opened.writelines("\nJoke of the day -----------------------------")
            self.file_opened.writelines("\n" + Details)
            self.file_opened.writelines("\nFunny Meter - "+kwargs.get("rating")+"/10")

    def private_ad(self):
        ad_detail = input("Enter the ad Details")
        expired_date = input("Enter the expired date of the ad in format(YYYY-mm-dd)")
        now = datetime.now()
        current_date = now.date()
        print(expired_date)
        print(current_date)
        tmp_expired_date = datetime.strptime(expired_date, "%Y-%m-%d")
        tmp_current_date = datetime.strptime(str(current_date), "%Y-%m-%d")

        while (tmp_expired_date < tmp_current_date):
            expired_date = input("Past Date is entered , Please enter the valid date")
            tmp_expired_date = datetime.strptime(expired_date, "%Y-%m-%d")
        days = tmp_expired_date - tmp_current_date
        self.data_into_file(Details=ad_detail, tmp_expired_date=tmp_expired_date.date(), days=days.days)
    def joke_of_day(self):
        joke_detail=input("Enter the joke of the day")
        rating=input("Enter the rating of the joke out of 10")
        self.data_into_file(Details=joke_detail,rating=rating)


pub = Publisher()
pub.user_input()
