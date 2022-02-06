from flask import Flask, render_template, jsonify
import configs.main_config
from controllers import book_controller, entrance_controller
from middlewares import auth

app = Flask(__name__, template_folder=configs.main_config.APP.get("template_folder"))

app.register_blueprint(book_controller.books_blueprint, url_prefix='/api/books' )
app.register_blueprint(entrance_controller.entrance_blueprint, url_prefix='/api/entrance')

app.before_request_funcs = {
    # blueprint name: [list_of_functions]
    'books': [auth.is_auth, auth.is_admin]
}
# www.localhost:8080
@app.route('/', methods=['GET']) 
def home():
    return render_template(
        '/home/index.html',
        title='Flask-Login Tutorial.',
        body="You are now logged in!"
    )

# www.localhost:8080/score/<int:score>
@app.route('/score/<int:score>', methods=['GET'])
def score(score):
    # request.args.get('username')
    result = { "msg": "", "your_score": score}
    if score < 50:
        result["msg"] = "Your result is fail"
        return jsonify(result), 200
    result["msg"] = "Your result is pass"
    return jsonify(result), 200
     


if __name__ == '__main__':
    app.run(configs.main_config.APP.get("host"), configs.main_config.APP.get("port"), configs.main_config.APP.get("debug"))