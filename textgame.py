# Relics of Time – Chapter 1: The Echo of the First Relic
import time
import random

def say(text, delay=2):
    print(text)
    time.sleep(delay)

def battle(enemy_name, enemy_hp, player_hp):
    say(f"\n⚔️ A {enemy_name} appears!", 2)
    say("Akira grips her staff firmly. Her silver hair moves with the cold wind.", 2)

    while enemy_hp > 0 and player_hp > 0:
        print(f"\n🧙 Akira HP: {player_hp} | {enemy_name} HP: {enemy_hp}")
        print("Choose your action:")
        print("1. Attack")
        print("2. Defend")
        print("3. Use relic power")
        action = input("> ")

        if action == "1":
            dmg = random.randint(5, 12)
            enemy_hp -= dmg
            say(f"You strike the {enemy_name} for {dmg} damage!")
            say('Akira: "Time always takes something back..."', 2)

        elif action == "2":
            block = random.randint(3, 8)
            say(f"You defend yourself. You’ll block up to {block} damage this turn.", 2)

        elif action == "3":
            relic_dmg = random.randint(10, 18)
            say("The Heart of Eternity glows softly in your hand...", 2)
            say(f"You release a burst of temporal energy that hits the {enemy_name} for {relic_dmg} damage!", 2)
            enemy_hp -= relic_dmg
            cost = random.randint(3, 6)
            player_hp -= cost
            say(f"The power drains your strength. You lose {cost} HP.", 2)
            say('Akira: "The present consumes me... every time."', 2)

        else:
            say("You hesitate and lose your focus.", 2)

        if enemy_hp <= 0:
            break

        enemy_dmg = random.randint(4, 10)
        say(f"The {enemy_name} attacks!", 2)
        player_hp -= enemy_dmg
        say(f"You take {enemy_dmg} damage.", 2)

    if player_hp <= 0:
        say("Akira falls to her knees. The Heart of Eternity slips from her hand.", 2)
        say('"Maybe... this is how my time ends."', 2)
        return False
    else:
        say(f"The {enemy_name} collapses. The forest grows silent once again.", 2)
        say('Akira: "Even victory feels... heavy."', 2)
        return True


def chapter1():
    say("🌲 Chapter I – The Echo of the First Relic 🌲", 3)
    say("The forest is calm, yet strange echoes move through the air.", 2.5)
    say("Akira walks carefully, guided by the faint glow of her relic — The Heart of Eternity.", 2.5)
    say("Each step she takes disturbs the mist that clings to the ground.", 2.5)
    say("Her silver hair shines faintly under the moonlight, her eyes calm but distant.", 2.5)
    say("Suddenly, she feels it — another source of temporal energy nearby.", 2.5)
    say("She follows it until she reaches the ruins of an ancient altar.", 2.5)
    say("On top of it lies a small glass hourglass, glowing faintly with golden light.", 2.5)
    say("Its sand flows upward, defying gravity.", 2.5)
    say("A soft voice whispers in her mind: 'Would you change what was never meant to be undone?'", 2.5)

    say('Akira lowers her gaze, whispering: "The past... always calling to those who regret."', 2.5)

    choice = input("\nWill Akira touch the relic? (yes/no): ").lower()
    
    if choice == "yes":
        say("As her fingers touch the glass, the air trembles.", 2.5)
        say("The ruins shimmer for a moment — time itself bends.", 2.5)
        say("But something awakens within the flow — a guardian of the past!", 2.5)
        say('Akira: "So, you were left behind to protect the Hourglass of Ages."', 2.5)
        win = battle("Time-Worn Guardian", enemy_hp=35, player_hp=40)

        if win:
            say("The hourglass pulses softly in her hands.", 2.5)
            say('Akira: "The past listens... and remembers."', 2.5)
            say('A whisper follows: "One more relic remain... The Tears of Fate."', 2.5)
            say("Akira glances at the sky... the stars move slower, as if watching her.", 2.5)
            say('"The first echo has been heard."', 2.5)
        else:
            say("The flow of time resets. The relic waits again in silence.", 2.5)

    elif choice == "no":
        say("Akira steps back, her relic pulsing faintly in warning.", 2.5)
        say('"I’ve seen what happens when mortals defy time."', 2.5)
        say("She turns away, disappearing into the fog.", 2.5)
        say('"Not everything should be changed."', 2.5)
    else:
        say("The wind howls softly. The relic fades into dust.", 2.5)
        say("And time keeps its secret... for now.", 2.5)


print("✨ Welcome to Relics of Time ✨")
startgame = int(input("Start the game (1)   Exit (2): "))

if startgame == 1:
    say("In a world where time and magic are one, only a few dare to change fate.", 2.5)
    say("Chronos, the God of Time, forged three relics to control all creation.", 2.5)
    say("⏳ The Hourglass of Ages – The power of the Past.", 2.5)
    say("❤️ The Heart of Eternity – The power of the Present.", 2.5)
    say("💧 The Tear of Fate – The power of the Future.", 2.5)
    say("The Keeper of the Heart of Eternity is Akira, a young mage born with a rare gift.", 2.5)
    say("Her relic allows her to see glimpses of the near future, but at a cost.", 2.5)
    say("Every vision drains her strength, leaving her weaker each time.", 2.5)
    say("People say her eyes hold the color of winter, and her hair shines like silver light.", 2.5)
    say("She searches for the ancient Relics of Time... perhaps not for power, but for answers.", 2.5)
    say("Her journey begins in a quiet forest, where her relic whispers through the wind.", 2.5)
    chapter1()

elif startgame == 2:
    print("You have closed the game.")
else:
    print("Unexpected input. Exiting...")
