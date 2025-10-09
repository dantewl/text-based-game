#text based game
import time
import random

def say(text, delay=2):
    print(text)
    time.sleep(delay)

def battle(enemy_name, enemy_hp, player_hp):
    say(f"\n ⚔️ A {enemy_name} appears!", 2)
    say("Akira grips her staff firmly. Her silver hair moves with the cold wind.", 2)

    while enemy_hp > 0 and player_hp > 0:
        print(f"\n🧙 Akira HP: {player_hp} | {enemy_name} HP: {enemy_hp}")
        print("Choose your action:")
        print("1. Attack")
        print("2. Defend")
        print("3. Use relic power")
        action = input("> ")

        if action == "1" or action.lower() == "attack":
            dmg = random.randint(5, 12)
            enemy_hp -= dmg
            say(f"You strike the {enemy_name} for {dmg} damage!")
            say('Akira: "Time always takes something back..."', 2)

        elif action == "2" or action.lower() == "defend":
            block = random.randint(3, 8)
            say(f"You defend yourself. You’ll block up to {block} damage this turn.", 2)

        elif action == "3" or action.lower() == "use relic power":
            relic_dmg = random.randint(10, 18)
            say("The Heart of Eternity glows softly in your hand...", 2)
            say(f"You release a burst of temporal energy that hits the {enemy_name} for {relic_dmg} damage!", 2)
            enemy_hp -= relic_dmg
            cost = random.randint(3, 9)
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
        say('Akira: "Even victory feels... empty."', 2)
        return True


def chapter0():
    say("🌲 Chapter 0 – The Echo of the Second Relic 🌲", 3)
    say("The forest is calm, yet strange echoes move through the air.", 2.5)
    say("Akira walks carefully, guided by the faint glow of her relic — The Heart of Eternity.", 2.5)
    say("Each step she takes disturbs the mist that clings to the ground.", 2.5)
    say("Her silver hair shines faintly under the moonlight, her eyes calm but distant.", 2.5)
    say("Suddenly, she feels it... another source of temporal energy nearby.", 2.5)
    say("She follows it until she reaches the ruins of an ancient altar.", 2.5)
    say("On top of it lies a small glass hourglass, glowing faintly with golden light.", 2.5)
    say("Its sand flows upward, defying gravity.", 2.5)
    say("A soft voice whispers in her mind: 'Would you change what was never meant to be undone?'", 2.5)

    say('Akira lowers her gaze, whispering: "The past... always calling to those who regret."', 2.5)

    choice = input("\nWill Akira touch the relic? (yes/no): ").lower()
    
    if choice == "yes":
        say("As her fingers touch the glass, the air trembles.", 2.5)
        say("The ruins shimmer for a moment... time itself bends.", 2.5)
        say("But something awakens within the flow — a guardian of the past!", 2.5)
        say('Akira: "So, you were left behind to protect the Hourglass of Ages."', 2.5)
        win = battle("Time-Worn Guardian", enemy_hp=35, player_hp=40)

        if win:
            say("The hourglass pulses softly in her hands.", 2.5)
            say('Akira: "The past listens... and remembers."', 2.5)
            say('A whisper follows: "One more relic remain... The Tears of Fate."', 2.5)
            say("Akira glances at the sky... the stars move slower, as if watching her.", 2.5)
            say('"The second echo has been heard."', 2.5)
            return True
        else:
            say("The flow of time resets. The relic waits again in silence.", 2.5)
            return False

    elif choice == "no":
        say("Akira steps back, her relic pulsing faintly in warning.", 2.5)
        say('"I’ve seen what happens when mortals defy time."', 2.5)
        say("She turns away, disappearing into the fog.", 2.5)
        say('"Not everything should be changed."', 2.5)
        return True
    else:
        say("The wind howls softly. The relic fades into dust.", 2.5)
        say("And time keeps its secret... for now.", 2.5)
        return True

def chapter1():
    say("🌌 Chapter I – The Whisper of the Future 🌌", 3)
    say("After defeating the Time-Worn Guardian, Akira feels a shift in the air.", 2.5)
    say("The Heart of Eternity pulses with a new rhythm, resonating with the echoes of time.", 2.5)
    say("She knows the journey is far from over.", 2.5)
    say("Guided by the whispers of her two relics, she ventures deeper into the forest.", 2.5)
    say("The trees seem to part for her, revealing a hidden village", 2.5)
    say("The villagers look at her covered with a black cloak.", 2.5)
    say("She walks to the center of the village, where an bar stands.", 2.5)
    say("Inside, she sees a group of people drinking and laughing.", 2.5)
    say("Akira approaches the bar, her presence drawing curious glances.", 2.5)
    say("Bartender: \"What'll it be, traveler?\" ", 2.5)
    say("Akira: \"Just a moment of warmth...\" ", 2.5)
    say("As she sips her drink, she pays the bartender and goes outside.", 2.5)
    say("The night air is cool against her skin, a stark contrast to the warmth of the bar.", 2.5)
    say("Akira takes a deep breath, feeling the weight of her journey ahead.", 2.5)
    say("Suddenly, a chill runs down her spine. She senses a presence watching her.", 2.5)
    say("A group of men from the bar approach her, their intentions unclear.", 2.5)
    say("Leader: \"Well, well, what do we have here? A lost little lamb?\" ", 2.5)
    say("Akira: \"I’m not lost. Just passing through.\" ", 2.5)
    say("Leader: \"You look like you could use some company... or maybe something more.\" ", 2.5)
    say("Akira: \"I suggest you leave me be.\" ", 2.5)
    say("Leader: \"Or what? You’ll use that shiny trinket of yours?\" ", 2.5)
    say("Akira: \"You better not test me.\" ", 2.5)
    say("The air crackles with tension as the men close in.", 2.5)
    say("Leader: \"You’re in our territory now. Hand over that relic, and maybe we’ll let you walk away.\" ", 2.5)
    say("Akira: \"I wanna see you try.\" ", 2.5)
    say("With a swift motion, Akira grips her staff, the Heart of Eternity glowing faintly.", 2.5)
    say("Leader: \"Let me see how brave you are little lamb!\" ", 2.5)
    
    win = battle("Village Thug", enemy_hp=30, player_hp=40)

    if win:
        say("Akira stands victorious, the thugs retreating in fear.", 2.5)
        say("Leader: \"This isn’t over, girl!\" ", 2.5)
        say("Akira: \"Maybe not. But I’m not the one who should be afraid.\"", 2.5)
        say("She watches them disappear into the night, her grip tightening on the Heart of Eternity.", 2.5)
        say("Akira: \"I should find some place to rest.\"", 2.5)
        say("As she walks through the village, she sees a small inn with a warm light glowing from the windows.", 2.5)
        say("She enters, hoping to find some respite after the thugs.", 2.5)
        say("Inside, the inn is cozy, filled with the scent of wood smoke and baked bread.", 2.5)
        say("The innkeeper looks up as she enters.", 2.5)
        say("Innkeeper: \"Welcome, traveler. What brings you to our humble inn?\" ", 2.5)
        say("Akira: \"Just seeking a moment of peace...\" ", 2.5)
        say("Innkeeper: \"You’ve come to the right place. We have a room upstairs if you need it.\" ", 2.5)
        say("Akira: \"Thank you. I’ll take it.\" ", 2.5)
        say("She climbs the stairs to a small room, the bed looking inviting after her long journey.", 2.5)
        say("As she lies down, the weight of her relics feels heavier than ever.", 2.5)
        say("Akira: \"I'm close... I can feel it.\" ", 2.5)
        say("She closes her eyes, hoping for a moment of rest before the next leg of her journey.", 2.5)
        say("As sleep takes her, visions of the past and future swirl in her mind.", 2.5)
        say("In her dreams, she sees the Hourglass of Ages, its sands slipping away.", 2.5)
        say("A shadowed figure looms over it, whispering secrets of time.", 2.5)
        say("Akira: \"Who are you?...\" ", 2.5)
        say("The figure remains silent, its presence both ominous and intriguing.", 2.5)
        say("The figure: \"Always remember, you cannot change your fate.\" ", 2.5)
        say("The figure laughs evilly as the vision fades.", 2.5)
        say("Akira wakes gasping, the room still and quiet.", 2.5)
        say("Akira: \"What was that?\" ", 2.5)
        say("She clutches the Heart of Eternity, its warmth a small comfort against the cold fear creeping into her heart.", 2.5)
        say("Akira: \"I need to find the Tear of Fate... before it’s too late.\" ", 2.5)
        say("Akira goes understairs to pay the innkeeper.", 2.5)
        say("Innkeeper: \"Did you sleep well?\" ", 2.5)
        say("Akira: \"As well as I could. Here’s your payment.\" ", 2.5)
        say("Innkeeper: \"Thank you. Safe travels, Akira.\" ", 2.5)
        say("Akira: \"I appreciate your kindness. Have a nice day.\" ", 2.5)
        say("Akira steps outside, the morning sun casting a golden light over the village.", 2.5)
        say("As she walks through the center of the village, she notices the townsfolk going about their daily routines.", 2.5)
        say("Akira reveals her silver hair and winter-colored eyes, standing out among the villagers.", 2.5)
        say("Enchnanted by Akira's beauty, a few villagers stop to stare, whispering among themselves.", 2.5)
        say("She feels their eyes on her, feeling embarrassed.", 2.5)
        say("A fancy old woman approaches her, rounded by bodyguards", 2.5)
        say("Akira thinks to herself: \"Why is she approaching me?\" ", 2.5)
        say("A fancy young lady: \"You there, with the silver hair. Come, we should talk.\" ", 2.5)
        say("Akira: \"Who are you? Why do you want to talk to me?\" ", 2.5)
        say("Fancy young lady says something to her bodyguards and start walking away.", 2.5)
        say("A few bodyguards approach Akira, surrounding her.", 2.5)
        say("Akira: \"What do you guys want?\" ", 2.5)
        say("Leader of the bodyguards: \"The Queen wants to talk with you. Right now\" ", 2.5)
        say("Akira realizes that the fancy young lady is The Princess", 2.5)
        say("Akira: \"I don’t want any trouble.\" ", 2.5)
        say("Leader of the bodyguards: \"You don’t have a choice.\" ", 2.5)
        say("Akira: \"Fine...\" ", 2.5)
        say("Without choice. Akira follows The Queen surrounded by bodyguards to the castle.", 2.5)
        say("Inside the castle, Akira is led to a grand hall where The Queen awaits.", 2.5)
        say("The Queen: \"Welcome, Akira. I've heard much about you.\" ", 2.5)
        say("Akira: \"I don’t know why I’m here. I just want to be left alone.\" ", 2.5)
        say("The Queen: \"Oh, but you see, I have a proposition for you.\" ", 2.5)
        say("Akira: \"I’m listening.\" ", 2.5)
        say("The Queen: \"My sources told me they have spotted a young gifted mage... Carrying a silver hair...\"", 2.5)
        say("The Queen: \"I believe that mage is you.\" ", 2.5)
        say("Akira: \"What do you want from me?\" ", 2.5)
        say("The Queen smiles mysteriously.", 2.5)
        say("The Queen says: \"My sources said you've beat the Leader of the thugs... isn't it... admirable?\" ", 2.5)
        say("Akira: \"Yes, a complete stupid man, what next?\" ", 2.5)
        say("The Queen: \"I have a proposition for you...\" ", 2.5)
        say("The Queen: \"Join us. Work for me, and I can offer you protection, resources, and a place in my court.\" ", 2.5)
        say("Akira: \"Could you clarify it?\" ", 2.5)
        say("The Queen explains: \"With your powers and my influence, we could achieve great things together, dear.\" ", 2.5)
        say("Akira: \"What type of things?\" ", 2.5)
        say("The Queen: \"Oh, the usual... expanding my realm, dealing with troublesome nobles...\" ", 2.5)
        say("Akira: \"What would be my function?\" ", 2.5)
        say("The Queen: \"You would be my personal mage, using your powers to assist me in my rule.\" ", 2.5)
        say("Akira: \"Assisting you with?...\" ", 2.5)
        say("The Queen: \"Oh, you know... the usual...\" ", 2.5)
        say("Akira: \"What is the usual?\" ", 2.5)
        say("The Queen: \"Protecting me...  \" ", 2.5)
        say("Akira: \"So, you want me to be your... enforcer?\" ", 2.5)
        say("The Queen: \"If you put it that way... yes.\" ", 2.5)
        say("Akira: \"I'm not sure...\" ", 2.5)
        say("The Queen: \"You'll never have a better opportunity than this.\" ", 2.5)
        
        choice1 = input("\nWill Akira accept the Queen's offer? (yes/no): ").lower()
        
        if choice1 == "yes":
            say("Akira takes a deep breath, considering the offer.", 2.5)
            say("Akira: \"Alright, I will join you. But on my terms.\" ", 2.5)
            say("The Queen smiles, pleased with the decision.", 2.5)
            say("The Queen: \"Excellent choice, Akira. Let's prepare the ceremony!.\" ", 2.5)
            say("Akira feels a mix of apprehension and determination as she steps into her new role.", 2.5)
            say("Akira: \"I hope I made the right choice...\" ", 2.5)
            say("Akira sees a lot of servants and bodyguards. They are preparing the ceremony.", 2.5)
            say("The Queen: Guards! Show her her new room! ", 2.5)
            say("Akira is led to a lavish room adorned with silks and jewels.", 2.5)
            say("Akira: \"This is... quite the change from the forest.\" ", 2.5)
            say("The Queen: \"You deserve the best, Akira. Welcome to your new life.\" ", 2.5)
            say("Akira: \"Thank you, I guess.\" ", 2.5)
            say("As she settles into her new surroundings, Akira can't help but wonder what the future holds.", 2.5)
            say("A servant knocks Akira's door", 2.5)
            say("Servant: \"Mistress, your bath is ready.\" ", 2.5)
            say("Akira: \"Thank you. I’ll be there shortly.\" ", 2.5)
            say("Akira takes a deep breath, \"I'm definitely not used to this life...\" ", 2.5)
            say("As she steps into the bath, she feels the weight of her decision settling in.", 2.5)
            say("Akira: \"What have I gotten myself into?\" ", 2.5)
            say("The only hearable sound is the gentle splashing of water.", 2.5)
            say("Akira: \"Just one more relic, \" ", 2.5)
            say("And I put an end to all of this...", 2.5)
            say("Akira closes her eyes, trying to find some peace amidst the uncertainty of her new life.", 2.5)
            say("Akira finishes her bath and gets dressed.", 2.5)
            say("As she steps out of her room, she is greeted by the Queen herself.", 2.5)
            say("The Queen: \"I trust you found everything to your liking?\" ", 2.5)
            say("Akira: \"Kind of it. I usually prefer dark colors, but it's nice...\" ", 2.5)
            say("The Queen: \"I thought you might. Now, we have much to discuss about your new role.\" ", 2.5)
            say("Akira: \"Yes, I suppose we do.\" ", 2.5)
            say("The Queen: \"First, since you are ready for the ceremony, follow me.\" ", 2.5)
            say("Akira follows the Queen to a grand hall where the ceremony will take place.", 2.5)
            say("The hall is filled with nobles and courtiers, all eager to see the new royal mage.", 2.5)
            say("The Queen: \"Everyone, please welcome Akira, our new royal mage!\" ", 2.5)
            say("The crowd applauds as Akira steps forward, feeling the weight of their gazes.", 2.5)
            say("Akira: \"Thank you all for your warm welcome.\" ", 2.5)
            say("The Queen: \"Now, let us begin the ceremony.\" ", 2.5)
            say("As the ceremony begins, Akira can't help but feel a mix of excitement and apprehension about her new life.", 2.5)
            say("Akira stays alone drinking some water.", 2.5)
            say("Suddenly, a nobelman approaches her.", 2.5)
            say("Nobleman: \"You must be the new royal mage. I've heard much about you.\" ", 2.5)
            say("Akira: \"And you are?\" ", 2.5)
            say("Nobleman: \"Just a humble servant of the crown. But I must say, your beauty is as enchanting as your powers.\" ", 2.5)
            say("Akira: \"Thank you for your kind words.\" ", 2.5)
            say("Nobleman: \"Perhaps we could get to know each other better?\" ", 2.5)
            say("Akira: \"As a royal mage, I must maintain a professional distance.\" ", 2.5)
            say("Nobleman: \"Of course, I understand. But if you ever change your mind...\" ", 2.5)
            say("Akira: \"Thank you but I'm not interested in a relationship right now.\" ", 2.5)
            say("Nobleman: \"Very well. I respect your decision.\" ", 2.5)
            say("The nobleman walks away, leaving Akira to her thoughts.", 2.5)
            say("Akira: \"Everytime...\" ", 2.5)
            say("The Queen approaches her.", 2.5)
            say("The Queen: \"How are you finding your new role so far?\" ", 2.5)
            say("Akira: \"It's... different. But I'm adapting.\" ", 2.5)
            say("The Queen: \"Good to hear. Remember, you are now part of the royal family.\" ", 2.5)
            say("Akira: \"I understand.\" ", 2.5)
            say("The Queen: \"Now, I have another proposition for you.\" ", 2.5)
            say("Akira: \"What is it?\" ", 2.5)
            say("The Queen: \"There's a matter of state that requires your unique skills.\" ", 2.5)
            say("Akira: \"I'm listening.\" ", 2.5) 
            say("The Queen: \"There's a rival kingdom that has been causing trouble. I need you to use your powers to help us gain an advantage.\" ", 2.5)
            say("Akira: \"What kind of advantage?\" ", 2.5)
            say("The Queen: \"I need you to infiltrate their ranks and gather information.\" ", 2.5)
            say("Akira: \"You want me to spy for you?\" ", 2.5)
            say("The Queen: \"Precisely. Your abilities make you the perfect candidate for this task.\" ", 2.5)
            say("Akira: \"This is a dangerous mission. Why me?\" ", 2.5)
            say("The Queen: \"Because you are loyal and capable. I trust you, Akira.\" ", 2.5)
            say("Akira: \"I need some time to think about it.\" ", 2.5)
            say("The Queen: \"Of course. Take all the time you need. But remember, this mission is crucial for our kingdom's safety.\" ", 2.5)
            say("Akira: \"I understand. I'll consider it.\" ", 2.5)

        
        
        elif choice1 == "no":
            say("Akira shakes her head firmly.", 2.5)
            say("Akira: \"I cannot accept your offer. I value my freedom too much.\" ", 2.5)
        
        else:
            say("Unexpected input.", 2.5)
            return False
    
    
    else:
        say("Akira falls to the ground, the world fading to black.", 2.5)
        say("Leader: \"Looks like we found ourselves a new toy.\" ", 2.5)
        say("The relic is taken from her, its power now in the hands of those who do not understand it.", 2.5)
        say("And so, the journey ends...", 2.5)

print("✨ Welcome to Relics of Time ✨")
startgame = int(input("Start the game (1)   Exit (2): "))

if startgame == 1:
    say("In a world where time and magic are one, only a few dare to change fate.", 2.5)
    say("Chronos, the God of Time, forged three relics to control all creation.", 2.5)
    say("⏳ The Hourglass of Ages – The power of the Past.", 2.5)
    say("❤️  The Heart of Eternity – The power of the Present.", 2.5)
    say("💧 The Tear of Fate – The power of the Future.", 2.5)
    say("The Keeper of the Heart of Eternity, Akira, a young mage born with a rare gift.", 2.5)
    say("Her relic allows her to see glimpses of the near future, but at a cost.", 2.5)
    say("Every vision drains her strength, leaving her weaker each time.", 2.5)
    say("People say her eyes hold the color of winter, and her hair shines like silver light.", 2.5)
    say("She searches for the ancient Relics of Time... perhaps not for power, but for answers.", 2.5)
    say("Her journey begins in a quiet forest, where her relic whispers through the wind.", 2.5)
    chapter0_result = chapter0()

    say("\n\n--- End of Chapter 0 ---\n\n", 3)
    
    if chapter0_result:
        chapter1()
    else:
        print("Game Over.")
elif startgame == 2:
    print("You have closed the game.")
else:
    print("Unexpected input. Exiting...")
    print("Unexpected input. Exiting...")
