import math
class Pagination:
    def __init__(self, items: [], page_size: 10):
        self.items = items
        self.visible_items = [ch for ch in items[0]]
        self.page_size = page_size
        self.starting_index = 0

    def  getVisibleItems(self):
        page = []
        for i in range(self.page_size):
            page.append(self.visible_items[self.starting_index + i])
        print(page)
    def nextPage(self):
        self.starting_index = self.starting_index + self.page_size
    def prevPage(self):
        self.starting_index = self.starting_index - self.page_size

    def firstPage(self):
        self.starting_index = 0
    def lastPage(self):
        times_spliting_list_by_page = len(self.visible_items)/self.page_size
        remainder = math.modf(times_spliting_list_by_page)
        self.starting_index = round(times_spliting_list_by_page)*self.page_size
        self.page_size = int(self.page_size * remainder[0])

    def goToPage(self, pageNum):
        times_spliting_list_by_page = len(self.visible_items) / self.page_size
        remainder = math.modf(times_spliting_list_by_page)
        if pageNum < times_spliting_list_by_page:
            self.starting_index = pageNum * self.page_size
        else:
            self.page_size = int(self.page_size * remainder[0])



alphabetList = "abcdefghijklmnopqrstuvwxyz".split(', ')
page = Pagination(alphabetList, 4)
page.getVisibleItems()
page.nextPage()
page.getVisibleItems()
page.nextPage()
page.getVisibleItems()
page.nextPage()
page.getVisibleItems()
page.prevPage()
page.getVisibleItems()
page.prevPage()
page.getVisibleItems()
print('go to')
page.goToPage(0)
page.getVisibleItems()
page.firstPage()
page.getVisibleItems()
page.lastPage()
page.getVisibleItems()


