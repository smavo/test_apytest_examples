from woocommerce import API
import pprint

wcapi = API(
    url="http://localhost/wordpress",
    consumer_key='ck_ed3798998982d615242e297ae280584b65ca106c',
    consumer_secret='cs_10d514e7824ea92d00c8a1970d713b557e13d7c3',
    version='wc/v3'
)

result = wcapi.get('products')

pprint.pprint(result.json())
