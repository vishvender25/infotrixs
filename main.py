from functions import Functions


def title():
    title_top = '###########################################################'
    title_text = '               CONTACT MANAGEMENT SYSTEM                 '
    title_bottom = '###########################################################'
    print(title_top.center(130))
    print(title_text.center(130))
    print(title_bottom.center(130))


def functionalities():
    print("Enter 1 to view contacts  ".center(150))
    print("Enter 2 to create contacts".center(150))
    print("Enter 3 to search contacts".center(150))
    print("Enter 4 to delete contacts".center(150))
    print("Enter 5 to exit the system".center(150))


title()
functionalities()

using_the_system = True

system_functions = Functions()
while using_the_system:

    user_choice = int(input("Enter functionality to perform ".center(150)))

    if user_choice == 1:
        system_functions.view()

    if user_choice == 2:
        system_functions.create()

        create_more_contacts = 'y'
        while create_more_contacts.lower() == 'y':
            create_more_contacts = input('Do you want to create more contacts[Y/N]')
            if create_more_contacts == 'y':
                system_functions.create()
            else:
                break

    if user_choice == 3:
        system_functions.search()

        search_more_contacts = 'y'
        while search_more_contacts.lower() == 'y':
            search_more_contacts = input('Do you want to search more contacts[Y/N]')
            if search_more_contacts == 'y':
                system_functions.search()
            else:
                break

    if user_choice == 4:
        system_functions.delete()

        delete_more_contacts = 'y'
        while delete_more_contacts.lower() == 'y':
            delete_more_contacts = input('Do you want to delete more contacts[Y/N]')
            if delete_more_contacts == 'y':
                system_functions.delete()
            else:
                break

    if user_choice == 5:
        print('Thanks for using our contact management system!!!')
        using_the_system = False

