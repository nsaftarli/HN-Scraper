#!/bin/bash

today=`date +%Y-%m-%d`
form='.json'


scrapy crawl hnspider -o "$today.json"

cp "$today.json" ./hnscraper/

rm "$today.json"
