import os, sys

from enum import Enum

from sqlalchemy import sql
from sqlite_database_creation import Podcast, Episode, Category


from log import logging as log
import utils
from sql_category import CategoryControls as sql_category

class Menu:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def main_menu(self):
        try:
            while True:
                os.system('clear')
                print('number 1 add category')
                print('number 2 edit category')
                print('number 3 add new podcast')
                print('number 4 edit existing podcast')
                print('number 5 delete existing podcast')
                print('number 6 choose episodes to download')
                print('number 7 start downloads')
                print('number 8 search for podcasts')
                print('number 9 delete from download queue')
                print('number 10 update all podcasts')
                print('number 11 archive')
                response = self.get_input('choice ')
                if (response and not utils.special_characters_check(response)):
                    return response
        except KeyboardInterrupt:
            pass

    def get_input(self, request):
        try:
            while True:
                response = input(request)
                if len(response) == 0:
                    return None
                if ( not utils.special_characters_check(response)):
                    return response
                return None
        except KeyboardInterrupt:
            return None

    def print_out_menu_options(self, objects, attribute=None, three=None, four=None, five=None):
        result = self.display_items(objects)
        if result:
            return result
        else:
            return None

    def display_items(self, objects):
        object_dict = {}
        object_enum = enumerate(objects, 1)
        for i,obj in object_enum: 
            object_dict[i] = obj
            print('{}. {}'.format(i,str(obj)))
        while True:
            try:
                result = input('choice ') 
                if result == 'n':
                    # next page
                    pass
                elif result == 'p':
                    # previous page
                    pass
                elif result == 'q':
                    return None
                else:
                    back = object_dict[int(result)]
                    return back
            except ValueError as e:
                log.error(e)
    
    
    

def main_menu_old():
    print(os.chdir(os.path.dirname(os.path.abspath(__file__))))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try:
        if len(sys.argv) >1 and sys.argv[1] == '-u':
            try:
                update_all_episodes()
            except  Exception as e:
                log.error('tried tp update')
                log.error(e)

        else:
            while True:
                os.system('clear')
                print('number 1 add category')
                print('number 2 edit category')
                print('number 3 add new podcast')
                print('number 4 edit existing podcast')
                print('number 5 delete existing podcast')
                print('number 6 choose episodes to download')
                print('number 7 start downloads')
                print('number 8 search for podcasts')
                print('number 9 delete from download queue')
                print('number 10 update all podcasts')
                print('number 11 archive')
                result = input('choice ')
                try:
                    result = int(result)
                    if result == 1:
                        add_category()
                    elif result == 2:
                        edit_category()
                    elif result == 3:
                        # add_new_podcast(Podcast())
                        add_new_podcast()
                    elif result == 4:
                        edit_existing_podcast()
                    elif result == 5:
                        delete_existing_podcast()
                    elif result == 6:
                        choose_episodes_to_download()
                    elif result == 7:
                        start_downloads()
                    elif result == 8:
                        search()
                    elif result == 9:
                        delete_from_download_queue()
                    elif result == 10:
                        update_all_episodes()
                    elif result == 11:
                        list_archived_episodes()

                    # # hidden
                    # elif result == 20:
                    #     for each in download_queue:
                    #         log.info(vars(each))
                    # elif result == 21:
                    #     update_episodes_fix()

                except ValueError:
                    if result == 'q':
                        break
    except KeyboardInterrupt:
        pass

def add_category():
    os.system('clear')
    category_name = get_inputs()
    sql_category.add_new_category(session, category_name)

def edit_category():
    pass
# def add_new_podcast(Podcast()):
def add_new_podcast():
    pass
def edit_existing_podcast():
    pass
def delete_existing_podcast():
    pass
def choose_episodes_to_download():
    pass
def start_downloads():
    pass
def search():
    pass
def delete_from_download_queue():
    pass
def update_all_episodes():
    pass
def list_archived_episodes():
    pass

def get_inputs(request):
    try:
        while True:
            response = input(request)
            if len(response) == 0:
                return None
            if ( not utils.special_characters_check(response)):
                return response
            return None
    except KeyboardInterrupt:
        pass


