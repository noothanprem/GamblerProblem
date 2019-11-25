import random
class Gambler:
	STARTING_STAKE_AMOUNT = 100
	bet_amount = 1
	daily_stake_amount = STARTING_STAKE_AMOUNT
	won_count=lose_count=0
	win_percentage=lose_percentage=0
	def win_or_lose(self):
		self.daily_stake_amount=STARTING_STAKE_AMOUNT
		half_percentage = (self.STARTING_STAKE_AMOUNT*50)/100
		self.win_percentage = self.STARTING_STAKE_AMOUNT + half_percentage
		self.lose_percentage = self.STARTING_STAKE_AMOUNT - half_percentage
		print("daily stake amount at first: ",self.daily_stake_amount)
		print("win percentage at first : ",self.win_percentage)
		print("Lose percentage : ",self.lose_percentage)
		while(self.daily_stake_amount < self.win_percentage and self.daily_stake_amount > self.lose_percentage):
			print("Inside while loop")
			random_number = random.random()
			bet_amount = 1
			if(random_number < 0.5):
				self.daily_stake_amount += bet_amount
			else:
				self.daily_stake_amount -= bet_amount
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
	
			amount_difference = final_stake_amount - STARTING_STAKE_AMOUNT
			print("amount difference : ",amount_difference)
			total_amount += amount_difference
				
			print("day :",day_count)
			days_list.append(total_amount)
			day_count += 1
	
		if(total_amount > 0):
			print("You won in this motnh, continue with the next mont")
			return self.count_days()
		else:
			print("You lose in this month, ending the game")
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

	def  luckiest_and_unluckiest_day(self):
		daily_amount_list=self.count_days()
		print("daily amount list",daily_amount_list)
		max_amount = 0
		min_amount = 0
		max_amount_index = 0
		min_amount_index = 0
		for daily_amount_list_index in range(len(daily_amount_list)):
			if daily_amount_list[daily_amount_list_index] > max_amount :
				max_amount = daily_amount_list[daily_amount_list_index]
				max_amount_index = daily_amount_list_index
			elif daily_amount_list[daily_amount_list_index] < min_amount :
				min_amount = daily_amount_list[daily_amount_list_index]
				min_amount_index = daily_amount_list_index
		print("Luckiest day : ",max_amount_index + 1,"with an amount of : ",max_amount)
		print("Unluckiest day :",min_amount_index + 1,"with an amount of :",min_amount)

		
				
			
		
		
	
if __name__ == "__main__":
	gambler_object=Gambler()
	gambler_object.daily_won_lose()
	gambler_object.luckiest_and_unluckiest_day()
	


