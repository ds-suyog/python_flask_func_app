from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def functions():
  return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
  if request.form["submit"] == "submit":
    import funcs
    if request.form['factorial'] != '':
      fact_input = int(request.form['factorial'])
      result_fact = funcs.fact(fact_input)
    else:
      fact_input = ''
      result_fact = ''

    if request.form['fibonacci'] != '':
      fibo_input = int(request.form['fibonacci'])    
      result_fibo = funcs.fibo(fibo_input) 
    else:
      result_fibo = ''

    if request.form['armstrong'] != '':
      arms_input = int(request.form['armstrong'])
      result_arms = funcs.isarmstrong(arms_input)
    else:
      result_arms = ''

    if request.form['palindrome'] != '':
      pal_input = request.form['palindrome']
      result_palin = funcs.ispalin(pal_input)
    else:
      result_palin = ''                
    return render_template('display.html', fact_in = fact_input, r_fact = result_fact, r_fibo = result_fibo, r_arms = result_arms, r_palin = result_palin)
 
  elif request.form["submit"] == "back":
    return render_template('my-form.html')

if __name__ == '__main__':
    app.run()