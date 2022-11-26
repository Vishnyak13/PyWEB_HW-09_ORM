from sqlalchemy.exc import SQLAlchemyError

from database.seed import create_fake_contacts, add_contact, get_contact_by_id, get_all_contacts, update_contact, \
    delete_contact, add_phone, add_email, add_address


def match_case(choice):
    try:
        match choice:
            case 1:
                print(get_all_contacts())
            case 2:
                print(get_contact_by_id(int(input('Enter id: '))))
            case 3:
                add_contact(input('Enter first name: '), input('Enter last name: '), input('Enter address: '))
            case 4:
                update_contact(int(input('Enter id: ')), input('Enter first name: '), input('Enter last name: '),
                               input('Enter address: '))
            case 5:
                delete_contact(int(input('Enter id: ')))
            case 6:
                add_phone(int(input('Enter id: ')), input('Enter phone number: '))
            case 7:
                add_email(int(input('Enter id: ')), input('Enter email address: '))
            case 8:
                add_address(int(input('Enter id: ')), input('Enter address: '))
    except SQLAlchemyError as e:
        print(e)


def run():
    try:
        while True:
            print('What do you want to do?')
            print('1. Get all contacts')
            print('2. Get contact by id')
            print('3. Add contact')
            print('4. Update contact')
            print('5. Delete contact')
            print('6. Add phone number to contact')
            print('7. Add email address to contact')
            print('8. Add address to contact')
            print('9. Exit')
            choice = int(input('Enter choice: '))
            if choice == 9:
                print('Goodbye')
                break
            match_case(choice)
    except ValueError:
        print('Please enter a number')
        run()


def main():
    print('Welcome to Address Book')
    print('Do you want to create fake contacts? (y/n)')
    if input() == 'y':
        try:
            print('How many contacts do you want to create?')
            create_fake_contacts(int(input('Enter count: ')))
            run()
        except SQLAlchemyError as e:
            print(e)
    else:
        print('Ok, no fake contacts')
        run()


if __name__ == '__main__':
    main()
