from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', message='')

@app.route('/', methods=['POST'])
def result():
    file_choice = request.files.get('file')
    file_choice.save('./uploads/' + file_choice.filename)
    return render_template('index.html', message="アップロードが完了しました！")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')