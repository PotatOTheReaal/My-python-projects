def convert():
    fell=input("enter the emojie :")
    felling=fell.replace(":)","happy")
    felling2=fell.replace("):","sad")
    if fell==felling:
        print(":)")
    elif fell==felling2:
        print("):")
convert()
