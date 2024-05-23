from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return 'Hello Flask'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)

# comment to check the branch flow
# comment to check the branch flow