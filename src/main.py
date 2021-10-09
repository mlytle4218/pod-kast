# python imports
import os, subprocess

# local imports
import utils
from data_accessor import DataAccessor
from menu import Menu 
from sqlite_database_creation import Category, Podcast
from sql_category import CategoryControls
from sql_podcast import PodcastControls
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
        self.podcast_controls = PodcastControls()
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
            self.category_controls.add_new_category(self.session, category)
            self.result_print(category, 'added')

        
    def edit_category(self):
        os.system('clear')
        categories = self.category_controls.get_all_categories(self.session)
        category = self.menu.print_out_menu_options_categories(objects=categories)
        if category:
            category.title = utils.rlinput('category name: ', category.title).strip()
            result  = self.category_controls.update_category(self.session, category)
            self.result_print(category, 'updated')


    def delete_category(self):
        os.system('clear')
        categories = self.category_controls.get_all_categories(self.session)
        category = self.menu.print_out_menu_options_categories(objects=categories)
        if category:
            self.category_controls.remove_category(self.session, category)
            self.result_print(category, 'deleted')



    def add_new_podcast(self):
        os.system('clear')
        podcast = Podcast()
        podcast.title = self.menu.get_input('Enter name: ')
        podcast.url = self.menu.get_input('Enter url name: ')
        podcast.audio  = self.menu.get_input('Enter audio directory: ')
        podcast.video  = self.menu.get_input('Enter video directory: ')
        categories = self.category_controls.get_all_categories(self.session)
        category = self.menu.print_out_menu_options_categories(objects=categories)
        podcast.category = category.category_id
        result = self.podcast_controls.add_new_podcast(self.session,podcast)
        if result:
            self.result_print(podcast, 'added')
        # TODO: add episode creation



        # self.title = title
        # self.url = url
        # self.audio = audio
        # self.video = video
        # self.catgory = category
        # podcast = enter_podcast_info(podcast)
        # if podcast != None:
        #     episodes = backend.get_episodes_from_feed(podcast.url)
        #     sql.insert_podcast(podcast, episodes)
        #     pass

    def edit_existing_podcast(self):
        os.system('clear')
        podcasts = self.podcast_controls.get_all_podcasts(self.session)
        podcast = self.menu.display_items_podcasts(objects=podcasts)
        # if podcast:
        #     podcast.title = utils.rlinput('podcast name: ', podcast.title).strip()
        #     result  = self.podcast_controls.update_podcast(self.session, podcast)
        #     self.result_print(podcast, 'updated')

        pass
    def delete_existing_podcast(self):
        os.system('clear')
        podcasts = self.podcast_controls.get_all_podcasts(self.session)
        podcast = self.menu.display_items_podcasts(objects=podcasts)
        if podcast:
            self.podcast_controls.delete_podcast_id(self.session, podcast.podcast_id)
            self.result_print(podcast, 'deleted')
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


    def result_print(self, result, message_text):
        if result:
            print('{} was {}'.format(result, message_text))
            input('press enter to acknowledge')
        else:
            print('{} was not {}'.format(result, message_text))
            input('press enter to acknowledge')

if __name__ == "__main__":
    Main()
