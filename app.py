from flask import Flask,render_template,jsonify 
app=Flask(__name__)
Jobs=[  
  #Job list ,inside list the set of dictionaries are there 
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'FrontEnd Engineer',
    'location':'Delhi, India',
    'salary':'Rs. 15,00,000'
  },
  {
    'id':3,
    'title':'Backend Engineer',
    'location':'Remote',
    'salary':'Rs. 12,00,000'
  },
  {
    'id':4,
    'title':'Data Scientist',
    'location':'San Francisco,USA',
    'salary':'Rs.$130,000'
  },
]
#in html endpoint 
@app.route("/")
def carrers_web():
  return render_template('home.html',JOBS=Jobs)
#In json endpoint
@app.route("/api/jobs")
def list_jobs():
  return jsonify(Jobs) #json is just js objects ,rest API,json Api,Api end point means web server returning some info not just as html verson can also retutrn in the  form of json data and  if we put / with the router name given here its jobs
if __name__=='__main__':
  app.run(host="0.0.0.0",debug=True)
