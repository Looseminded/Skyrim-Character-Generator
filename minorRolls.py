# Skyrim Character / Scenario Generator - minorRolls.py
# Written and tested in Python 3.7.7
import string
import random

system_random = random.SystemRandom()

#difficulty = startPerkPoints = addHealth = addHealRate = addHealRateMult = addStamina = addStamRate = addStamRateMult = addMagicka = addMagickaRate = addMagickaRateMult = addSpeed = addWSpeed = addWDamage = addCrit = addUnarmed = addShoutRecovery = addAlteration = addConjuration = addDestruction = addIllusion = addRestoration = addEnchanting = addDisease = addPoison = addFire = addShock = addFrost = addMagic = ""

def chooseDifficulty():	
	diffList = ['Adept', 'Expert', 'Master', 'Legendary']
	pickedDiff = system_random.choice(diffList)
	return pickedDiff
	print("Difficulty: " + pickedDiff)

def chooseDragonSouls():
	pickedDragonSouls = random.randint(0, 5)
	return pickedDragonSouls
	print("Starting Dragon Souls: " + str(pickedDragonSouls))
	
def chooseHealth():
	pickedHealth = random.randint(-20, 20)
	return pickedHealth
	print("Modified Health: " + pickedHealth)
	
def chooseHealRate():
	pickedHealRate = random.randint(-20, 20)
	formattedHealRate = "{:.2f}".format(pickedHealRate / 100)
	return formattedHealRate
	print("Modified Heal Rate: " + formattedHealRate)
	
def chooseHealRateMult():
	pickedHRateMult = random.randint(-35, 35)
	return pickedHRateMult
	print("Modified Heal Mult: " + pickedHRateMult)

def chooseStamina():
	pickedStamina = random.randint(-20, 20)
	return pickedStamina
	print("Modified Stamina: " + pickedStamina)
	
def chooseStamRate():
	pickedStamRate = random.randint(-20, 20)
	formattedStamRate = "{:.2f}".format(pickedStamRate / 100)
	return formattedStamRate
	print("Modified Stamina Rate: " + formattedStamRate)
	
def chooseStamMult():
	pickedStamMult = random.randint(-35, 35)
	return pickedStamMult
	print("Modified Stamina Rate: " + pickedStamMult)

def chooseMagicka():
	pickedMagicka = random.randint(-20, 20)
	return pickedMagicka
	print("Modified Magicka: " + pickedMagicka)
	
def chooseMagickaRate():
	pickedMagickaRate = random.randint(-20, 20)
	formattedMagickaRate = "{:.2f}".format(pickedMagickaRate / 100)
	return formattedMagickaRate
	print("Modified Magicka Rate: " + formattedMagickaRate)
	
def chooseMagickaMult():
	pickedMagickaMult = random.randint(-35, 35)
	return pickedMagickaMult
	print("Modified Magicka Rate: " + pickedMagickaMult)
	
def chooseSpeed():
	pickedSpeed = random.randint(-20, 20)
	return pickedSpeed
	print("Modified Speed Mult: " + pickedSpeed)
	
def chooseWSpeed():
	pickedWSpeed = random.randint(-20, 20)
	formattedWSpeed = "{:.2f}".format(pickedWSpeed / 100)
	baseValue = float(formattedWSpeed)
	baseValue += 1.0
	formattedWSpeed = "{:.2f}".format(baseValue)
	return formattedWSpeed
	print("Modified Weapon Speed: " + formattedWSpeed)
	
def chooseADamage():
	pickedADamage = random.randint(-35, 35)
	formattedADamage = "{:.2f}".format(pickedADamage / 100)
	return formattedADamage
	print("Modified Attack Damage: " + formattedADamage)
	
def chooseCrit():
	pickedCrit = random.randint(0, 10)
	return pickedCrit
	print("Modified Crit Chance: " + pickedCrit)
	
def chooseUnarmed():
	pickedUnarmed = random.randint(0, 10)
	return pickedUnarmed
	print("Modified Unarmed Damage: " + pickedUnarmed)
	
def chooseShoutMult():
	pickedShoutMult = random.randint(-30, 30)
	formattedShoutMult = "{:.2f}".format(pickedShoutMult / 100)
	return formattedShoutMult
	print("Modified Shout Mult: " + formattedShoutMult)
	
def chooseAlteration():
	pickedAlteration = random.randint(-15, 15)
	return pickedAlteration
	print("Modified Alteration Power: " + pickedAlteration)
	
def chooseConjuration():
	pickedConjuration = random.randint(-15, 15)
	return pickedConjuration
	print("Modified Conjuration Power: " + pickedConjuration)
	
def chooseDestruction():
	pickedDestruction = random.randint(-15, 15)
	return pickedDestruction
	print("Modified Destruction Power: " + pickedDestruction)
	
def chooseIllusion():
	pickedIllusion = random.randint(-15, 15)
	return pickedIllusion
	print("Modified Illusion Power: " + pickedIllusion)
	
def chooseRestoration():
	pickedRestoration = random.randint(-15, 15)
	return pickedRestoration
	print("Modified Restoration Power: " + pickedRestoration)
	
def chooseEnchanting():
	pickedEnchanting = random.randint(-25, 25)
	return pickedEnchanting
	print("Modified Enchanting Power: " + pickedEnchanting)
	
def chooseDisease():
	pickedDisease = random.randint(-10, 10)
	return pickedDisease
	print("Modified Disease Resist: " + pickedDisease)
	
def choosePoison():
	pickedPoison = random.randint(-10, 10)
	return pickedPoison
	print("Modified Poison Resist: " + pickedPoison)
	
def chooseFire():
	pickedFire = random.randint(-10, 10)
	return pickedFire
	print("Modified Fire Resist: " + pickedFire)
	
def chooseShock():
	pickedShock = random.randint(-10, 10)
	return pickedShock
	print("Modified Shock Resist: " + pickedShock)
	
def chooseFrost():
	pickedFrost = random.randint(-10, 10)
	return pickedFrost
	print("Modified Frost Resist: " + pickedFrost)
	
def chooseMagic():
	pickedMagic = random.randint(-10, 10)
	return pickedMagic
	print("Modified Magic Resist: " + pickedMagic)
	
def chooseAbsorb():
	pickedAbsorb = random.randint(0, 5)
	return pickedAbsorb
	print("Modified Absorb Chance: " + pickedAbsorb)