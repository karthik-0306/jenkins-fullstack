from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/student-details', methods=['GET'])
def get_student_details():
    # Only returning Name and Roll Number as requested
    return jsonify({
        "name": "Thota Sai Karthik",
        "roll_number": "2023bcs0159"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)