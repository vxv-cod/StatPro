def setv():
    with open("version.txt", 'r',  encoding='utf-8') as file:
        text = file.read()
        text = int(text) + 1
    with open("version.txt", 'w',  encoding='utf-8') as file:
        file.write(str(text))
    with open("version.py", "w") as file:
        ver = f"ver = {text}"
        file.write(ver)
setv()