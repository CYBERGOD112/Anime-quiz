from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secretkey"


# ✅ OOP CLASS
class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


# ✅ QUESTIONS (JAMB STYLE)
questions = [
    Question("In 'Naruto', who is the leader of Team 7?",
             ["A. Kakashi Hatake", "B. Jiraiya", "C. Tsunade", "D. Minato Namikaze"], "A"),
    Question("In 'One Piece', what is Luffy’s dream?",
             ["A. Find One Piece", "B. Become Pirate King", "C. Rule the Navy", "D. Find All Devils Fruits"], "B"),
    Question("Who is the main protagonist of 'Attack on Titan'?",
             ["A. Levi", "B. Eren Yeager", "C. Armin", "D. Mikasa"], "B"),
    Question("In 'Dragon Ball Z', what race is Vegeta?", ["A. Namekian", "B. Saiyan", "C. Human", "D. Android"], "B"),
    Question("In 'My Hero Academia', what is Deku’s real name?",
             ["A. Katsuki Bakugo", "B. Shoto Todoroki", "C. Izuku Midoriya", "D. All Might"], "C"),
    Question("Who created 'Death Note'?",
             ["A. Masashi Kishimoto", "B. Eiichiro Oda", "C. Tsugumi Ohba", "D. Yoshihiro Togashi"], "C"),
    Question("In 'Bleach', what is Ichigo’s weapon called?",
             ["A. Zanpakuto", "B. Bankai", "C. Spirit Sword", "D. Soul Blade"], "A"),
    Question("Which anime features a character named Edward Elric?",
             ["A. Black Clover", "B. Fullmetal Alchemist", "C. Naruto", "D. One Piece"], "B"),
    Question("In 'Tokyo Ghoul', what is Kaneki’s eye type called?",
             ["A. Sharingan", "B. Rinnegan", "C. Kakugan", "D. Byakugan"], "C"),
    Question("Who is the main female lead in 'Sword Art Online'?",
             ["A. Asuna Yuuki", "B. Alice Zuberg", "C. Sinon", "D. Leafa"], "A"),
    Question("In 'Demon Slayer', what is Tanjiro’s sword style?",
             ["A. Water Breathing", "B. Flame Breathing", "C. Moon Breathing", "D. Beast Breathing"], "A"),
    Question("Who is the villain in 'Naruto' that uses the Akatsuki ring?",
             ["A. Orochimaru", "B. Pain", "C. Kabuto", "D. Zabuza"], "B"),
    Question("Which anime has the characters Natsu, Lucy, and Happy?",
             ["A. Fairy Tail", "B. One Piece", "C. Bleach", "D. Black Clover"], "A"),
    Question("In 'One Punch Man', who is the main hero?", ["A. Genos", "B. Saitama", "C. Garou", "D. Bang"], "B"),
    Question("Which anime features 'Quirks' as superpowers?",
             ["A. Naruto", "B. My Hero Academia", "C. One Piece", "D. Dragon Ball Z"], "B"),
    Question("In 'Black Clover', who is Asta’s rival?", ["A. Yuno", "B. Noelle", "C. Licht", "D. Finral"], "A"),
    Question("Who is the captain of the Survey Corps in 'Attack on Titan'?",
             ["A. Eren Yeager", "B. Levi Ackerman", "C. Erwin Smith", "D. Armin Arlert"], "C"),
    Question("Which anime has a character named Rimuru Tempest?",
             ["A. That Time I Got Reincarnated as a Slime", "B. Re:Zero", "C. Overlord", "D. Log Horizon"], "A"),
    Question("In 'Dragon Ball Z', who is Goku’s brother?", ["A. Raditz", "B. Vegeta", "C. Broly", "D. Bardock"], "A"),
    Question("Which anime features the story of a notebook that can kill people?",
             ["A. Code Geass", "B. Death Note", "C. Psycho-Pass", "D. Akame ga Kill"], "B")
]

# ✅ QUEUE (FIFO)
question_queue = questions.copy()


# 🏠 HOME PAGE
@app.route("/")
def index():
    session["score"] = 0
    session["q_index"] = 0
    return render_template("index.html")


# ❓ QUIZ PAGE
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        user_answer = request.form.get("answer")
        q_index = session.get("q_index")

        current_question = questions[q_index]

        if current_question.check_answer(user_answer):
            session["score"] += 1

        session["q_index"] += 1

    q_index = session.get("q_index")

    if q_index >= len(questions):
        return redirect(url_for("result"))

    return render_template("quiz.html", question=questions[q_index], q_num=q_index+1)


# 📊 RESULT PAGE
@app.route("/result")
def result():
    score = session.get("score")
    total = len(questions)
    time = datetime.now().strftime("%I:%M %p")

    return render_template("result.html", score=score, total=total, time=time)


if __name__ == "__main__":
    app.run(debug=True)