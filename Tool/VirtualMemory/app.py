from flask import Flask, flash, redirect, request, render_template
from algo import *
from utils import *

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = 'unique-key'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        algo = request.form.get("algorithm")

        org_frames = request.form.get("frames")
        org_data = request.form.get("data")
        
        if not org_frames or not org_data:
            return render_template("index.html")
        
        frames = int(org_frames.strip()) if org_frames.isnumeric() else 1
        data = [int(num) for num in org_data.strip().split(' ') if num.isnumeric()]

        HIT = 0
        MISS = 0
        algorithm = ""

        if algo == "fifo":
            
            algo_data, HIT, MISS = FIFO(data, frames)

            algo_data = transform_data(algo_data)

            headings = data

            algorithm = "FIFO"
        elif algo=='lru':
            algo_data, HIT, MISS = LRU(data, frames)

            algo_data = transform_data(algo_data)

            headings = data

            algorithm = "LRU"
        elif algo=='mru':
            algo_data, HIT, MISS = MRU(data, frames)

            algo_data = transform_data(algo_data)

            headings = data

            algorithm = "MRU"  
        elif algo=="lfu":
            algo_data, HIT, MISS = LFU(data, frames)

            algo_data = transform_data(algo_data)

            headings = data

            algorithm = "LFU"
        elif algo=="mfu":
            algo_data, HIT, MISS = MFU(data, frames)

            algo_data = transform_data(algo_data)

            headings = data

            algorithm = "MFU"   
        elif algo=="sc":
            algo_data, HIT, MISS = SecondChance(data, frames)

            algo_data = transform_data(algo_data)

            headings = data

            algorithm = "Second Chance"                            
        elif algo=='opt':
            algo_data, HIT, MISS = OPT(data, frames)

            algo_data = transform_data(algo_data)

            headings = data

            algorithm = "Optimal"
        HIT_RATIO = round((HIT / len(data)), 2) * 100
        MISS_RATIO = round((MISS / len(data)), 2) * 100
        return render_template('index.html', headings=headings, data=algo_data, org_data=org_data, org_frames=org_frames,
                                HIT=HIT, MISS=MISS, HIT_RATIO = HIT_RATIO, MISS_RATIO = MISS_RATIO, algorithm=algorithm)       
        
    else:
        return render_template('index.html')

@app.route('/pass.html', methods=['POST'])
def get():
    return request.form['name']
if __name__ == '__main__':
    app.run(debug=True)