from flask import (Blueprint, render_template)
import json
pets= json.load(open('pets.json'))
print = pets

bp = Blueprint('pet', __name__, url_prefix="/pets")

# pet index route
@bp.route('/')
# method named index
def index():
    return render_template('index.html', pets=pets)