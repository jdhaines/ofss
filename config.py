"""Primary flask configuration file."""
import os

# globals
WTF_CSRF_ENABLED = True
SECRET_KEY = '^&H2i@Wtq&9pd8pa6#EtUheKvENfS2'
BASEDIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'blogposts.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
RECAPTCHA_PARAMETERS = {'hl': 'zh', 'render': 'explicit'}
RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}
RECAPTCHA_PUBLIC_KEY = '6LcYeiUTAAAAAIqSR-KXWX3Bp5PZ28AMcvgw0spD'
RECAPTCHA_PRIVATE_KEY = '6LcYeiUTAAAAAK_mvpCsQ8q_TVLIhgoDs6rkb7o_'

# Blogging Config
BLOGGING_URL_PREFIX = "/blog"
BLOGGING_DISQUS_SITENAME = None
BLOGGING_SITEURL = "http://localhost:5000"

# end
