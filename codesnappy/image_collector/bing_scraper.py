from bing_image_downloader import downloader


class BingScraper:
    def __init__(self, input_search, limit, output_dir):
        self.input_search = input_search
        self.output = self.scrape_bing()

    def scrape_bing(self):
        download_things = downloader.download(self.input_search, limit=100,  output_dir='dataset',
                                              adult_filter_off=True,
                                              force_replace=False, timeout=60)
        return download_things

