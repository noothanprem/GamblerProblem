import random
class Gambler:
	starting_stake_amount = 100
	bet_amount = 1
	daily_stake_amount = 100 
	def win_or_loose(self):
		win_percentage = self.starting_stake_amount + (self.starting_stake_amount/2)
		lose_percentage = self.starting_stake_amount / 2
		while(self.daily_stake_amount < win_percentage and self.daily_stake_amount > lose_percentage):
			random_number = random.random()
			if(random_number < 0.5):
				self.daily_stake_amount +=1
			else:
				self.daily_stake_amount -=1
			print("current stake : ",self.daily_stake_amount)
		print("End of the day")			
		return self.daily_stake_amount
		
	def calculative_gambler(self):
		daily_stake=0
		daily_stake=self.daily_stake_amount
		
		
	
if __name__ == "__main__":
	gambler_object=Gambler()
	gambler_object.win_or_loose()
	


