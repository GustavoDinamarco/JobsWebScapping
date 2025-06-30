from bs4 import BeautifulSoup

class Transform:
    def __init__(self):
        pass

    def soupHtml(self,html_text):
        soup = BeautifulSoup(html_text, "html.parser")
        return soup
    
    def getJobs(self, site_source, soup):
        match site_source:
            case "remotar":
                return print("remotar")
            case _:
                return "not found"