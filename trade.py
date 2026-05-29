import random
import time
def trade_action(self):
        country = ["China", "England", "Ottoman", "Safavid", "Mughal", "Spain", "Mali" , "Mongols"]
        test_country = random.choice(country)
        max_mat = self.natural_resources
        max_wealth = self.wealth
        trade_mat = random.randint(1, max_mat)
        trade_wealth = random.randint(1, max_wealth)
        military = self.military
        lost_mat= random.randint(1,10)
        lost1= random.randint(1,10)
        armydied = random.randint(1, military)

        print(f"{test_country} would like to trade with you for materials and spices")
        print(f"1. Trade with {test_country}...You will lose {trade_mat} wood and iron but increase wealth by {trade_wealth}")
        print("2. no deal")

        choice1_ = input("> ")

        if choice1_ == "1":
            if max_mat >= trade_mat:
                self.natural_resources -= trade_mat 
                self.wealth+= trade_wealth 
                print(f"{test_country} was extremely pleased with the trade and would like to become an alliance. You will gain 1-10 silver coins everyday in exchange for 10-20 wood material. Do you accept to the conditions? Yes or No")
                choice1_ = input(">")
                
                if choice1_.lower() == "yes":
                    tradealliance = True
                    self.trade.append(f"{test_country}")


                else: 

                    print(f"{test_country} is extremely mad and attempted to colonize you...")
                    time.sleep(3)
                    print(f"Luckily you survived but {armydied} army has died trying to defend u...  ")

                    self.military -= armydied


                        


            else:
                print("You dont have enough resources for the trade. ")

        elif choice1_ == "2":

            print(f"{test_country} was extremely mad and attempted to steal from u. you lost {lost_mat} wood/metal and {lost1} military trying to defend")

            self.military -= lost1
            self.natural_resources -= lost1

        else:
            print("Invalid decision.")
