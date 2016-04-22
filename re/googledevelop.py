import re
match =re.search(r'iii','piiig')
if match:
    print 'found',match.group()
else:
    print 'did not find'