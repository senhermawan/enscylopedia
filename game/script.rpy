# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.
default randquizz = []
default quizlist = ["q1","q2","q3","q4","q5"]
init python:
    def randomizequiz(quizlists):
        new_quizzt = []
        eligble_quizz = quizlists
        for i in range(0,3):
            new_quizz = renpy.random.choice(eligble_quizz)
            new_quizzt.append(new_quizz)
            eligble_quizz.remove(new_quizz)
        return new_quizzt
label start:
    $randquizz = randomizequiz(quizlist)
    call expression randquizz[0]
    call expression randquizz[1]
    call expression randquizz[2]
    return
