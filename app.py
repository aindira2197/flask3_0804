from flask import Flask, render_template

app = Flask(__name__)

talabalar = ["Zafar", "Malika", "Ali", "Gulnora", "Bekzod"]

@app.route('/talabalar/<ism>')
def ism_uzunlik(ism):
    if ism in talabalar:
        uzunlik = len(ism)

        if uzunlik >= 6:
            kategoriya = "Uzun ism"
        else:
            kategoriya = "Qisqa ism"

        return render_template(
            'uzunlik.html',
            ism=ism,
            uzunlik=uzunlik,
            kategoriya=kategoriya
        )
    else:
        return f"{ism} ro'yxatda topilmadi ❌"


if __name__ == "__main__":
    app.run(debug=True)
