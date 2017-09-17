class Page_Obj:
    def __init__(self, page_id=None, page_title=None, page_namespace=None):
        self.page_id = page_id
        self.page_title = page_title
        self.page_namespace = page_namespace

    def get_id(self):
        return self.page_id

    def get_title(self):
        return self.page_title

    def get_namespace(self):
        return self.page_namespace
