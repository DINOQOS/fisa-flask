from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
   # app.py인 곳을 입구로 찾아서 기본적으로 실행합니다.
   # 또는 FLASK_APP이라는 환경변수의 이름을 파일명으로 변경
   # set FLASK_APP=test
   # wsgi.py에 직접 키=밸류로 여러 환경변수들을 기입합니다.

import config


db = SQLAlchemy()
migrate = Migrate()


def create_app():
   test = Flask(__name__)

   # ORM DB정보를 먼저 메모리에 올려놓음
   test.config.from_object(config)
   db.init_app(test)
   migrate.init_app(test, db)

   # 블루프린트
   from .views import main_views, board_views # views 폴더 밑의 mina_views
   test.register_blueprint(main_views.bp)
   test.register_blueprint(board_views.board)

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