#Author 'Ammad Younas'
import random
stored_number = random.randint(0, 1000)
class color:
	bold='\033[01m'
	blue='\033[34m'
	orange='\033[33m'
	gold='\033[33m'
	red='\033[31m'
	green='\033[32m'
	cyan='\033[36m'
	darkgrey = '\033[90m'
attempt = 1
print(color.darkgrey, "              Made By @Ammad !!!")
print(color.bold, color.blue, "Welcome to guess the number Game  b/w  1 to 1000")
print(color.orange, "            You have only 15 attempts")
while (attempt<=15):
	user_input = int(input(" Enter a Number: "))
	if user_input < stored_number:
		print(color.gold, "Enter Greater Number and attempt left:", 15-attempt)
	elif user_input > stored_number:
		print(color.red, "Enter Lesser Number and attempt left:", 15-attempt)
	else:
		print(color.green ,"Congratulation ! You Win the Game In", attempt, "Attempt")
		break
	attempt = attempt + 1
if (attempt>15):
	print(color.cyan, "         Game over")
	print(color.cyan, "You Have Run Out Of Attempts")
	print("  The Stored number Was", [stored_number])