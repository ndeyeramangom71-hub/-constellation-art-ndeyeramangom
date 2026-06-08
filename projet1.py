#projet Rama

import turtle

#--- Configuration de l'écran ---
#creation de la fenetre
ecran = turtle.Screen()
#couleur de l'arriére plan 
ecran.bgcolor("#1a1a2e")  # Bleu nuit
#titre de la fenetre 
ecran.title("Constellation : Le Cheval Complet")

#creation de notre curseur 
stylo = turtle.Turtle()
#couleur du trait
stylo.color("#68DDDD") 
 #l'epaisseur du trait à 4pixel
stylo.pensize(4) 
 # Vitesse du stylo 
stylo.speed(3)  

#reation de la liste 

cheval_complet = [
    # -- Le bout du nez (point de départ) --
    (100, -20),

    # -- Mâchoire et poitrail --
    (108, -28), (105, -38), (90, -42), (60, -30), (35, -45), (10, -100),

    # -- Patte avant --
    (15, -150), (20, -200), (10, -210), (0, -210), (5, -150),

    # -- Ventre --
    (-30, -130), (-70, -130),

    # -- Patte arrière --
    (-90, -150), (-85, -200), (-95, -210), (-105, -210), (-100, -150), (-120, -100),

    # -- Cuisse et Queue --
    (-140, -60), (-160, -100), (-180, -150), (-170, -80), (-150, -40),

    # -- Croupe et Dos --
    (-130, -20), (-80, -30), (-40, -20),

    # -- Encolure (Crinière) --
    (-30, 30), (-20, 60),

    # -- Oreilles et Front --
    (-5, 105), (5, 75), (15, 80), (20, 95), (25, 70), (35, 50), (70, 15), (95, -5),

    # -- Retour au museau pour fermer le dessin --
    (100, -20)
]


#lever du stylo dans la fenetre
stylo.penup()

# On va directement au premier point (le nez) sans faire de trait depuis le centre
stylo.goto(cheval_complet[0][0], cheval_complet[0][1])
#pose du stylo
stylo.pendown()

print("Tracé du cheval en cours...")

for coord in cheval_complet:
    # Déplacement vers le point (x, y)
    stylo.goto(coord[0], coord[1])
    # Dessin de l'étoile le point de la constellation
    stylo.dot(5, "gold")

# --- Fin
stylo.hideturtle()
ecran.exitonclick()