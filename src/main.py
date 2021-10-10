# python imports
import os, subprocess

# local imports
import utils
from data_accessor import DataAccessor
from menu import Menu 
from sqlite_database_creation import Category
from sql_category import CategoryControls
import config


from log import logging as log

class Main:
    def __init__(self):
        dataAccessor = DataAccessor()
        self.session = dataAccessor.get_session()
        width = config.width
        height = config.height
        try:
            width = int(subprocess.check_output(['tput', 'cols']))
            height = int(subprocess.check_output(['tput', 'lines'])) - 1
        except Exception as e:
            log.error(e)
            
        self.menu = Menu(width, height)
        self.category_controls = CategoryControls()
        self.start()
    
    def start(self):
        try:
            while True:
                try:
                    result = self.menu.main_menu()
                    result = int(result)
                    if result == 1:
                        self.add_category()
                    elif result == 2:
                        self.edit_category()
                    elif result == 3:
                        self.delete_category()
                    elif result == 4:
                        self.add_new_podcast()
                    elif result == 5:
                        self.edit_existing_podcast()
                    elif result == 6:
                        self.delete_existing_podcast()
                    elif result == 7:
                        self.choose_episodes_to_download()
                    elif result == 8:
                        self.start_downloads()
                    elif result == 9:
                        self.search()
                    elif result == 10:
                        self.delete_from_download_queue()
                    elif result == 11:
                        self.update_all_episodes()
                    elif result == 12:
                        self.list_archived_episodes()
                except ValueError as e: 
                    if result == 'q':
                        break
        except KeyboardInterrupt as e:
            log.error(e)
            pass

    def add_category(self):
        os.system('clear')
        category_name = self.menu.get_input('Enter category name: ')
        if category_name:
            category = Category(category_name)
            result = self.category_controls.add_new_category(self.session, category)
            if not result:
                print('{} could not be added as a category'.format(category_name))
                input('press enter to acknowledge')
            else:
                print('{} was added as a category'.format(category_name))
                input('press enter to acknowledge')

        
    def edit_category(self):
        os.system('clear')
        categories = self.category_controls.get_all_categories(self.session)
        category = self.menu.print_out_menu_options(
            objects=categories, attribute='category')
        if category:
            category.title = utils.rlinput('category name: ', category.title).strip()
            result  = self.category_controls.update_category(self.session, category)
            if result:
                print('{} was updated'.format(category.title))
                input('press enter to acknowledge')
                return
            else:
                print('{} was not updated'.format(category.title))
                input('press enter to acknowledge')


    def delete_category(self):
        pass
    def add_new_podcast(self):
        pass
    def edit_existing_podcast(self):
        pass
    def delete_existing_podcast(self):
        pass
    def choose_episodes_to_download(self):
        pass
    def start_downloads(self):
        pass
    def search(self):
        pass
    def delete_from_download_queue(self):
        pass
    def update_all_episodes(self):
        pass
    def list_archived_episodes(self):
        pass

if __name__ == "__main__":
    Main()
