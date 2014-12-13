# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from data_science.items import DataScienceItem

class JobSpider(scrapy.Spider):
    """
    job spider for each job the site analytictalent.com
    """
    name = "jobspider"
    allowed_domains = ["analytictalent.com"]
    #urlFile = "C:\\Users\\a\\Google Drive\\workspace\\DataScience\\data_science\\listURL.txt"
    #urlread = open(urlFile,'rb')
    #urlFile.close() not necessary
    #filedict = urlread.read()
    count = 0
    start_urls = (
         u'http://careers.analytictalent.com/jobs/advanced-technologist-level-3-4-huntsville-alabama-72055208-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/aerospace-systems-modeling-and-simulation-engineer-level-2-3-huntsville-alabama-72055209-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/parallel-database-systems-engineer-level-2-3-huntsville-alabama-72060146-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/director-strategy-consumer-insights-new-york-new-york-10001-71942287-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-scientist-redwood-city-california-94063-71786227-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/assistant-professor-data-analytics-and-audience-engagement-phoenix-arizona-85004-71628051-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-science-lead-new-york-new-york-10014-71627986-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/applied-scientist-microsoft-bellevue-washington-71585468-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/maps-data-sciences-engineer-apple-santa-clara-valley-california-71585475-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/software-engineer-phd-university-graduate-youtube-san-bruno-california-71585608-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-scientist-instagram-analytics-facebook-menlo-park-california-71585331-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/lead-software-engineer-oracle-identity-manager-oim-platform-visa-foster-city-california-71585332-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/hadoop-software-dev-eng-principal-yahoo-champaign-illinois-71585333-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/principal-data-scientist-ads-microsoft-cambridge-massachusetts-71585343-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/senior-data-scientist-bosch-north-america-palo-alto-california-71585350-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/sr-data-analyst-new-york-new-york-10001-71159121-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/senior-software-architect-machine-learning-apple-santa-clara-valley-california-70981487-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/rnd-phd-internship-global-statistics-data-management-procter-gamble-cincinnati-ohio-70981489-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/director-of-algorithms-engineering-santa-clara-california-95054-70981227-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/intern-scientist-yahoo-labs-sunnyvale-california-70981339-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/senior-relevance-machine-learning-software-engineer-twitter-san-francisco-bay-area-70981364-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/researcher-software-engineer-robotics-special-projects-google-mountain-view-california-70981362-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-scientist-machine-learning-zillow-seattle-washington-70981355-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/machine-learning-software-engineer-data-scientist-tripadvisor-newton-massachusetts-70981372-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/mckinsey-solutions-ingenuity-data-scientist-new-york-70981276-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/digital-social-media-communications-senior-manager-el-segundo-california-90245-70386961-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-scientist-skype-redmond-washington-70384158-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/senior-machine-learning-scientist-microsoft-sunnyvale-california-70384066-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-scientist-consumer-hallmark-cards-kansas-city-missouri-70384153-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/chief-product-owner-data-replication-paypal-san-jose-california-70384142-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/chief-architect-of-big-data-and-analytics-huawei-technologies-santa-clara-california-70384155-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-scientist-hp-plano-texas-70383308-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/machine-learning-engineer-adroll-san-francisco-california-70383304-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/machine-learning-scientist-amazon-seattle-washington-70383326-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-scientist-applied-machine-learning-apple-santa-clara-valley-california-70383331-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/machine-learning-researcher-ge-software-san-ramon-california-70383328-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-mining-engineer-association-rule-mining-bosch-palo-alto-california-69858832-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-mining-scientist-apple-austin-texas-69858833-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/senior-software-engineer-machine-learning-bose-corporation-framingham-massachusetts-69858825-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/predictive-modeler-ebay-san-jose-california-69858842-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/lead-data-scientist-paypal-omaha-nebraska-69858789-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/technical-lead-for-android-development-hewlett-packard-palo-alto-california-69709870-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/big-data-senior-principal-engineer-intel-santa-clara-california-69709732-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-scientist-l-3-communications-washington-district-of-columbia-69709691-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/principal-data-scientist-predictive-analytics-walmart-ecommerce-sunnyvale-california-69709716-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/data-scientist-senior-associate-ey-69709719-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/staff-data-scientist-chegg-santa-clara-california-69709671-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/lead-data-scientist-ge-software-san-ramon-california-69709664-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/senior-manager-data-scientist-vmware-austin-texas-69709703-d?contextType=rss',
         u'http://careers.analytictalent.com/jobs/principal-big-data-software-engineer-at-t-palo-alto-california-69709669-d?contextType=rss',
    )

    def parse(self, response):

        ###urlFile has to change per the local path

        items = []
        item = DataScienceItem()
        item['text_a'] =  response.xpath('//a/@href').extract() #bullet points in the texts
        item['text_all'] =  response.xpath('//*/text()').extract() #span class, usually all the texts
        item['title'] =  response.xpath('//title/text()').extract() #title of the page]
        item['text_p'] =  response.xpath('//p/text()').extract() #span class, usually all the texts

        items.append(item)

        s =item['title'][0]
        new_s =""
        for i in s :
         if (i >= "0" and i <="9") or (i>="a" and i <= "z") or ( i>="A" and i<="Z"):
             new_s += i
        filename = new_s
        with open(filename+".txt", 'wb') as f:
            f.write(str(items))
