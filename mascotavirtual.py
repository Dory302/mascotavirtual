nombre = "Waffle"
energia=100
felicidad=100
print(f"energia inicial de: {nombre},energia:{energia},felicidad:{felicidad}")
while energia > 0 :
    print("¿Que quieres hacer:?")
    print("1.- alimentar")
    print("2.- jugar")
    print("3.- ver estado de salud")
    print("4.- no hacer nada")
    opcion = input("Seleccione:")
    if opcion == "1":
        energia = energia +20
        felicidad= felicidad+1
        print(f"Alimentaste a {nombre}, esta muy feliz contigo..")
    elif opcion =="2":
        energia = energia -15
        felicidad = felicidad+20
        print(f"{nombre} esta cansado pero feliz de jugar contigo")
    elif opcion =="3":
        print("     /\_              /\_____/\ ")
        print("    (    @\___       ( o  .  o )")
        print("    /         O      (_________)")
        print("   /     (____/           |     ")
        print("  /_______/               |____ ")
        print(f"energia:{energia}")
        print(f"felicidad:{felicidad}")
    elif opcion =="4":
        felicidad=felicidad-10
        energia=energia-5
        print(f"{nombre}esta muy aburrido....")
    else:
        print("error de ingreso")