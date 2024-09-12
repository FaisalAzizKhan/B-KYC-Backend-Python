def require_secret_key(f):
    def decorator(*args, **kwargs):
        print("Middleware triggered")  # Debugging statement
        if request.method == 'POST':
            secret_key = request.form.get('secret_key')
        else:
            secret_key = request.args.get('secret_key')
        
        print(f"Secret Key: {secret_key}")  # Debugging statement
        
        if secret_key != SECRET_KEY:
            return jsonify({'error': 'Unauthorized'}), 401
        
        return f(*args, **kwargs)
    return decorator
