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
		total_amount = 0
		day_count=1
		days_list = []
		amount_difference = 0
		for day in range(20):
			
			final_stake_amount = self.win_or_lose()
			print("stake for the day : " ,final_stake_amount)
			#if(final_stake_amount > 100):
			amount_difference = final_stake_amount - 100
			print("amount difference : ",amount_difference)
			total_amount += amount_difference
				
			#else:
				#total_amount -= final_stake_amount 
				#print("You lose :",final_stake_amount)
			print("day :",day_count)
			days_list.append(total_amount)
			day_count += 1
		if(total_amount < 0):
			print("Lose : ",abs(total_amount))
		else:
			print("win : ",total_amount)
		return days_list

	def daily_won_lose(self):
		days_list=self.count_days()
		print(days_list)
		for day in range(len(days_list)):
			if(days_list[day] > 0):
				print(day+1," won ",days_list[day])
			elif(days_list[day] < 0):
				print(day+1," Lose ",abs(days_list[day]))
			else:
				print(day+1," Tie ")
			
		
				
			
		
		
	
if __name__ == "__main__":
	gambler_object=Gambler()
	gambler_object.daily_won_lose()
	


