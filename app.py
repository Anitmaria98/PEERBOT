from flask import Flask, jsonify

app = Flask(__name__)

# Route to return student number in JSON format
@app.route('/', methods=['GET'])
def get_student_number():
    student_number = 200584979
    return jsonify({'student_number': student_number})

# Route to return text for Dialogflow integration
@app.route('/webhook', methods=['GET'])
def webhook():
    response_text = "Sure, I can help you schedule a meeting with $person."
    return response_text

if __name__ == '__main__':
    app.run(debug=True)

