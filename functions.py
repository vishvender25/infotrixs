import datetime
import csv


class Functions:
    contact_parameters = ['name', 'phone']
    contact_directory = 'contacts.csv'
    contact_data = []
    contact_match = 'false'

    def create(self):
        print()
        print('create contact : '.center(150))
        print()
        for para in self.contact_parameters:
            contact_detail = input(('Enter ' + para+':'))
            self.contact_data.append(contact_detail)

        date = datetime.datetime.today()
        d = date.strftime('%B %d %Y')

        self.contact_data.append(d)

        with open(self.contact_directory, 'a') as file:
            write = csv.writer(file)
            write.writerows([self.contact_data])

        self.contact_data = []

        print('contact created successfully')

    def view(self):
        print()
        print('Contacts'.center(150))
        print()
        count = 0
        with open(self.contact_directory) as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    count += 1
        print('Total contacts in the directory are ', count)

        if count == 0:
            print('The directory is empty!!')
            return

        with open(self.contact_directory) as file:
            read = csv.reader(file)

            for para in self.contact_parameters:
                print('{0:<10}'.format(para).center(10), end='\t\t')
            print('{0:<10}'.format('Date'))

            for data in read:
                if len(data) > 0:
                    for item in data:
                        print('{0:<10}'.format(item).center(10), end = '\t\t')
                    print()

    def search(self):
        print()
        print('Search Contacts'.center(150))
        print()
        self.contact_match = 'false'
        search_val = input('Enter contact you want to search : ')

        for para in self.contact_parameters:
            print('{0:<10}'.format(para).center(10), end = '\t\t')
        print('{0:<10}.'.format('Date'))

        with open(self.contact_directory, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if search_val == data[0]:
                        self.contact_match = 'true'
                        print('{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0], data[1], data[2]).center(10))

            if self.contact_match == 'false':
                print('No contact found')

    def delete(self):
        print()
        print('Delete Contacts'.center(150))
        print()

        self.contact_match = 'false'

        delete_val = input('Enter contact to delete : ')
        update_list = []

        with open(self.contact_directory, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if delete_val != data[0]:
                        update_list.append(data)
                    else:
                        self.contact_match = 'true'

        if self.contact_match == 'true':
            with open(self.contact_directory, 'w') as file:
                write = csv.writer(file)
                write.writerows(update_list)
            print('Contact is deleted successfully')

        if self.contact_match == 'false':
            print('Given user does not exist in the directory')







