import utils

while True:
    choice = input("Enter your number: ")
    if choice == 'q':
        break
    else:
        print(utils.process_item(int(choice)))
    