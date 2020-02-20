libraries = []
books = []
scanned_books = []
total_score = 0
current_day = 0
signing = False
libraries_signed = []


def solve(books, libraries, days):
    global current_day

    while current_day < days:
        print("current day", current_day)
        for library in libraries:
            if library.signed == False:
                library.signup()
            else:
                library.scan_books()
        current_day += 1


    return scanned_books


class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
        self.scanned = False

    def scan(self):
        self.scanned = True

    def __str__(self):
        return f'{self.id} {self.score}'


class Library:
    def __init__(self, id, books, signup_days, books_per_day):
        self.id = id
        self.books = books
        self.signup_days = signup_days
        self.books_per_day = books_per_day
        self.signed = False
        self.books_scanned = []

    def signup(self):
        global current_day, libraries_signed, signing

        print(signing)
        while(signing == True):
            print("trying sign up")
            time.sleep(1)

        signing = True
        print("library {} signed".format(self.id))
        current_day += (self.signup_days - 1)
        self.signed = True
        libraries_signed.append(self)
        signing = False
        # print("Library {} signed on day {}".format(self.id, current_day))
    
    def scan_books(self):
        global total_score, current_day
        for i in range(self.books_per_day):
            tempBook = self.books.pop(0)
            if(tempBook.scanned == False):
                tempBook.scan()
                scanned_books.append(tempBook.id)
                total_score += tempBook.score
                self.books_scanned.append(tempBook)

        current_day += 1

    def __str__(self):
        return f'{self.signup_days} {self.books_per_day} {self.books[0]}'


def process(fileName):

    inputFile = open("inputs/" + fileName + ".txt", "rt")

    firstLine = inputFile.readline()
    secondLine = inputFile.readline()

    num_books, num_libraries, num_days = list(map(int, firstLine.split()))

    scores_books = list(map(int, secondLine.split()))

    for i in range(num_books):
        books.append(Book(i, scores_books[i]))

    for i in range(num_libraries):
        library_line1 = inputFile.readline()
        library_line2 = inputFile.readline()

        num_library_books, signup_days, books_per_day = list(
            map(int, library_line1.split()))

        temp_books = list(map(int, library_line2.split()))
        library_books = []
        for index in temp_books:
            for book in books:
                if book.id == index:
                    library_books.append(book)
                    break

        libraries.append(Library(i, library_books, signup_days, books_per_day))

    inputFile.close()

    result = solve(books, libraries, num_days)

    outputFile = open("outputs/" + fileName + ".txt", "w")
    outputFile.write(str(len(libraries_signed)) + "\n")
    # print(len(libraries_signed))
    for library in libraries_signed:
        # print("{} {}".format(library.id, len(library.books_scanned)))
        outputFile.write(str(library.id) + " " + str(len(library.books_scanned)) + "\n")
        parsedOutputString = ""
        for book in library.books_scanned:
            parsedOutputString = parsedOutputString + str(book.id) + " "    
        outputFile.write(parsedOutputString + "\n")
    outputFile.close()



# files = ["a_example", "b_read_on", "c_incunabula",
#          "d_tough_choices", "e_so_many_books", "f_libraries_of_the_world"]

files = ["a_example", "b_read_on"]
for file in files:
    process(file)
