from pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        self.open_url('https://www.amazon.com/')

    def best_seller(self):
        self.open_url('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
