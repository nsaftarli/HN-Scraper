import scrapy
import time


date = time.strftime("%d.%m.%y")
filename = date + ".json"
class QuotesSpiders(scrapy.Spider):
	name = "hnspider"
	start_urls = [
	'http://news.ycombinator.com/',
	]


	def parse(self,response):
		for title in response.css('tr.athing'):
			yield {
				'title' : title.css('a.storylink::text').extract(),
				'link' : title.css('a.storylink::attr(href)').extract_first(),
			}

		#next_page = response.css('li.next a::attr(href)').extract_first()
		next_page = response.css('a.morelink::attr(href)').extract_first()

		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page,callback=self.parse)

'''with open(filename,"wb") as f:
	f.close()'''






#use 'scrapy crawl quotes -o quotes.json' to store scraped info in JSON file
#'scrapy crawl quotes -o quotes.jl' to store in JSON Lines, which is appendable
