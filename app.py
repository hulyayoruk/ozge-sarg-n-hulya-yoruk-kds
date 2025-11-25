from flask import Flask, render_template, request, redirect, url_for
import json
import random

app = Flask(__name__)

# --- ÖĞRETMEN KARAR DESTEK SİSTEMİ İÇİN SİMÜLE EDİLMİŞ VERİLER ---
# Bu veriler, CSV analizinizden türetilen bilgileri temsil eder.

TEACHER_DATA = {
    "class_name": "9/A Matematik Sınıfı",
    "teacher_name": "Ayşe Yılmaz",
    "class_overview_accuracy": 70.8,
    "struggling_topics": [
        {"name": "Rotations", "struggle_level": 95},
        {"name": "Surface Area Cylinder", "struggle_level": 88},
        {"name": "Volume Cylinder", "struggle_level": 76}
    ],
    "top_struggling_students": [
        {"id": 92007, "name": "Eren Yılmaz", "recent_score": 55, "hint_avg": 4.1},
        {"id": 88904, "name": "Defne Demir", "recent_score": 62, "hint_avg": 3.5},
        {"id": 78647, "name": "Srene Demir", "recent_score": 70, "hint_avg": 2.8}
    ]
}


# --- ROTALAR ---

@app.route('/')
def home():
    """Varsayılan ana sayfa girişe yönlendirir."""
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Öğretmen Giriş Ekranı ve İşlemi."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Gerçek bir uygulamada burada veritabanı kontrolü yapılır.
        # Simülasyon: Başarılı girişte dashboard'a yönlendir.
        if email and password:
            return redirect(url_for('teacher_dashboard'))

        return render_template('login.html', error="Hatalı e-posta veya şifre.")

    return render_template('login.html', error=None)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Öğretmen Kayıt Ekranı ve İşlemi."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        # Gerçek bir uygulamada burada veritabanına kayıt yapılır.
        print(f"Yeni Öğretmen Kaydı: {name}, E-posta: {email}")

        # Başarılı kayıttan sonra giriş ekranına yönlendir.
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/dashboard')
def teacher_dashboard():
    """Öğretmen Karar Destek Sistemi Dashboard'u."""

    # Karar Destek Önerileri Üretme Mantığı (Simülasyon)
    # Bu öneriler, TEACHER_DATA'daki analizlerden türetilmiştir.

    top_struggle_topic = TEACHER_DATA['struggling_topics'][0]['name']
    top_struggle_student = TEACHER_DATA['top_struggling_students'][0]

    decision_support_recommendations = [
        {
            "type": "Konu Odaklı",
            "text": f"Sınıfın en çok zorlandığı konu olan **{top_struggle_topic}** için ek alıştırmalar veya video kaynakları atayın.",
            "action": "Ders Materyali Ekle"
        },
        {
            "type": "Bireysel Öğrenci",
            "text": f"**{top_struggle_student['name']}** ({top_struggle_student['recent_score']}%) son denemelerinde düşük performans gösteriyor. Bire bir görüşme planlayın.",
            "action": "Görüşme Planla"
        },
        {
            "type": "Grup Çalışması",
            "text": "Ortalama zorluk seviyesindeki öğrencileri birbirleriyle eşleştirerek akran desteği grubu oluşturun.",
            "action": "Grup Oluştur"
        }
    ]

    # Dashboard'a veri ve rastgele 2 öneri gönder
    return render_template(
        'teacher.html',
        data=TEACHER_DATA,
        recommendations=random.sample(decision_support_recommendations, 2)
    )


if __name__ == '__main__':
    # Flask sunucusu 5000 portunda çalışır
    app.run(debug=True)