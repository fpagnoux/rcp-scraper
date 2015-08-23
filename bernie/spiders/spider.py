import scrapy
from bernie.items import TableItem

class spider(scrapy.Spider):
    name = "bernieSpider"
    start_urls = ["file:///home/fpagnoux/erika/national.html"]

    def parse(self, response):
        table = response.css('.data').pop()
        legend = table.css('tr')[0]
        fieldNames = legend.css('th::text').extract()
        nb_fields = len(fieldNames)
        items = []

        contentLines = table.css('tr')[1::]

        for line in contentLines:
            item = TableItem()
            values = line.css('td::text, td span::text, td a::text').extract()
            for i in range(nb_fields):
                item[fieldNames[i]] = values[i]

            items.append(item)

        return items
