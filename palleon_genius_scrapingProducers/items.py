# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PalleonGeniusScrapingproducersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id_producers = scrapy.Field()
    _type = scrapy.Field()
    annotation_count = scrapy.Field()
    api_path = scrapy.Field()
    full_title = scrapy.Field()
    header_image_thumbnail_url = scrapy.Field()
    header_image_url = scrapy.Field()
    id = scrapy.Field()
    instrumental = scrapy.Field()
    lyrics_owner_id = scrapy.Field()
    lyrics_state = scrapy.Field()
    lyrics_updated_at = scrapy.Field()
    path = scrapy.Field()
    pyongs_count = scrapy.Field()
    song_art_image_thumbnail_url = scrapy.Field()
    song_art_image_url = scrapy.Field()
    stats_unreviewed_annotations = scrapy.Field()
    stats_hot = scrapy.Field()
    stats_pageviews = scrapy.Field()
    title = scrapy.Field()
    title_with_featured = scrapy.Field()
    updated_by_human_at = scrapy.Field()
    url = scrapy.Field()
    primary_artist__type = scrapy.Field()
    primary_artist_api_path = scrapy.Field()
    primary_artist_header_image_url = scrapy.Field()
    primary_artist_id = scrapy.Field()
    primary_artist_image_url = scrapy.Field()
    primary_artist_index_character = scrapy.Field()
    primary_artist_is_meme_verified = scrapy.Field()
    primary_artist_is_verified = scrapy.Field()
    primary_artist_name = scrapy.Field()
    primary_artist_slug = scrapy.Field()
    primary_artist_url = scrapy.Field()
    primary_artist_iq = scrapy.Field()

    pass
