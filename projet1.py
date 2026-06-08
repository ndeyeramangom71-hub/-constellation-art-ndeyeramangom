#projet Rama

import turtle

# je crée la fenetre d'affichage
ecran = turtle.Screen()
ecran.bgcolor("#1a1a2e")
ecran.title("Constellation : Le Cheval Complet")

# je crée le stylo pour dessiner
stylo = turtle.Turtle()
stylo.color("#68DDDD")
stylo.pensize(4)
stylo.speed(3)

# les coordonnées de chaque point du cheval
cheval_complet = [
    # le museau
    (100, -20),

    # la machoire et le poitrail
    (108, -28), (105, -38), (90, -42), (60, -30), (35, -45), (10, -100),

    # patte avant
    (15, -150), (20, -200), (10, -210), (0, -210), (5, -150),

    # le ventre
    (-30, -130), (-70, -130),

    # patte arrière
    (-90, -150), (-85, -200), (-95, -210), (-105, -210), (-100, -150), (-120, -100),

    # la queue
    (-140, -60), (-160, -100), (-180, -150), (-170, -80), (-150, -40),

    # le dos
    (-130, -20), (-80, -30), (-40, -20),

    # l'encolure
    (-30, 30), (-20, 60),

    # les oreilles et la tete
    (-5, 105), (5, 75), (15, 80), (20, 95), (25, 70), (35, 50), (70, 15), (95, -5),

    # je reviens au debut pour fermer le contour
    (100, -20)
]

# je lève le stylo pour aller au premier point sans tracer de trait
stylo.penup()
stylo.goto(cheval_complet[0][0], cheval_complet[0][1])
stylo.pendown()

print("dessin en cours...")

# je parcours tous les points un par un
for point in cheval_complet:
    stylo.goto(point[0], point[1])
    stylo.dot(5, "gold") # je dessine une petite etoile doree a chaque point

# j'écris mon prénom à côté du cheval
stylo.penup()
stylo.goto(120, 60)
stylo.color("pink")
stylo.write("Rama 🌸❤️", font=("Arial", 18, "bold"))

stylo.hideturtle()
ecran.exitonclick()