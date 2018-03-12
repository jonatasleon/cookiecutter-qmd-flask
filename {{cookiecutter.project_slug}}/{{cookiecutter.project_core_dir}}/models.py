from flask_security import RoleMixin, UserMixin, SQLAlchemySessionUserDatastore
from {{cookiecutter.project_core_dir}} import db

role_users = db.Table(
    'role_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role _id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer())
    roles = db.relationship(
        'Role',
        secondary=role_users,
        backref=db.backref('users', lazy='dynamic')
    )

    def get_security_payload(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }

    def __str__(self):
        return self.email


user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)


# Add your own models
