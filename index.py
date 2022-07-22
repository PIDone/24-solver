from flask import Flask, request, render_template
import solver

aaaaaa = "asdfg"
 
app = Flask(__name__)
app.static_folder = "static"  
 
@app.route("/", methods =["GET", "POST"])
def process():
	if request.method == "POST":
		numbers = []
		for i in range(1, 5):
			numbers.append(int(request.form.get("number{}".format(str(i)))))
		answer = solver.solve(numbers)
		return render_template("index.html", answer=answer)
	return render_template("index.html", answer="")
 
if __name__=='__main__':
   app.run()