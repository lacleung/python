from stegano import lsb

secret = "5 letter word that becomes shorter when you add 2 letters to it"

hide = lsb.hide("./IMG_9357.png", secret)
print(hide)
hide.save("./secret.png")
