name=input("enter name:")
print("hello" + name + "lets play hangman!")

secret_word="melike"

guess_string="" 
"""burada guess_word ü global tanımladık ki altta her yerde kullanabilelim"""

lives=10

while lives>0:

	character_left=0
"""character_left:geriye kalan bilinecek harf demek"""
	
	for character in secret_word:

		if character in guess_string:
			print(character)

		else:
			print("_")
			character_left+=1

	if character_left==0:
		print("you won!!!")
		break

	guess=input("guess a word:")
	guess_string+=guess

	if guess not in secret_word:
		lives-=1
		print("wrong!!!")
		print(f"you have {lives} left")

		if lives==0:
			print("you died!!!")
