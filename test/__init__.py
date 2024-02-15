from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
   # app.py인 곳을 입구로 찾아서 기본적으로 실행합니다.
   # 또는 FLASK_APP이라는 환경변수의 이름을 파일명으로 변경
   # set FLASK_APP=test
   # wsgi.py에 직접 키=밸류로 여러 환경변수들을 기입합니다.

import config


# db = SQLAlchemy()
migrate = Migrate()
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))

def create_app():
   test = Flask(__name__)
   test.config.from_object(config)

   # ORM
   db.init_app(test)
   if test.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
      migrate.init_app(test, db, render_as_batch=True)
   else:
      migrate.init_app(test, db)


   # 블루프린트
   from .views import main_views, board_views, answer_views, auth_views # views 폴더 밑의 mina_views
   test.register_blueprint(main_views.bp)
   test.register_blueprint(board_views.board)
   test.register_blueprint(answer_views.answer)
   test.register_blueprint(auth_views.auth)

   # 커스텀 필터 사용
   from test.filters import format_datetime
   test.jinja_env.filters['date_time'] = format_datetime

   return test

   @test.route("/")
   def hello():
      return f'Hello {__name__}' 

   #localhost:5000/bye 로 접속하면 bye만 출력되도록 컨트롤러

   @test.route("/fisa/bye")
   def bye():
      return f'bye'
   
   @test.route("/fisa/about_me")
   def about_me():
      return f'저는 장정우입니다.'
   
   @test.route("/fisa/hi")
   def hi():
      return f'안녕하세요.'   

   return test


