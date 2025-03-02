from flask import Flask, render_template, send_from_directory, request, make_response
import os

app = Flask(__name__)

def get_client_ip():
    """Extracts the real client IP behind a proxy (e.g., Render)"""
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(',')[0]  # Get the first IP in the list
    return request.remote_addr  # Fallback if no header is present

@app.route('/')
@app.route('/<path:path>')
def home(path=None):
    user_ip = get_client_ip()  # Get the real client IP
    user_agent = request.headers.get('User-Agent')  # Get browser info
    referrer = request.referrer  # Get referrer (if available)

    # Log info to console
    print(f"IP: {user_ip}, User-Agent: {user_agent}, Referrer: {referrer}")

    return render_template('home.html')

@app.route('/static/<path:filename>')
def get_image(filename):
    user_ip = get_client_ip()  # Get the real client IP
    user_agent = request.headers.get('User-Agent')  # Get browser info
    referrer = request.referrer  # Get referrer (if available)

    # Log info to console
    print(f"IP: {user_ip}, User-Agent: {user_agent}, Referrer: {referrer}")

    # Send the image with a no-cache policy
    response = make_response(send_from_directory('static', filename))
    response.headers['Content-Type'] = 'image/jpeg'  # Set correct MIME type
    response.headers['Cache-Control'] = 'public, max-age=86400'  # Allow caching
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    
    return response
@app.errorhandler(404)
def page_not_found(error):
    user_ip = get_client_ip()  # Get the real client IP
    user_agent = request.headers.get('User-Agent')  # Get browser info
    referrer = request.referrer  # Get referrer (if available)
    requested_path = request.path  # Get the requested path

    # Log the 404 request details
    print(f"404 ERROR -> IP: {user_ip}, Path: {requested_path}, User-Agent: {user_agent}, Referrer: {referrer}")

    return f"404 Not Found\nIP: {user_ip}\nRequested Path: {requested_path}", 404
    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render provides a PORT variable
    app.run(host="0.0.0.0", port=port)
