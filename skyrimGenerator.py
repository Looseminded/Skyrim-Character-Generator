# Skyrim Character / Scenario Generator
# Written and tested in Python 3.7.7

import string
import random
import os
import time

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
		
		minor = input("Would you like to roll additional or lower minor stats and difficulty?\n(Health, regen rate, damage, etc.) (y/n)\n")
		
		if(minor == 'y'):
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
				print("Difficulty: " + diff)
				print("Starting Dragon Souls: " + str(startDS))
				print("Modified Health: " + str(health))
				print("Modified Heal Rate: " + str(healRate) + "%")
				print("Modified Heal Mult: " + str(healMult) + "%")
				print("Modified Stamina: " + str(stamina))
				print("Modified Stamina Rate: " + str(stamRate) + "%")
				print("Modified Stamina Mult: " + str(stamMult) + "%")
				print("Modified Magicka: " + str(magicka))
				print("Modified Magicka Rate: " + str(magickaRate) + "%")
				print("Modified Magicka Mult: " + str(magickaMult) + "%")
				print("Modified Speed: " + str(speed) + "%")
				print("Modified Weapon Speed: " + str(wSpeed))
				print("Modified Attack Damage: " + str(aDamage) + "%")
				print("Modified Crit Chance: " + str(crit) + "%")
				print("Modified Unarmed Damage: " + str(unarmed))
				print("Modified Shout Recovery Mult: " + str(shoutMult))
				print("Modified Alteration Power: " + str(alteration) + "%")
				print("Modified Conjuration Power: " + str(conjuration) + "%")
				print("Modified Destruction Power: " + str(destruction) + "%")
				print("Modified Illusion Power: " + str(illusion) + "%")
				print("Modified Restoration Power: " + str(restoration) + "%")
				print("Modified Enchanting Power: " + str(enchanting) + "%")
				print("Modified Disease Resist: " + str(disease) + "%")
				print("Modified Poison Resist: " + str(poison) + "%")
				print("Modified Fire Resist: " + str(fire) + "%")
				print("Modified Shock Resist: " + str(shock) + "%")
				print("Modified Frost Resist: " + str(frost) + "%")
				print("Modified Magic Resist: " + str(magic) + "%")
				print("Modified Absorb Chance: " + str(absorb) + "%")
			except Exception as f:
				print("File does not exist or something is broken.  Skipping...")
				pass
		elif(minor == 'n'):
			pass
		else:
			print("Invalid input, passing.\n")
		
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
			if(minor == 'y'):
				fo.write("\nDifficulty: " + diff)
				fo.write("\nStarting Dragon Souls: " + str(startDS))
				fo.write("\nModified Health: " + str(health))
				fo.write("\nModified Heal Rate: " + str(healRate) + "%")
				fo.write("\nModified Heal Mult: " + str(healMult) + "%")
				fo.write("\nModified Stamina: " + str(stamina))
				fo.write("\nModified Stamina Rate: " + str(stamRate) + "%")
				fo.write("\nModified Stamina Mult: " + str(stamMult) + "%")
				fo.write("\nModified Magicka: " + str(magicka))
				fo.write("\nModified Magicka Rate: " + str(magickaRate) + "%")
				fo.write("\nModified Magicka Mult: " + str(magickaMult) + "%")
				fo.write("\nModified Speed: " + str(speed) + "%")
				fo.write("\nModified Weapon Speed: " + str(wSpeed))
				fo.write("\nModified Attack Damage: " + str(aDamage) + "%")
				fo.write("\nModified Crit Chance: " + str(crit) + "%")
				fo.write("\nModified Unarmed Damage: " + str(unarmed))
				fo.write("\nModified Shout Recovery Mult: " + str(shoutMult))
				fo.write("\nModified Alteration Power: " + str(alteration) + "%")
				fo.write("\nModified Conjuration Power: " + str(conjuration) + "%")
				fo.write("\nModified Destruction Power: " + str(destruction) + "%")
				fo.write("\nModified Illusion Power: " + str(illusion) + "%")
				fo.write("\nModified Restoration Power: " + str(restoration) + "%")
				fo.write("\nModified Enchanting Power: " + str(enchanting) + "%")
				fo.write("\nModified Disease Resist: " + str(disease) + "%")
				fo.write("\nModified Poison Resist: " + str(poison) + "%")
				fo.write("\nModified Fire Resist: " + str(fire) + "%")
				fo.write("\nModified Shock Resist: " + str(shock) + "%")
				fo.write("\nModified Frost Resist: " + str(frost) + "%")
				fo.write("\nModified Magic Resist: " + str(magic) + "%")
				fo.write("\nModified Absorb Chance: " + str(absorb) + "%")
			else:
				pass
			fo.close()
			print("\nFile saved as " + filename + ".txt at " + str(os.getcwd()))
			makefile = input("\nWould you like to generate a .txt file to run in Skyrim's\nconsole to make the changes for you? (y/n)\n")
			if(makefile == 'y'):
				fname = "skyrimModified.txt"
				fi = open(fname, "w")
				fi.write("player.modav dragonsouls " + str(startDS))
				fi.write("\nplayer.modav health " + str(health))
				fi.write("\nplayer.modav healrate " + str(healRate))
				fi.write("\nplayer.modav healratemult " + str(healMult))
				fi.write("\nplayer.modav stamina " + str(stamina))
				fi.write("\nplayer.modav staminarate " + str(stamRate))
				fi.write("\nplayer.modav staminaratemult " + str(stamMult))
				fi.write("\nplayer.modav magicka " + str(magicka))
				fi.write("\nplayer.modav magickarate " + str(magickaRate))
				fi.write("\nplayer.modav magickaratemult " + str(magickaMult))
				fi.write("\nplayer.modav speedmult " + str(speed))
				fi.write("\nplayer.modav weaponspeedmult " + str(wSpeed))
				fi.write("\nplayer.modav attackdamagemult " + str(aDamage))
				fi.write("\nplayer.modav critchance " + str(crit))
				fi.write("\nplayer.modav unarmeddamage " + str(unarmed))
				fi.write("\nplayer.modav shoutrecoverymult " + str(shoutMult))
				fi.write("\nplayer.modav alterationpowermod " + str(alteration))
				fi.write("\nplayer.modav conjurationpowermod " + str(conjuration))
				fi.write("\nplayer.modav destructionpowermod " + str(destruction))
				fi.write("\nplayer.modav illusionpowermod " + str(illusion))
				fi.write("\nplayer.modav restorationpowermod " + str(restoration))
				fi.write("\nplayer.modav enchantingpowermod " + str(enchanting))
				fi.write("\nplayer.modav diseaseresist " + str(disease))
				fi.write("\nplayer.modav poisonresist " + str(poison))
				fi.write("\nplayer.modav fireresist " + str(fire))
				fi.write("\nplayer.modav electricresist " + str(shock))
				fi.write("\nplayer.modav frostresist " + str(frost))
				fi.write("\nplayer.modav magicresist " + str(magic))
				fi.write("\nplayer.modav absorbchance " + str(absorb))
				fi.close()
			else:
				pass
			print("\nFile saved as " + fname + " at " + str(os.getcwd()))
			print("Make sure you move this file into your Skyrim folder.")
			print("Afterwards, if playing Vanilla, you can run 'bat skyrimModified' once you're out of\nHelgen.")
			print("If playing with mods, I'd recommend waiting until you're at your first major city or\ntown.")
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