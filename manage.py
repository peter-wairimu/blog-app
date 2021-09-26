from flask_sqlalchemy import SQLAlchemy
from app import create_app, db
from app.models import User,Post,Comment,Like
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand


app = create_app('production')
manage = Manager(app)
manage.add_command('server',Server)
@manage.command


def test():
    '''
    Run the unit tests.

    '''
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manage.shell
def make_shell_context():
    return dict(app = app,db = db,User= User,Post = Post,Like=Like,Comment=Comment)
    


migrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)
db = SQLAlchemy(app)


if __name__ == '__main__':
    manage.run()