from __init__ import *
from views import *

app.add_url_rule('/', 'home_page', home_page, methods=['POST', 'GET'])
app.add_url_rule('/members', 'member_page', member_page, methods=['POST', 'GET'])
app.add_url_rule('/admin', 'admin_page', admin_page, methods=['POST', 'GET'])
app.add_url_rule('/dashboard', 'dashboard', dashboard, methods=['POST', 'GET'])
app.add_url_rule('/buttons', 'buttons', buttons, methods=['POST', 'GET'])
app.add_url_rule('/cards', 'cards', cards, methods=['POST', 'GET'])
app.add_url_rule('/charts', 'charts', charts, methods=['POST', 'GET'])
app.add_url_rule('/forms', 'forms', forms, methods=['POST', 'GET'])
app.add_url_rule('/modals', 'modals', modals, methods=['POST', 'GET'])
app.add_url_rule('/tables', 'tables', tables, methods=['POST', 'GET'])

app.add_url_rule('/pages/login', 'login', login, methods=['POST', 'GET'])
app.add_url_rule('/pages/create-account', 'create_account', create_account, methods=['POST', 'GET'])
app.add_url_rule('/pages/forgot-password', 'forgot_password', forgot_password, methods=['POST', 'GET'])
app.add_url_rule('/pages/404', 'e404', e404, methods=['POST', 'GET'])
app.add_url_rule('/pages/blank', 'blank', blank, methods=['POST', 'GET'])