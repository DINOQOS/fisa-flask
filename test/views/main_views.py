from flask import Blueprint
from ..models import Question
from flask import render_template

# 우리가 부를 이름, flask 프레임워크가 찾을 이름, 라우팅주소
bp = Blueprint('main', __name__, url_prefix="/")

# 첫번째 blueprint부터 찾기 때문에 board를 쓸 수 없게 됩니다 
# @bp.route("/", defaults={"var":'', "var2":""}) # 여러개의 route 어노테이션을 하나의 메서드에 얹어서 쓸 수도 있다
# @bp.route("/<var>/<var2>")  #대부분 uri는 str로 받기 때문에 str은 생략 # localhost:5000/yeonji  -> hello yeonji가 출력되도록 
@bp.route("/")
def index():

    return render_template("index.html")

@bp.route("/bye")
def bye():
    return f'BYE'