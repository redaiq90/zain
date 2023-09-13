import jwt
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['GET'])
def callback():
    try:
        token = request.args.get('token')  # Example: ?token=jsjsj...
    except Exception:
        return "Token not found", 400

    # Process the callback data from POST request
    callback_data = request.json  # Assuming the callback data is in JSON format

    response_text = "Received Callback Data:\n"
    response_text += str(callback_data) + "\n\n"

    print("Received Callback Data:")
    print(callback_data)

    # Replace 'your_secret_key_here' with your actual secret key
    secret = '$2y$10$hBbAZo2GfSSvyqAyV2SaqOfYewgYpfR1O19gIh4SqyGWdmySZYPuS'

    if token:
        try:
            result = jwt.decode(token, secret, algorithms=['HS256'])
            result = dict(result)  # Convert to a dictionary

            print(f"Token: {token}")
            print(result)

            if result.get('status') == 'success':
                # Successful transaction
                print("Successful transaction")
                response_text += "Status: success\n"

            if result.get('status') == 'failed':
                # Failed transaction and its reason
                reason = result.get('msg')
                print(f"Failed transaction. Reason: {reason}")
                response_text += f"Status: failed\nReason: {reason}\n"

        except jwt.ExpiredSignatureError:
            print("Token has expired")
            response_text += "Status: error\nMessage: Token has expired\n"
        except jwt.InvalidTokenError:
            print("Invalid token")
            response_text += "Status: error\nMessage: Invalid token\n"

    # Return the response as plain text
    return response_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    
