import random
class Gambler:
	starting_stake_amount = 100
	bet_amount = 1
	daily_stake_amount = 100 
	def win_or_loose(self):
		random_number = random.random()
		if(random_number < 0.5):
			self.daily_stake_amount +=1
		else:
			self.daily_stake_amount -=1
		print("current stake : ",self.daily_stake_amount)
	
if __name__ == "__main__":
	gambler_object=Gambler()
	gambler_object.win_or_loose()
	


