from flask import Flask, render_template,send_from_directory,request
import logging,requests
app = Flask(__name__)


    
@app.route('/')
def home():
    user_ip = request.remote_addr  # Get IP
    user_agent = request.headers.get('User-Agent')  # Get browser info
    referrer = request.referrer  # Get referrer (if available)

    # Log info to console
    print(f"IP: {user_ip}, User-Agent: {user_agent}, Referrer: {referrer}")

    return render_template('home.html')

@app.route('/image')
def get_image():
    user_ip = request.remote_addr  # Get IP
    user_agent = request.headers.get('User-Agent')  # Get browser info
    referrer = request.referrer  # Get referrer (if available)

    # Fetch extra details from ipinfo.io
    ip_details = get_ip_info(user_ip)

    # Log info to console
    print(f"IP: {user_ip}, User-Agent: {user_agent}, Referrer: {referrer}")


    return send_from_directory('static', 'japan.jpg')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
