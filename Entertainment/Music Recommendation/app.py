from flask import Flask, render_template, request
from api_integration import recommend
from flask_jwt_extended import JWTManager, jwt_required
from logging import getLogger

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)
logger = getLogger(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_id = request.form['user_id']
        recommendations = recommend(user_id)
        return render_template('recommendations.html', recommendations=recommendations)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)