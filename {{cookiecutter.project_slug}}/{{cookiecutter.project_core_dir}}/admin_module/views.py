from flask_admin.contrib.sqla import ModelView as BaseModelView
from flask_babelex import gettext, ngettext
from flask_security import current_user, utils
from wtforms.fields import PasswordField

from {{cookiecutter.project_core_dir}} import db, models


def get_views():
    return [
        UserAdmin(),
        RoleAdmin(),
    ]


class ModelView(BaseModelView):
    __model__ = None
    __session__ = db.session

    def __init__(self):
        if not self.__model__:
            raise NotImplementedError('__model__ must be defined')
        super(ModelView, self) \
            .__init__(self.__model__, self.__session__)


class UserAdmin(ModelView):
    __model__ = models.User
    column_exclude_list = ('password',)
    form_excluded_columns = ('id', 'password',)
    column_labels = {
        'name': gettext('Nome'),
        'email': gettext('E-mail'),
        'password': gettext('Senha'),
        'active': gettext('Ativo'),
        'confirmed_at': gettext('Confirmado em'),
        'roles': gettext('Cargos'),
    }

    column_auto_select_related = True

    def is_accessible(self):
        return current_user.has_role('admin')

    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()
        form_class.password2 = PasswordField('New Password')
        return form_class

    def on_model_change(self, form, model, is_created):
        if len(model.password2):
            model.password = utils.encrypt_password(model.password2)


class RoleAdmin(ModelView):
    __model__ = models.Role

    def is_accessible(self):
        return current_user.has_role('admin')
