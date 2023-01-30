# Skyrim Character / Scenario Generator
# Written and tested in Python 3.7.7

import string
import random
import os
import time

system_random = random.SystemRandom()

def main():
	try:
		chosenRace = chosenBirthsign = chosenFocus = chosenFactions = chosenWar = chosenWeapons = chosenShields = chosenArmor = chosenDawnguard = chosenHome = chosenFollower = chosenTheft = chosenMurder = ""
		chosenRace = chooseRace()
		chosenBirthsign = chooseBirthsign()
		chosenFocus = chooseFocus()
		chosenFactions = chooseFactions()
		chosenWar = chooseWar()
		chosenWeapons = chooseWeapons()
		chosenShields = chooseShields()
		chosenArmor = chooseArmor()
		chosenDawnguard = chooseDawnguard()
		chosenHome = chooseHome()
		chosenFollower = chooseFollower()
		chosenTheft = chooseTheft()
		chosenMurder = chooseMurder()
		print("Race: " + chosenRace)
		print("Birthsign: " + chosenBirthsign)
		print("Skills to focus: " + str(chosenFocus))
		print("Factions required: " + str(chosenFactions))
		print("Civil War Side: " + chosenWar)
		print("Weapons to use: " + str(chosenWeapons))
		print("Shields available: " + chosenShields)
		print("Armor available: " + chosenArmor)
		print("Dawnguard Side: " + chosenDawnguard)
		print("Player home: " + chosenHome)
		print("Companion: " + chosenFollower)
		print("Freelance Theft: " + chosenTheft)
		print("Murder Targets: " + chosenMurder)
		print("\n")
		
		save = input("Would you like to save your results to a file? (y/n)\n")
		
		if(save == 'y'):
			filename = input("\nPlease type the name you'd like to save your file as: \n")
			fo = open(filename + ".txt", "w")
			fo.write("Race: " + chosenRace + "\n")
			fo.write("Birthsign: " + chosenBirthsign + "\n")
			fo.write("Skills to focus: " + str(chosenFocus))
			fo.write("\nFactions required: " + str(chosenFactions))
			fo.write("\nCivil War Side: " + chosenWar + "\n")
			fo.write("Weapons to use: " + str(chosenWeapons))
			fo.write("\nShields available: " + chosenShields + "\n")
			fo.write("Armor available: " + chosenArmor + "\n")
			fo.write("Dawnguard Side: " + chosenDawnguard + "\n")
			fo.write("Player home: " + chosenHome + "\n")
			fo.write("Companion: " + chosenFollower + "\n")
			fo.write("Freelance Theft: " + chosenTheft + "\n")
			fo.write("Murder Targets: " + chosenMurder + "\n")
			fo.close()
			print("\nFile saved as " + filename + ".txt at " + str(os.getcwd()))
			time.sleep(10)
			exit()
		elif(save == 'n'):
			exit()
	except Exception as e:
		print("Something's not right...")
		print(e)
	
def chooseRace():
	race = ['Altmer (High Elf)', 'Argonian', 'Bosmer (Wood Elf)', 'Breton', 'Dunmer (Dark Elf)', 'Imperial', 'Khajiit', 'Nord', 'Orsimer (Orc)', 'Redguard']
	pickedRace = system_random.choice(race)
	return pickedRace
	
def chooseBirthsign():
	birthsign = ['Apprentice', 'Atronach', 'Lady', 'Lord', 'Lover', 'Mage', 'Ritual', 'Serpent', 'Shadow', 'Steed', 'Thief', 'Tower', 'Warrior']
	pickedBirthsign = system_random.choice(birthsign)
	return pickedBirthsign
	
def chooseFocus():
	countFocus = entryLoop()
	pickedFocus = ''
	skillList = ['Alteration', 'Conjuration', 'Destruction', 'Enchanting', 'Illusion', 'Restoration', 'Archery', 'Block', 'Heavy Armor', 'One-Handed', 'Smithing', 'Two-Handed', 'Alchemy', 'Light Armor', 'Lockpicking', 'Pickpocket', 'Sneak', 'Speech']
	pickedFocus = random.sample(skillList, countFocus)
	return pickedFocus
	
def chooseFactions():
	x = random.randint(2, 5)
	factionList = ['Bards College', 'The Blades', 'The Greybeards', 'College of Winterhold', 'The Companions', 'The Coven of Namira', 'House Telvanni', 'The Dark Brotherhood', 'The Nightingales (Thieves\' Guild)', 'Tribal Orcs']
	pickedFactions = random.sample(factionList, x)
	return pickedFactions
	
def chooseWar():
	warFactions = ['Imperials', 'Stormcloaks', 'Nobody']
	pickedWar = system_random.choice(warFactions)
	return pickedWar
	
def chooseWeapons():
	x = random.randint(2, 3)
	weaponsList = ['Bows and Crossbows', 'Daggers', 'Maces and Warhammers', 'Swords and Greatswords', 'War Axes and Battleaxes', 'Destruction Magic', 'Conjuration Magic', 'Restoration Magic']
	pickedWeapons = random.sample(weaponsList, x)
	return pickedWeapons
	
def chooseShields():
	shieldsList = ['Light', 'Heavy', 'None']
	pickedShield = system_random.choice(shieldsList)
	return pickedShield
	
def chooseArmor():
	armorList = ['Light Armor', 'Heavy Armor', 'Robes', 'Clothes']
	pickedArmor = system_random.choice(armorList)
	return pickedArmor
	
def chooseDawnguard():
	dgList = ['Dawnguard', 'Volkihar', 'Player\'s choice']
	pickedDG = system_random.choice(dgList)
	return pickedDG
	
# This is exceptionally hard to be thorough with. "A joined faction base" will, for example,
# include the Arch-Mage's Quarters at the College of Winterhold, if that is one of your chosen factions.
def chooseHome():
	homeList = ['A joined faction base', 'Breezehome (Whiterun)', 'Honeyside (Riften)', 'Vlindrel Hall (Markarth)', 'Hjerim (Windhelm)', 'Proudspire Manor (Solitude)', 'Heljarchen Hall (Dawnstar)', 'Lakeview Manor (Falkreath)', 'Windstad Manor (Morthal)', 'Severin Manor (Dragonborn, in Raven Rock)', 'Modded, or player\'s choice']
	pickedHome = system_random.choice(homeList)
	return pickedHome
	
def chooseFollower():
	followerList = ['Argis the Bulwark', 'Calder', 'Gregor', 'Iona', 'Jordis the Sword-Maiden', 'Lydia' ,'Rayya', 'Valdimar', 'Brelyna Maryon', 'J\'zargo', 'Onmund', 'Aela the Huntress', 'Athis', 'Farkas', 'Njada Stonearm', 'Ria', 'Torvar', 'Vilkas', 'Cicero', 'Dark Brotherhood Initiate (Male or Female)', 'Ingjard (Dawnguard)', 'Durak (Dawnguard)', 'Agmaer (Dawnguard)', 'Beleval (Dawnguard)', 'Celann (Dawnguard)', 'Belrand', 'Erik the Slayer', 'Jenassa', 'Marcurio', 'Stenvar', 'Teldryn Sero (Dragonborn)', 'Vorstag', 'Adelaisa Vendicci', 'Ahtar', 'Annekke Crag-Jumper', 'Aranea Ienith', 'Eola', 'Erandur', 'Faendal', 'Frea (Dragonborn)', 'Golldir', 'Illia', 'Kharjo', 'Lob', 'Mjoll the Lioness', 'Ogol', 'Ralis Sedarys (Dragonborn)', 'Roggi Knot-Beard', 'Serana (Dawnguard)', 'Sven', 'Talvas Fathryon (Dragonborn)', 'Ugor', 'Benor', 'Borgakh the Steel Heart', 'Cosnach', 'Derkeethus', 'Ghorbash the Iron Hand', 'Uthgerd the Unbroken', 'Modded or Player\'s choice']
	pickedFollower = system_random.choice(followerList)
	return pickedFollower

def chooseTheft():
	theftList = ['Always', 'Habitual', 'Never', 'When Provoked', 'When Required', 'Rarely']
	pickedTheft = system_random.choice(theftList)
	return pickedTheft

def chooseMurder():
	murderList = ['When Aggressive', 'When Provoked', 'When Necessary', 'Never', 'Always (Player\'s Choice)', 'Avoid if Possible']
	pickedMurder = system_random.choice(murderList)
	return pickedMurder
	
def entryLoop():
	countFocus = 0
	countFocus = int(input("How many skills would you like to focus on? (Between 3 and 6)\n"))
	if(countFocus < 3):
		print("Too few skills chosen, please pick again.\n")
		return entryLoop()
	elif(countFocus > 6):
		print("Too many skills chosen, please pick again.\n")
		return entryLoop()
	else:
		return countFocus
	
if __name__ == "__main__":
	main()