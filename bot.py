import jwt
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['GET'])
def callback():
    try:
        token = request.args.get('token')  # Example: ?token=jsjsj...
    except Exception:
        return "Token not found"

    print(f"Received Token: {token}")

    # Replace 'your_secret_key_here' with your actual secret key
    secret = '$2y$10$hBbAZo2GfSSvyqAyV2SaqOfYewgYpfR1O19gIh4SqyGWdmySZYPuS'

    if token:
        try:
            result = jwt.decode(token, secret, algorithms=['HS256'])
            print(result)
            result = dict(result)  # Convert to a dictionary

            print(f"Token: {token}")
            print(result)

            if result.get('status') == 'success':
                # Successful transaction
                print("Successful transaction")

            if result.get('status') == 'failed':
                # Failed transaction and its reason
                reason = result.get('msg')
                print(f"Failed transaction. Reason: {reason}")

        except jwt.ExpiredSignatureError:
            print("Token has expired")
        except jwt.InvalidTokenError:
            print("Invalid token")

    # Here, you can add your logic to handle the callback data

    return "Callback received"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    
