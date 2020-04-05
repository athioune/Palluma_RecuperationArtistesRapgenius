# -*- coding: utf-8 -*-
import datetime
import json
import scrapy
from scrapy.exceptions import CloseSpider
from palleon_genius_scrapingProducers.items import PalleonGeniusScrapingproducersItem


class GeniusSpider(scrapy.Spider):
    name = 'geniusOLD'
    allowed_domains = ['www.genius.com']

    '''
    You don't have to override __init__ each time and can simply use self.parameter (See https://bit.ly/2Wxbkd9),
    but I find this way much more readable.
    '''
    def __init__(self, id, *args,**kwargs):
        super(GeniusSpider, self).__init__(*args, **kwargs)
        self.id = id

    def start_requests(self):
        url = ('https://genius.com/api/artists/{0}/songs?page={1}&sort=popularity')
        new_url = url.format(self.id, 1)

        for url in self.urlList:
            yield scrapy.Request(url=url, callback=self.parse_id, dont_filter=True)


    def parse_id(self, response):
        '''Parses all the URLs/ids/available fields from the initial json object and stores into dictionary

        Args:
            response: Json object from explore_tabs
        Returns:
        '''

        # Fetch and Write the response data
        data = json.loads(response.body)

        # Return a List of all songs
        songs = data.get('response').get('songs')

        try:
            if songs is None:
                print('Rien trouvé')
                raise CloseSpider("Pas de chansons ou de producteurs")
        except IndexError:
                print('Rien trouvé')
                raise CloseSpider("Pas de chansons ou de producteurs")


        listing = PalleonGeniusScrapingproducersItem()

        for song in songs:
            listing['_id_producers'] = self.id
            listing['_type'] = song.get('_type')
            listing['annotation_count'] = song.get('annotation_count')
            listing['api_path'] = song.get('api_path')
            listing['full_title'] = song.get('full_title')
            listing['header_image_thumbnail_url'] = song.get('header_image_thumbnail_url')
            listing['header_image_url'] = song.get('header_image_url')
            listing['id'] = song.get('id')
            listing['instrumental'] = song.get('instrumental')
            listing['lyrics_owner_id'] = song.get('lyrics_owner_id')
            listing['lyrics_state'] = song.get('lyrics_state')
            listing['lyrics_updated_at'] = song.get('lyrics_updated_at')
            listing['path'] = song.get('path')
            listing['pyongs_count'] = song.get('pyongs_count')
            listing['song_art_image_thumbnail_url'] = song.get('song_art_image_thumbnail_url')
            listing['song_art_image_url'] = song.get('song_art_image_url')
            listing['stats_unreviewed_annotations'] = song.get('stats').get('unreviewed_annotations')
            listing['stats_hot'] = song.get('stats').get('hot')
            listing['stats_pageviews'] = song.get('stats').get('pageviews')
            listing['title'] = song.get('title')
            listing['title_with_featured'] = song.get('title_with_featured')
            listing['updated_by_human_at'] = song.get('updated_by_human_at')
            listing['url'] = song.get('url')
            listing['primary_artist__type'] = song.get('primary_artist').get('_type')
            listing['primary_artist_api_path'] = song.get('primary_artist').get('api_path')
            listing['primary_artist_header_image_url'] = song.get('primary_artist').get('header_image_url')
            listing['primary_artist_id'] = song.get('primary_artist').get('id')
            listing['primary_artist_image_url'] = song.get('primary_artist').get('image_url')
            listing['primary_artist_index_character'] = song.get('primary_artist').get('index_character')
            listing['primary_artist_is_meme_verified'] = song.get('primary_artist').get('is_meme_verified')
            listing['primary_artist_is_verified'] = song.get('primary_artist').get('is_verified')
            listing['primary_artist_name'] = song.get('primary_artist').get('name')
            listing['primary_artist_slug'] = song.get('primary_artist').get('slug')
            listing['primary_artist_url'] = song.get('primary_artist').get('url')
            listing['primary_artist_iq'] = song.get('primary_artist').get('iq')

            # Finally return the object
            yield listing

        # After scraping entire listings page, check if more pages
        if data.get('response').get('next_page'):
            nextPage = data.get('response').get('next_page')
            #print('Page Suivante !!!')
            url = ('https://genius.com/api/artists/{0}/songs?page={1}&sort=popularity')
            new_url = url.format(self.id, nextPage)

            # If there is a next page, update url and scrape from next page
            yield scrapy.Request(url=new_url, callback=self.parse_id, dont_filter=True)
