from scrapy.spider import Spider
from scrapy.selector import Selector

from scrapyreddit.items import ScrapyredditItem

class RedditSpider(Spider):
    name = "scrapyreddit"
    allowed_domains = ["reddit.com"]
    start_urls = [
        "http://www.reddit.com"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*[@id="siteTable"]/div[contains(@class, "thing ")]')
        items = []
        for site in sites:
            item = ScrapyredditItem()
            item['title'] = site.xpath('div[2]/p[1]/a/text()').extract()
            item['subreddit'] = site.xpath('div[2]/p[2]/a[2]/text()').extract()
            item['submittedby'] = site.xpath('div[2]/p[2]/a[1]/text()').extract()
            item['upvotes'] = site.xpath('div[1]/div[3]/text()').extract()
            item['nocomments'] = site.xpath('div[2]/ul/li[1]/a/text()').extract()
            items.append(item)
        
	return items