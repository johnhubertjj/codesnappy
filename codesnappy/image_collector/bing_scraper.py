from bing_image_downloader import downloader
downloader.download(query_string, limit=100,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, print_out=True)

class PycharmScraper:
    def __init__(self, input_search):
        self.input_search = input_search
        self.output = self.scrape_bing

    def scrape_bing(self):
        downloader.download(self.input_search, limit=100000,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, print_out=True))
