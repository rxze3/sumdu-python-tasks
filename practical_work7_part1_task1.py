class FileLesson:
    def creating_file_with_text():
        f = open("TF16_1.txt", "w")
        f.write("Hello world, it is my first try to study work with files in python!")
        f.close()

    def creating_file_with_words_from_text_file():
        f = open("TF16_1.txt", "r")
        text = f.read()
        words = text.split()
        f_2 = open("TF16_2.txt", "w")
        vowels = [ "e", "y", "u", "i", "o", "a", "E", "Y", "U", "I", "O", "A"]
        for i in words:
            if i[0] in vowels:
                f_2.write(f"{i}\n")
        f_2.close()

    def print_text_from_file2():
        f_2 = open("TF16_2.txt", "r")
        text = f_2.read()
        print(text)
        f_2.close()
fileLesson = FileLesson
try:
    fileLesson.creating_file_with_text()
    fileLesson.creating_file_with_words_from_text_file()
    fileLesson.print_text_from_file2()
except:
    print("something with files went wrong")