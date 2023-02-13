from __init__ import *
from views import *

app.add_url_rule('/', 'home_page', home_page, methods=['POST', 'GET'])
app.add_url_rule('/members', 'member_page', member_page, methods=['POST', 'GET'])
app.add_url_rule('/admin', 'admin_page', admin_page, methods=['POST', 'GET'])