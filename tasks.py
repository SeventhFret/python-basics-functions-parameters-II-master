from os import system


settings = {'title': 'Cool title', 'pages':[]}

default_settings = {'title': 'Super cool title', 'pages':[]}

def change_site_title_wo_global(new_title: str, global_settings=settings) -> dict:
    '''This function takes dict with 
    settings as an argument with default value and
    returns settings dict with updated values'''
    global_settings['title'] = new_title
    return global_settings

def change_site_title(new_title: str):
    '''This function make variabe global
    and change this variable with an updated title'''
    global settings
    settings['title'] = new_title

def get_title(settings_dict=default_settings):
    '''Getter function, which returns title of site
    from inserted dict argument. Default value is defaul_settings'''
    return settings_dict['title']

def get_pages(settings=default_settings):
    '''Getter function, which returns the list of 
    pages, available in "pages" key of given dictionary.
    Default value is default_settings dictionary.'''
    return settings['pages']

def add_page(page: dict, settings: dict = default_settings) -> dict:
    '''Setter function which accepts page dict and dict with settings.
    This function appends list in pages key of given dictionary.'''
    settings['pages'].append(page)
    return settings

def print_user_profile(gender: str = 'female', first: str = 'Jane', last: str = 'Doe', pictures: list = []):
    '''This function accepts 4 arguments - gender(str), first name(str),
    last name(str) and list of pictures. It changes the name according to
    gender and according to first name argument - if it is default or not.
    Then it prints phrase with first and last name of user and common header for every user.
    After that it iterates through list of pictures and prints them line by line.'''
    
    if gender == 'male' and first == 'Jane':
        first = 'John'
    elif gender == 'female' and first == 'Jane':
        first = 'Jane'

    print(f'The user {first} {last} has the following pictures: ')
    print('common_header.png')
    
    for pic in pictures:
        print(pic)

while True:
    system('clear')
    print('''What you want to do?
[1] - Task 1
[2] - Task 2
[3] - Task 3
[4] - Task 4
[x] - Exit
''')
    choice = input()
    print()
    if choice == '1':
        # I prefer to avoid using global keyword to don't mess my code
        # But I'll do that both ways, because as I understood I suggested to use global
        
        # 1 WAY
        print(settings)
        settings = change_site_title_wo_global('New cool title')
        print(settings)

        # RESETING SETTINGS VARIABLE
        settings = {'title': 'Cool title'}
        print()

        # 2 WAY
        print(settings)
        change_site_title("A new fancy title")
        print(settings)
    elif choice == '2':
        print(get_title(settings))
        print(get_title())
        change_site_title("A new fancy title")
        print(get_title(settings))
        print(get_title())
    elif choice == '3':
        home = {"title": "Home", "path": "/"}
        about = {"title": "About", "path": "/about/"}
        contacts = {"title": 'Contacts', "path": "/contacts/"}
        default_settings = add_page(home)
        print(get_pages())
        print(get_pages(settings))
        settings = add_page(about, settings=settings)
        print(get_pages())
        print(get_pages(settings))
        default_settings = add_page(contacts)
        print(get_pages())
        print(get_pages(settings))
    elif choice == '4':
        test_data1 = {
            "gender": "male",
            "last": "Brown",
            "pictures": ["holidays1.png", "easter_grandma.png"]
        }
        test_data2 = {
            "first": "Alicia",
            "last": "Schmidt"
        }
        test_data3 = {
            "last": "Korkov",
            "pictures": ["sunset.png"]
        }
        print_user_profile(**test_data1)
        print_user_profile(**test_data2)
        print_user_profile(**test_data3)
        print_user_profile(**test_data2)
    if choice != 'x':
        print()
        input('Press Enter to continue...')
        continue
    else:
        print("Alright, see you!")
        break