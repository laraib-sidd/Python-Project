from translate import Translator
try:
    with open("new.txt", 'r+') as file:
        text = file.readline()
        print(text)
        translator=Translator(to_lang="hi")
        translation=translator.translate(text)
        file.write(translation)
        print(file.readline())
except:
    print("file not found")
