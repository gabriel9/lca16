import sys
import json
import urllib.request
import xml.etree.ElementTree as ET

sys.path.append('../../')
import real_twitter_credentials as tc

def fetch_test_url(searchterms):
    '''
    Fetch a test URL to a valid flickr image
    '''

    return 'https://farm2.staticflickr.com/1503/24377660909_1aeec67c5a.jpg'

def fetch_url(searchterms):
    '''
    Return the image URL for the first matching image given the search terms
    '''

    html = search_for(searchterms)
    url = get_first_image_url(html)

    return url

def search_for(searchterms):
    # TODO: secure pack the search term


    resturl = ''
    resturl += "https://api.flickr.com/services/rest/?method=flickr.photos.search"
    resturl += "&api_key=%s" % tc.api_key
    resturl += '&text=%s' % searchterms
    resturl += "&safe_search=1&per_page=20"

    with urllib.request.urlopen(resturl) as response:
        html = response.read()

    return html

def get_first_image_url(html):

    tree = ET.fromstring(html)
    photos_list = tree.getchildren()[0]
    first_photo = photos_list.getchildren()[0]
    first_photo.attrib

    image_url_pattern = 'https://farm{farm}.staticflickr.com/{server}/{id}_{secret}.jpg'
    actual_image_url = image_url_pattern.format(**first_photo.attrib)

    return actual_image_url
