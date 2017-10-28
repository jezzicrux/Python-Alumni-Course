from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Circus(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You were lunched into a lava pit!",
        "Someone told you the funniest joke in the world and died laughing",
        "And now for something completely different.",
        "Nobody expects the Spanish Inquisition!",
        "You where blown up by the Holy Hand Grenade of Antioch"
         ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class SpamRoom(Scene):

    def enter(self):
        print(dedent("""
        Hello and welcome to the Flying Circus. You can travel the
        next few rooms, but I warn you...things could get a bit werid.
        I'm sure you can handle it though.

        Anyways, would you like something to eat? We've got Egg and bacon,
        Egg, sausage and bacon, Egg and Spam, Egg, bacon and Spam,
        Egg, bacon, sausage and Spam, Spam, bacon, sausage and Spam,
        Spam, egg, Spam, Spam, bacon and Spam, Spam, Spam, Spam, egg and Spam,
        Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam, or
        Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté,
        brandy and a fried egg on top, and Spam.
        """))

        action = input(">> ")

        if action == str.lower("spam"):
            print(dedent("""
            Which Spam! Egg and Spam, Egg, bacon and Spam,
            Egg, bacon, sausage and Spam, Spam, bacon, sausage and Spam,
            Spam, egg, Spam, Spam, bacon and Spam, Spam, Spam, Spam, egg and Spam,
            Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam, or
            Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté,
            brandy and a fried egg on top, and Spam.
            """))
            second_choice = input(">> ")
            if second_choice == str.lower("spam"):
            	print(dedent("""Alright! Stop That! It's gotten much too silly!"""))
            	return 'death'
            else:
            	print(dedent("""We're all out of that. Why don't you just go the parrot room?

            	You are pretty much forced in a low lit room with nothing in it
        		but a bird cage. You walk up to the bird cage and see a blue parrot."""))
            	return 'the_Parrot_Room'

        elif action == str.lower("chicken"):
            print(dedent("""
            CHICKEN! Don't come here with that posh talk, you nasty,
            stuck-up twit! Here! Take your chicken and leave!

            You need to go to the Parrot Room.

            You are pretty much forced in a low lit room with nothing in it
        	but a bird cage. You walk up to the bird cage and see a blue parrot
        	standing proud on his perch.
            """))
            return 'the_Parrot_Room'

        elif action == str.lower("I don't like spam"):
            print(dedent("""
            You don't like spam! BEGONE WITH YOU!!
            """))
            return 'death'

        else:
            print("We interrupt this program to annoy you and make things generally irritating.")
            return 'the_spam_room'

class ParrotRoom(Scene):

    welcomes = [
        """[Parrot] Waark! Call this a bleedin voyage? More like a bleedin'
        disaster if you ask me! Woo! What have we hit now? What have we hit
        now? Oh! Bang! There we go again! Hit something else now have we?
        What do you expect if a ship's got no brain!""",
        """[Parrot] You are entering parrot space! Ticket please! Show your
        passports! Get a blooby move on! Give us a nut, give us a nut,
        give us a bloody pistachio""",
        """[Parrot] Hey you! Sorry about your home. If you need somewhere to
        stay, I've got a lovely cage going cheap! or it would be going cheap if
        it was a chicken. Haha. Parrot humor! Don't you just love it!"""
        """[Parrot] Ah! The bearer of chickens I don't think!"""]

    Randomness = [
        """[Parrot] No point talking to me, I don't do smalltalk. Got more
        important things on my mind. Parrot thing. Stuff you wouldn't know
        about. Not if for human contemplation, hur whur. Squawk!""",
        """[Parrot] Questions? Questions? No point in talking to me, I'm
        just a parrot!"""
        """[Parrot] What did you say? What did you say? You come here and
        say that. No, better still, go away and say that. I don't want to
        hear any opinion of yours that isn't accompanied by good solid
        chucks of steaming chicken!"""
        """[Parrot] Won't do you any good! Won't do me any good, which
        is more to the point! No chickens in there! No pistachio nuts either!
        What good's about anything that is totally devoid of chicken or
        pistachio nuts? Waar!"""]

    def enter(self):
        print(ParrotRoom.welcomes[randint(0, len(self.welcomes)-1)])
        print("What would like to do?")

        action = input(">> ")

        if action == str.lower("take the parrot"):
            print(dedent("""
            [Parrot] Oi! Unhand me you...you person! Stop it! I shall screech!
            I shall screech! Screeeeeccchh! Well screeeeeccchh! Don't
            say I didn't warn you! I'll peck you! Screeeeeccchh!
            Screeeeeccchh! Screeeeeccchh! Screeeeeccchh!

            You can't hold on the bird for long and he bits your finger and flys off.

            [Parrot] Ahah! Not fast enough! Squaw
            Would you like to move on?
            """))

            choice = input(">> ")
            if choice == str.lower("yes"):
                return 'the_outside'
            else:
                return 'the_Parrot_Room'

        elif action == str.lower("give the parrot chicken"):
            print(dedent("""
            [Parrot] Chicken, chicken, squawk, oh bliss! Oh
            bleeding heck, this chicken's cold! What's this,
            some sort of low-calorie fob-off? Where's the
            steaming fat? Where's the hot running grease?
            This is no chicken - this is some dirty no-good health food!

            Would you like to move on?
            """))

            choice = input(">> ")
            if choice == str.lower("yes"):
            	return 'the_outside'
            else:
            	return 'the_Parrot_Room'

        elif action == str.lower("touch the perch"):
            print(dedent("""
            [Parrot] Oi! Stop it! Stop it! I'm standing on that! Leave it alone!
            You are an icredibly rube person! I'll peck you! I'll screech!
            I'll behave abominably! You think you've seen abominable,
            but haven't! You wait till I do abominable! Squawk

            Would you like to touch the perch again?
            """))

            bothering = input(">> ")
            if bothering == str.lower("yes"):
            	print(dedent("""
            	[Parrot] You think I'm some kind of barnacled goose you can prod?
            	You think I'm some kind of bay-breasted warbler to make free what?
            	You think I'm some kind of black-belied plover you can puch off its perch!

	            Would you like to move on?
                """))
                #choice = input(">> ")
                #if choice == str.lower("yes"):
                #    return 'the_bridge'
                #else:
                #    return 'the_Parrot_Room''''
            else:
                print("Would you like to move on?")

                choice = input(">> ")
                if choice == str.lower("yes"):
                    return 'the_outside'
                else:
                    return 'the_Parrot_Room'
        else:
            print(ParrotRoom.Randomness[randint(0, len(self.Randomness)-1)])
            print("Would you like to move on?")

            choice = input(">> ")
            if choice == str.lower("yes"):
            	return 'the_outside'
            else:
            	return 'the_Parrot_Room'

class Forest(Scene):

    def enter(self):
        print(dedent("""
        Once you walked out the parrot room you're stepped
        out into the forest, even though you went though the
        same door you enter when you went to the parrot room.

        Nothing makes scene anymore

        You keep walking until see a Black Knight standing by
        a point arrow sign that says 'Exit' The knight doesn't
        say anything so you try to walk past him.

        [Black Knight] None shall pass! None shall pass!

        The knight points his sword at you. There's a sword
        next to you and you pick it up.

        What do you want to do?

        """))

        action = input(">> ")

        if action == str.lower("cut off arms"):
            print(dedent("""
            You look at the black knight with no arms. He
            can no longer fight, so yo start walking arounf him.
            Then he start kicking you.

            [Black Knight] Come on, you pansy! 'Tis but a scratch!
            I've had worse. It's just a flesh wound. Chicken! Chicken!

            What do you want to do?

	        """))

            next_action = input(">> ")
            if next_action == str.lower("cut off right leg") or next_action == str.lower("cut off left leg") or next_action == str.lower("cut off leg"):
                print(dedent("""
                [Black Knight] Right, I'll do you for that! Come 'ere!

            	The black kinght starts headbutting you. What else can
            	he do? Bleed on you? He's a loony.

            	[Black Knight] I'm invincible! The Black Knight always
            	triumphs! Have at you! Come on then.
            	What do you want to do?

			    """))

                final_action = input(">> ")
                if final_action == str.lower("cut off other leg"):
                    print(dedent("""
                    [Black Knight] All right, we'll call it a draw.

                    You start walking away.
                    [Black Knight] Oh, oh, I see, running away,
                    'eh? You yellow bastards! Come back here and
                    take what's coming to you. I'll bite your legs off!
                    """))

                    return 'the_bridge'
                else:
                    return 'death'
            else:
                return 'death'
        else:
            return 'death'

class TheBridgeofDoom(Scene):
    final_pick = ["[Bridgekeeper] What... is your favourite colour?",
    "[Bridgekeeper] What... is the capital of Assyria?"]

    def enter(self):
        print(dedent("""
        You followed the signs to the top of a mountain.
        You are starting to wonder what in the world is
        going on.

        You up ahead and see a small old man staring in front of bridge.

        [Bridgekeeper] Stop. Who would cross the Bridge of Death must answer
        me these questions three, ere the other side he see.

        Are you willing to answer the Bridgekeepers questions?
        """))

        action = input(">> ")

        if action == str.lower("yes"):
            print("[Bridgekeeper] What... is your name?")
            name = input(">> ")
            print("[Bridgekeeper] What... is your quest?")
            quest = input(">> ")
            final_chioce = (TheBridgeofDoom.final_pick[randint(0, len(self.final_pick)-1)])
            print (final_chioce)
            if final_chioce == "What... is your favourite colour?":
                colour = input(">> ")
                print("Alright. Off you go.")
            else:
                final_answer = input(">> ")
                if final_answer == str.lower("assur"):
                    print("Alright. Off you go.")
                    return 'final_room'
                else:
                    return 'death'
        elif action == str.lower("no"):
            return 'death'
        else:
            print("We interrupt this program to annoy you and make things generally irritating.")
            return "the_bridge"

class ExitRoom(Scene):

    def enter(self):
        print(dedent("""
        You have made it over the bridge and now you a piller with
        writing on it"

        'WHAT IS THE MEANING OF LIFE? THE ANSWER TO THE GREAT QUESTION...
        OF LIFE, THE UNIVERSE AND EVERYTHING'

        """))

        guess = int(input("YOUR ANSWER? "))
        turn = 0

        while turn <4:
            if guess == 42:
                print(dedent("""
                Confetti shots out the pillar and it starts
                moving up out the ground. There is now a big door
                that says 'EXIT' and you walk though it.
                """))
                return 'Finished'
            elif guess != 42 and turn == 3:
                return 'death'
            else:
                print("TRY AGAIN")
                turn = turn+1

class Finished(Scene):

    def enter(self):
        print("Congratulations! You have escaped the Flying Circus")
        print("So Long, and Thanks for All the Fish")
        return 'finished'


class Map(object):

    scenes = {
        'the_spam_room': SpamRoom(),
        'the_Parrot_Room': ParrotRoom(),
        'the_outside': Forest(),
        'the_bridge': TheBridgeofDoom(),
        'final_room': ExitRoom(),
        'death': Death(),
        'finished': Finished(),
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('the_spam_room')
a_game = Circus(a_map)
a_game.play()
