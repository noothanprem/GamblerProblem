import random
class Gambler:
	starting_stake_amount = 100
	bet_amount = 1
	daily_stake_amount = 100 
	won_count=lose_count=0
	win_percentage=lose_percentage=0
	def win_or_lose(self):
		self.daily_stake_amount=100
		self.win_percentage = self.starting_stake_amount + (self.starting_stake_amount/2)
		self.lose_percentage = self.starting_stake_amount / 2
		self.won_count=self.lose_count=0
		print("daily stake amount at first: ",self.daily_stake_amount)
		print("win percentage at first : ",self.win_percentage)
		print("Lose percentage : ",self.lose_percentage)
		while(self.daily_stake_amount < self.win_percentage and self.daily_stake_amount > self.lose_percentage):
			print("Inside while loop")
			random_number = random.random()
			if(random_number < 0.5):
				self.daily_stake_amount += 1
			else:
				self.daily_stake_amount -=1
			print("current stake : ",self.daily_stake_amount)
		print("End of the day")	
		self.win_percentage=self.lose_percentage=0
		return self.daily_stake_amount
		
	def count_days(self):
		day_count=1
		for day in range(20):
			
			final_stake_amount = self.win_or_lose()
			print("stake for the day : " ,final_stake_amount)
			if(final_stake_amount > 100):
				print("You Won : ",final_stake_amount)
			else:
				print("You lose :",final_stake_amount)
			print("day :",day_count)
			day_count += 1
				
			
		
		
	
if __name__ == "__main__":
	gambler_object=Gambler()
	gambler_object.count_days()
	


