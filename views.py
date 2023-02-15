from __init__ import *

def home_page():
    # print(os.environ)
    # if not User.query.filter(User.email == 'member@example.com').first():
    #     user = User(
    #         email='member@example.com',
    #         email_confirmed_at=datetime.datetime.utcnow(),
    #         password=user_manager.hash_password('Password1'),
    #     )
    #     db.session.add(user)
    #     db.session.commit()

    # # Create 'admin@example.com' user with 'Admin' and 'Agent' roles
    # if not User.query.filter(User.email == 'admin@example.com').first():
    #     user = User(
    #         email='admin@example.com',
    #         email_confirmed_at=datetime.datetime.utcnow(),
    #         password=user_manager.hash_password('Password1'),
    #     )
    #     user.roles.append(Role(name='Admin'))
    #     user.roles.append(Role(name='Agent'))
    #     db.session.add(user)
    #     db.session.commit()
    return render_template('app/index.html')
    
@roles_required('Admin')    # Use of @roles_required decorator
def admin_page():
    return render_template('app/admin.html')
@login_required 
def member_page():
    return render_template('app/member.html')
@login_required
def buttons():
    return render_template('public/buttons.html')
@login_required
def cards():
    return render_template('public/cards.html')
@login_required
def charts():
    return render_template('public/charts.html')
@login_required
def forms():
    return render_template('public/forms.html')
@login_required
def modals():
    return render_template('public/modals.html')
@login_required
def modals():
    return render_template('public/modals.html')
@login_required
def tables():
    return render_template('public/tables.html')
@login_required
def dashboard():
    return render_template('public/dashboard.html')

def create_account():
    return render_template('public/pages/create-account.html')
def e404():
    return render_template('public/pages/404.html')
def blank():
    return render_template('public/pages/blank.html')
def login():
    return render_template('public/pages/login.html')
def forgot_password():
    return render_template('public/pages/forgot-password.html')