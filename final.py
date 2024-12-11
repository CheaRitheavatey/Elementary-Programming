# file handling practice
# task 1: create a python script that writes a list of your favorite movies to a text file, one movie per line.
import os
def task1(filepath):
    movies = ["movie1", "movie2", "movie3"]
    myfile = open(filepath, "w")

    # write file
    for i in movies:
        myfile.write(i+'\n')
    
    myfile.close()

    # read file
    myfile = open(filepath, "r")
    print(myfile.read())
    myfile.close()

    # append file
    myfile = open(filepath, 'a')
    myfile.write("movie4"+'\n')
    myfile.close()

    # count line
    myfile = open(filepath, 'r')
    print(len(myfile.readlines()))
    myfile.close()

    # copy a file
    myfile = open(filepath, 'r')
    newfile = open('newfile.txt', 'w')

    for i in myfile.readlines():
        newfile.write(i)
    newfile.close()
    myfile.close()

    # check if file exist
    print(os.path.exists(filepath))

    # exception handling
    try:
        file = open(filepath)
        print(file.read())
    except FileNotFoundError:
        print("File not found")
    finally:
        file.close()

    # file statistic
    file = open(filepath, 'r')
    count = 0
    longest_movie = ""

    for i in file:
        title = i.strip() # remove extra white space
        count += 1
        if len(title) > len(longest_movie):
            longest_movie = title
    
    print(f"Number of movies: {count}")
    print(f"Longest movie: {longest_movie}")

    file.close()



        


task1('name.txt')