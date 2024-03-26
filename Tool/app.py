from flask import Flask, flash, redirect, request, render_template
from Data import *
from deadlock import *

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = 'unique-key'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        algo = request.form.get("algorithm")
        if 'file' not in request.files:
            
            flash('No file part')
            return redirect(request.url)
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        
        file_content = file.read().decode('utf-8').split("\n")

        data = []
        for i in file_content:
            data.append(i)

        element = []

        for i in data:
            element.append([int(e) for e in i.split(' ')])

        if (algo == "banker"):
            
            data = handle_data_for_res_req(element)
            allocation = data[0]
            need = data[1]
            available = data[2]
            resources = data[3]
            max = data[4]

            resource_headings = []
            for i in range(len(allocation[0])):
                resource_headings.append(chr(ord('A') + i))
            resource_data = []
            for j in range(len(resources)):
                tmp = ''
                tmp += str(resources[j])
                resource_data.append(tmp)
            
                
            table_headings = ('Index','Allocation', 'Max', 'Need')

            table_resource = []

            banker_algo_table = []

            banker_algo_headings = ('Index', 'Need', 'Work', '<=')

            for i in range(len(allocation)):
                table_source_element = []
                table_source_element.append(str(i))
                table_source_element.append(append(allocation[i]))
                table_source_element.append(append(max[i]))
                table_source_element.append(append(need[i]))
                table_resource.append(table_source_element)

            banker_data, res, safe_list, unsafe_process = banker(allocation, need, available)
            
            print(res)
            if (res == 1):
                paragraph = "It is safe with the list of processes of <" + safe_list[:-1] +">"
            else:
                paragraph = "It is not safe with the process " + str(unsafe_process)
            return render_template('index.html', table_1_headings=resource_headings, table_1_data=resource_data,
                                    table_2_headings=table_headings, table_2_data=table_resource,
                                    table_3_headings=banker_algo_headings, table_3_data=banker_data, result=res, conclusion_paragraph=paragraph)
        elif algo=='detection':
            data = handle_data_for_detection(element)


            detection_algo_headings = ('Index', 'Allocation', 'Request', 'Work', 'Request <= Work')

            detection_data, res, safe_list = detection(data)
            
            if (res):
                paragraph = "It is safe with the list of processes of <" + safe_list +">"
            else:
                paragraph = "It is not safe with the process " + str(detection_data)

            return render_template('index.html', table_2_headings=detection_algo_headings, table_2_data=detection_data, conclusion_paragraph=paragraph)
    else:
        return render_template('index.html')

@app.route('/pass.html', methods=['POST'])
def get():
    return request.form['name']
if __name__ == '__main__':  
    app.run(debug=True)


