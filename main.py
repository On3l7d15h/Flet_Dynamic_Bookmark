from flet import *;

# Importing the components and settings for our app
from classes.layout.page_settings import Settings;

def main(page: Page):

    # Settings of the page (Window)
    Settings(page);


if __name__ == "__main__":
    app(target=main);