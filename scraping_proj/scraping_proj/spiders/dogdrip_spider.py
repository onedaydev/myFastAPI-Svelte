from pathlib import Path

import scrapy


class DogdripSpider(scrapy.Spider):
    name = "dogdrip"

    def start_requests(self):
        urls = [
            "https://www.dogdrip.net/dogdrip?page=",
        ]
        for url in urls:
            for i in range(2,3):
                yield scrapy.Request(url=url+str(i), callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("?")[-1][-1]
        filename = f"dogdrip-{page}.html"
        Path(filename).write_bytes(response.body)        
        self.log(f"Saved file {filename}")
