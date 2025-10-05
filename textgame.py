# As Relics of Time – Chapter 1: The Echo of the First Relic
import time
import random

def say(text, delay=2):
    print(text)
    time.sleep(delay)

def battle(enemy_name, enemy_hp, player_hp):
    say(f"\n⚔️ A wild {enemy_name} appears!", 2)
    say("You ready your staff, feeling the weight of the relic pulsing with energy...", 2)
    
    while enemy_hp > 0 and player_hp > 0:
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Defend")
        print("3. Use relic power")
        action = input("> ")

        if action == "1":
            dmg = random.randint(5, 12)
            enemy_hp -= dmg
            say(f"You strike with your staff and deal {dmg} damage!")
        elif action == "2":
            block = random.randint(3, 8)
            say(f"You brace yourself. You’ll reduce incoming damage by {block}.")
        elif action == "3":
            relic_dmg = random.randint(10, 18)
            say(f"The relic glows faintly... You unleash a surge of temporal energy!")
            say(f"It burns your veins but strikes the {enemy_name} for {relic_dmg} damage!")
            enemy_hp -= relic_dmg
            player_hp -= random.randint(3, 6)
        else:
            say("You hesitate... and lose your focus.")

        if enemy_hp <= 0:
            break

        enemy_dmg = random.randint(4, 10)
        say(f"The {enemy_name} attacks!")
        player_hp -= enemy_dmg
        say(f"You take {enemy_dmg} damage. HP left: {player_hp}")

    if player_hp <= 0:
        say("Your vision fades... The relic slips from your hand...")
        say("You have fallen.")
        return False
    else:
        say(f"The {enemy_name} collapses. Silence returns to the forest.")
        return True


def chapter1():
    say("🌲 Chapter I – The Echo of the First Relic 🌲", 3)
    say("The wind howls through the forest as Akira steps into the ruins of an ancient village.", 2.5)
    say("Scattered stone, burnt trees, and the scent of ash fill the air.", 2.5)
    say("At the center, half-buried in dust, lies a small glass hourglass...", 2.5)
    say("...the first Relic of Time.", 2.5)
    say("She reaches for it. The sand within flows upward, as if defying gravity.", 2.5)
    say("A whisper echoes in her mind: 'Would you turn back what was never meant to be undone?'", 2.5)

    choice = input("\nWill you touch the relic? (yes/no): ").lower()
    
    if choice == "yes":
        say("As your fingers brush the glass, the world blurs.", 2.5)
        say("The ashes rise, the trees reform... time reverses itself!", 2.5)
        say("But something comes with it — a guardian bound to the relic awakens!", 2.5)
        win = battle("Time-Worn Guardian", enemy_hp=30, player_hp=35)

        if win:
            say("The relic’s power settles into your hand, heavy and warm.", 2.5)
            say("You’ve tampered with time... but the cost is not yet clear.", 2.5)
            say("A voice whispers: 'Two more relics await... use them wisely.'", 2.5)
        else:
            say("Time resets. The relic waits again in the dust, patient as eternity.", 2.5)

    elif choice == "no":
        say("You step back, feeling an invisible force urging you closer.", 2.5)
        say("But you resist. The relic hums faintly, almost disappointed.", 2.5)
        say("You walk away, leaving the power untouched... for now.", 2.5)
    else:
        say("The wind answers in your silence. The relic fades into dust.", 2.5)


print("✨ Welcome to As Relics of Time ✨")
startgame = int(input("Start the game (1)   Exit (2): "))

if startgame == 1:
    say("In a world where time itself bleeds into magic...", 2.5)
    say("A young mage named Akira wanders in search of forgotten relics.", 2.5)
    say("They say each relic can command time — but at a terrible cost.", 2.5)
    say("Your journey begins in the forest where whispers of the first relic are heard.", 2.5)
    chapter1()
elif startgame == 2:
    print("You have closed the game.")
else:
    print("Unexpected input. Exiting...")
