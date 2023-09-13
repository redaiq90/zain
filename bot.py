import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    # Capture the query parameters
    try:
        token = request.args.get('token')  # Example: ?token=jsjsj...
        #print(token)
    except Exception:
        continue
    # Process the callback data from POST request
    callback_data = request.json  # Assuming the callback data is in JSON format
    print("Received Callback Data:")
    
    print(json.dumps(callback_data, indent=2))
    print(f"Token: {token}")
    # Here, you can add your logic to handle the callback data

    return jsonify({'message': 'Callback Received'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    
