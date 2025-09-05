from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
CVS_file = 'static/cvs/cv_list.csv'
app.secret_key = 'secret_key_for_flash_messages'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('remember') == 'on'

        if not email or not password:
            flash('Email və şifrə daxil edilməlidir!', 'error')
            return redirect(url_for('login'))

        flash(f"Xoş gəlmisiniz, {email}! Şifrəni yadda saxla: {remember}", 'success')
        return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4600)
