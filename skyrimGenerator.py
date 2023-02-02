# Skyrim Character / Scenario Generator
# Written and tested in Python 3.7.7

import string
import random
import os
import time
from pathlib import Path

path = Path('./minorRolls.py')
system_random = random.SystemRandom()

def main():
	try:
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
		print(f"Race: {chosenRace}")
		print(f"Birthsign: {chosenBirthsign}")
		print(f"Skills to focus: {chosenFocus}")
		print(f"Factions required: {chosenFactions}")
		print(f"Civil War Side: {chosenWar}")
		print(f"Weapons to use: {chosenWeapons}")
		print(f"Shields available: {chosenShields}")
		print(f"Armor available: {chosenArmor}")
		print(f"Dawnguard Side: {chosenDawnguard}")
		print(f"Player home: {chosenHome}")
		print(f"Companion: {chosenFollower}")
		print(f"Freelance Theft: {chosenTheft}")
		print(f"Murder Targets: {chosenMurder}")
		print(f"\n")
		
		if(path.is_file()):
			minor = input("Would you like to roll additional or lower minor stats and difficulty?\n(Health, regen rate, damage, etc.) (y/n)\n")
		
			if(minor is 'y'):
				try:
					import minorRolls
					diff = minorRolls.chooseDifficulty()
					startDS = minorRolls.chooseDragonSouls()
					health = minorRolls.chooseHealth()
					healRate = minorRolls.chooseHealRate()
					healMult = minorRolls.chooseHealRateMult()
					stamina = minorRolls.chooseStamina()
					stamRate = minorRolls.chooseStamRate()
					stamMult = minorRolls.chooseStamMult()
					magicka = minorRolls.chooseMagicka()
					magickaRate = minorRolls.chooseMagickaRate()
					magickaMult = minorRolls.chooseMagickaMult()
					speed = minorRolls.chooseSpeed()
					wSpeed = minorRolls.chooseWSpeed()
					aDamage = minorRolls.chooseADamage()
					if(aDamage):
						aDamagePercentRaw = float(aDamage)
						aDamagePercentRaw *= 100
						aDamagePercent = "{:.2f}".format(aDamagePercentRaw)
					crit = minorRolls.chooseCrit()
					unarmed = minorRolls.chooseUnarmed()
					shoutMult = minorRolls.chooseShoutMult()
					alteration = minorRolls.chooseAlteration()
					conjuration = minorRolls.chooseConjuration()
					destruction = minorRolls.chooseDestruction()
					illusion = minorRolls.chooseIllusion()
					restoration = minorRolls.chooseRestoration()
					enchanting = minorRolls.chooseEnchanting()
					disease = minorRolls.chooseDisease()
					poison = minorRolls.choosePoison()
					fire = minorRolls.chooseFire()
					shock = minorRolls.chooseShock()
					frost = minorRolls.chooseFrost()
					magic = minorRolls.chooseMagic()
					absorb = minorRolls.chooseAbsorb()
					print(f"Difficulty: {diff}")
					print(f"Starting Dragon Souls: {startDS}")
					print(f"Modified Health: {health}")
					print(f"Modified Heal Rate: {healRate}%")
					print(f"Modified Heal Mult: {healMult}%")
					print(f"Modified Stamina: {stamina}")
					print(f"Modified Stamina Rate: {stamRate}%")
					print(f"Modified Stamina Mult: {stamMult}%")
					print(f"Modified Magicka: {magicka}")
					print(f"Modified Magicka Rate: {magickaRate}%")
					print(f"Modified Magicka Mult: {magickaMult}%")
					print(f"Modified Speed: {speed}%")
					print(f"Modified Weapon Speed: {wSpeed}")
					print(f"Modified Attack Damage: {aDamagePercent}%")
					print(f"Modified Crit Chance: {crit}%")
					print(f"Modified Unarmed Damage: {unarmed}")
					print(f"Modified Shout Recovery Mult: {shoutMult}")
					print(f"Modified Alteration Power: {alteration}%")
					print(f"Modified Conjuration Power: {conjuration}%")
					print(f"Modified Destruction Power: {destruction}%")
					print(f"Modified Illusion Power: {illusion}%")
					print(f"Modified Restoration Power: {restoration}%")
					print(f"Modified Enchanting Power: {enchanting}%")
					print(f"Modified Disease Resist: {disease}%")
					print(f"Modified Poison Resist: {poison}%")
					print(f"Modified Fire Resist: {fire}%")
					print(f"Modified Shock Resist: {shock}%")
					print(f"Modified Frost Resist: {frost}%")
					print(f"Modified Magic Resist: {magic}%")
					print(f"Modified Absorb Chance: {absorb}%")
				except ValueError as e:
					print(f"File does not exist or something is broken.  Skipping...")
					print(e)
					pass
			elif(minor is 'n'):
				pass
			else:
				print(f"Invalid input, passing.\n")
		else:
			pass
		
		save = input("Would you like to save your results to a file? (y/n)\n")
		
		if(save is 'y'):
			filename = input("\nPlease type the name you'd like to save your file as: \n")
			fo = open(filename + ".txt", "w")
			fo.write(f"Race: {chosenRace}\n")
			fo.write(f"Birthsign: {chosenBirthsign}\n")
			fo.write(f"Skills to focus: {chosenFocus}\n")
			fo.write(f"Factions required: {chosenFactions}\n")
			fo.write(f"Civil War Side: {chosenWar}\n")
			fo.write(f"Weapons to use: {chosenWeapons}\n")
			fo.write(f"Shields available: {chosenShields}\n")
			fo.write(f"Armor available: {chosenArmor}\n")
			fo.write(f"Dawnguard Side: {chosenDawnguard}\n")
			fo.write(f"Player home: {chosenHome}\n")
			fo.write(f"Companion: {chosenFollower}\n")
			fo.write(f"Freelance Theft: {chosenTheft}\n")
			fo.write(f"Murder Targets: {chosenMurder}\n")
			print(f"\nFile saved as {filename}.txt at {os.getcwd()}")
			fo.close()
			time.sleep(3)
			if(minor is 'y'):
				fo = open(filename + ".txt", "a")
				fo.write(f"\nDifficulty: {diff}")
				fo.write(f"\nStarting Dragon Souls: {startDS}")
				fo.write(f"\nModified Health: {health}")
				fo.write(f"\nModified Heal Rate: {healRate}%")
				fo.write(f"\nModified Heal Mult: {healMult}%")
				fo.write(f"\nModified Stamina: {stamina}")
				fo.write(f"\nModified Stamina Rate: {stamRate}%")
				fo.write(f"\nModified Stamina Mult: {stamMult}%")
				fo.write(f"\nModified Magicka: {magicka}")
				fo.write(f"\nModified Magicka Rate: {magickaRate}%")
				fo.write(f"\nModified Magicka Mult: {magickaMult}%")
				fo.write(f"\nModified Speed: {speed}%")
				fo.write(f"\nModified Weapon Speed: {wSpeed}")
				fo.write(f"\nModified Attack Damage: {aDamagePercent}%")
				fo.write(f"\nModified Crit Chance: {crit}%")
				fo.write(f"\nModified Unarmed Damage: {unarmed}")
				fo.write(f"\nModified Shout Recovery Mult: {shoutMult}")
				fo.write(f"\nModified Alteration Power: {alteration}%")
				fo.write(f"\nModified Conjuration Power: {conjuration}%")
				fo.write(f"\nModified Destruction Power: {destruction}%")
				fo.write(f"\nModified Illusion Power: {illusion}%")
				fo.write(f"\nModified Restoration Power: {restoration}%")
				fo.write(f"\nModified Enchanting Power: {enchanting}%")
				fo.write(f"\nModified Disease Resist: {disease}%")
				fo.write(f"\nModified Poison Resist: {poison}%")
				fo.write(f"\nModified Fire Resist: {fire}%")
				fo.write(f"\nModified Shock Resist: {shock}%")
				fo.write(f"\nModified Frost Resist: {frost}%")
				fo.write(f"\nModified Magic Resist: {magic}%")
				fo.write(f"\nModified Absorb Chance: {absorb}%")
				fo.close()
				
				makefile = input("\nWould you like to generate a .txt file to run in Skyrim's\nconsole to make the changes for you? (y/n)\n")
				if(makefile is 'y'):
					fname = "skyrimModified.txt"
					fi = open(fname, "w")
					fi.write(f"player.modav dragonsouls {startDS}")
					fi.write(f"\nplayer.modav health {health}")
					fi.write(f"\nplayer.modav healrate {healRate}")
					fi.write(f"\nplayer.modav healratemult {healMult}")
					fi.write(f"\nplayer.modav stamina {stamina}")
					fi.write(f"\nplayer.modav staminarate {stamRate}")
					fi.write(f"\nplayer.modav staminaratemult {stamMult}")
					fi.write(f"\nplayer.modav magicka {magicka}")
					fi.write(f"\nplayer.modav magickarate {magickaRate}")
					fi.write(f"\nplayer.modav magickaratemult {magickaMult}")
					fi.write(f"\nplayer.modav speedmult {speed}")
					fi.write(f"\nplayer.modav weaponspeedmult {wSpeed}")
					fi.write(f"\nplayer.modav attackdamagemult {aDamage}")
					fi.write(f"\nplayer.modav critchance {crit}")
					fi.write(f"\nplayer.modav unarmeddamage {unarmed}")
					fi.write(f"\nplayer.modav shoutrecoverymult {shoutMult}")
					fi.write(f"\nplayer.modav alterationpowermod {alteration}")
					fi.write(f"\nplayer.modav conjurationpowermod {conjuration}")
					fi.write(f"\nplayer.modav destructionpowermod {destruction}")
					fi.write(f"\nplayer.modav illusionpowermod {illusion}")
					fi.write(f"\nplayer.modav restorationpowermod {restoration}")
					fi.write(f"\nplayer.modav enchantingpowermod {enchanting}")
					fi.write(f"\nplayer.modav diseaseresist {disease}")
					fi.write(f"\nplayer.modav poisonresist {poison}")
					fi.write(f"\nplayer.modav fireresist {fire}")
					fi.write(f"\nplayer.modav electricresist {shock}")
					fi.write(f"\nplayer.modav frostresist {frost}")
					fi.write(f"\nplayer.modav magicresist {magic}")
					fi.write(f"\nplayer.modav absorbchance {absorb}")
					fi.close()
					print(f"\nFile saved as {fname} at {os.getcwd()}\n")
					print(f"Make sure you move this file into your Skyrim folder.")
					print(f"Afterwards, if playing Vanilla, you can run 'bat skyrimModified'\nonce you're out of Helgen.")
					print(f"If playing with mods, I'd recommend waiting until you're at your\nfirst major city or town.")
				else:
					pass
			else:
				pass
			time.sleep(5)
			exit()
		elif(save is 'n'):
			exit()
	except ValueError as v:
		print(f"Something's not right...")
		print(v)
	
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
		print(f"Too few skills chosen, please pick again.\n")
		return entryLoop()
	elif(countFocus > 6):
		print(f"Too many skills chosen, please pick again.\n")
		return entryLoop()
	else:
		return countFocus
	
if __name__ == "__main__":
	main()