import facebook
import requests

import settings

graph = facebook.GraphAPI(access_token="EAACEdEose0cBAJYzVLxpgKYaRgoPaN8M7d4KkIEoU1QTUEpNmNcHBR0mNZAKXCc56iaPHysjVCGVHB8WkNZCe4bWBfnLoZBEbrZAuANTVhgV53Ni0RcDvvec5cPMSzozpQLj8F3mQq9R3ycVFj4wi18pSj4u1vZBUOnjKN0SxcmkLtnar5aY5DHXuasqgTwS4u6ZBtaxlzQQZDZD")
##users = graph.search(type='user',q='Katarina Mazanka')
##for user in users['data']:
    ##print('%s %s' % (user['id'],user['name'].encode()))
class FacebookFeed:
    token_url = 'https://graph.facebook.com/oauth/access_token'
    params = dict(client_id=settings.SOCIAL_AUTH_FACEBOOK_KEY, client_secret=settings.SOCIAL_AUTH_FACEBOOK_SECRET,
                  grant_type='client_credentials')

    
    ##def get_posts(cls, user, count):
        ##try:
            ##token_response = requests.get(url=cls.token_url, params=cls.params)
            ##access_token = token_response.text.split('=')[1]
            ##graph = facebook.GraphAPI(access_token)
            ##profile = graph.get_object(user)
            ##query_string = 'posts?limit={0}'.format(count)
            #posts = graph.get_connections(profile['id'], query_string)
            #return posts
        #except facebook.GraphAPIError:
            #return None
profiles = graph.search(type = 'user',q = 'Katarina Mazanka')

for user in profiles['data']:
    print('%s %s' % (user['id'],user['name'].encode()))
##I am the first user in this print
user = '1547253215290162'
posts = graph.get_object(id = user, fields = 'posts', limit=100)
##posts = graph.get_object(id= user, fields ='feed', limit = 100)
print(posts)