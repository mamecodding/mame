from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Flash mesajları için secret_key


# Anasayfa yönlendirmesi
@app.route('/')
def home():
    return render_template('login.html')  # Giriş sayfası


# Kayıt sayfası yönlendirmesi
@app.route('/register')
def register():
    return render_template('register.html')  # Kayıt sayfası


# Login işlemi
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Örnek kullanıcı doğrulama
    if username == 'admin' and password == 'admin':
        flash('Giriş başarılı!', 'success')  # Başarı mesajı
        return redirect(url_for('dashboard'))  # Kontrol paneline yönlendir
    else:
        flash('Kullanıcı adı veya şifre yanlış', 'danger')  # Hata mesajı
        return redirect(url_for('home'))  # Giriş sayfasına geri yönlendir


# Kontrol paneli sayfası
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # Dashboard sayfası


# Yayın ekleme işlemi
@app.route('/add_program', methods=['POST'])
def add_program():
    program_name = request.form['program_name']
    program_time = request.form['program_time']
    program_type = request.form['program_type']

    # Flash mesajı olarak program bilgilerini göster
    flash(f'{program_name} programı başarıyla eklendi! Yayın saati: {program_time}, Tür: {program_type}', 'success')

    return redirect(url_for('dashboard'))  # Kontrol paneline yönlendir


if __name__ == '__main__':
    app.run(debug=True)
