
from data_accessor import DataAccessor as da
from main import Menu 


if __name__ == "__main__":
    session = da.connect_to_database()
    menu = Menu()
