class twit:

    def user(self):
        user = open('user.txt')
        user_total = user.read()
        u_linum = user.readlines()
        for line in user:
            line = line[0:-1]
        self.total_user =(int)(user_total.count('\n')/4)
        print("Total user : "+str(self.total_user))

        wd = open('word.txt')
        wd_total = wd.read()
        wd_linum = wd.readlines()
        for line in wd:
            line = line[0:-1]
        self.total_twit =(int)(wd_total.count('\n')/4)
        print("Total tweets : "+str(self.total_twit))
        
    def main(self):
    
        print("0. Read data files\n"+
            "1. display statistics\n"+
            "2. Top 5 most tweeted words\n"+
            "3. Top 5 most tweeted users\n"+
            "4. Find users who tweeted a word (e.g., ’연세대’)\n"+
            "5. Find all people who are friends of the above users\n"+
            "6. Delete all mentions of a word\n"+
            "7. Delete all users who mentioned a word\n"+
            "8. Find strongly connected components\n"+
            "9. Find shortest path from a given user\n"+
            "99. Quit\n"+
            "Select Menu:")
        select=(int)(input())
        if select==0:
            self.user()
        else:
            print("wrong input")

t=twit()

t.main()
