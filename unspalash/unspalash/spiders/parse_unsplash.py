import scrapy
from urllib.parse import urljoin

class ParseUnsplashSpider(scrapy.Spider):
    name = "parse_unsplash"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com"]

    def parse(self, response):
         for image in response.xpath("//div/div/div/div[1]/figure/div[2]/a"):
            img_url = image.xpath(".//@href").get()
            # img_url = image.xpath('@alt').extract_first()
            # base = "photos/" + img_url
            # xpath(".//@href").get()
            # asd = urljoin(base, img_url)
            # print(response.urljoin(img_url))
            yield scrapy.Request(response.urljoin(img_url), self.parse_image_page)
            # print(image)

    def parse_image_page(self, response):
        # for image in response.xpath("//*[@id='modal-portal']//*[contains(@class, 'WxXog')]/img"):
            # print(response)
            img_url1 = response.xpath("//*[@id='app']//*[contains(@class, 'WxXog')]/img/@srcset").extract_first().split(',')[0]
            print(img_url1)
            yield scrapy.Request(response.urljoin(img_url1), self.save_img)

    def save_img(self, response):
        # filename = 'Test'
        filename = response.url.split('/')[-1][0:25] + '.jpg'
        with open(f"images/{filename}", 'wb') as f:
            f.write(response.body)




