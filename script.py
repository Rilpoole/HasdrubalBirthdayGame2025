'''
Title: Happy Birthday Hasdrubal

Synopsis:
Riley needs to use his shitty white car to pick up Jonny and Daniel to get to Hasdrubal’s house for his birthday. But, when they get there he's not home. They search all over town, eventually finding him at Spud's and bringing him back to play a game of Apples to Apples where Riley cheats and Jonny and Daniel pretend not to notice. 

basic scripting tutorial: 
https://www.youtube.com/watch?v=C3Ldd-5PKCw

renpy offical docs:
https://www.renpy.org/doc/html/index.html
'''

# Declare characters

r = character("Riley")

# Begin narative

label start:

    scene bg OutsideRileyWorkEvening

    play music "SunflowerDrag.mp3"

    show riley bored

    r "My job is to extract money out of people for things they don't need..."
    r "Helping people sucks."

    show riley happy

    r "But. I've looked forward to this all week. I'm going to see Hasdrubal and the guys!"

    show riley bored

    r "But. This shit car. Should I clean the trash out for Daniel and Jonny?" 

    menu:   
        "Yes": 
            r "Alright. All clean."
            default clean_car = True
        "No":
            r "Jerk."
            default clean_car = False


            






