from cypher import Cypher
from token import CONFIG

token = CONFIG['token']
get_url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={}'.format(token)
post_url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={}'.format(token)
filename = 'answer.json'

c = Cypher(get_url, post_url, filename)
print(c.decrypt())
c.update()