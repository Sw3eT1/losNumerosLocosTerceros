from time import sleep

mainDecision = False

wzory = ["f(x) = 3x-2", "f(x)=|x-2|", "f(x)=x^3-4x^2+x+6", "f(x)=sin(x)", "f(x)=sin(x^2)"]

while not mainDecision:

    print(f'Chose a proper function:'
          f'\n a) {wzory[0]}'
          f'\n b) {wzory[1]}'
          f'\n c) {wzory[2]}'
          f'\n d) {wzory[3]}'
          f'\n e) {wzory[4]}')

    val = input("Select your option: ").lower()

    properOptions = ["a", "b", "c", "d", "e"]

    if val not in properOptions:
        if val == "":
            print("You have entered an empty string!")
        else:
            print("Invalid input!")
            sleep(1)
    else:
        mainDecision = True