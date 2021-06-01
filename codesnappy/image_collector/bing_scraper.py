from bing_image_downloader import downloader


class BingScraper:
    def __init__(self, config):
        self.config = config
        self.output = self.scrape_bing()

    def scrape_bing(self):
        download_things = downloader.download(self.config.search, limit=self.config.limit,
                                              output_dir=self.config.output_dir,
                                              adult_filter_off=True,
                                              force_replace=False, timeout=60)
        return download_things

