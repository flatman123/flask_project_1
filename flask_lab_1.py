from flask import Flask, render_template
app = Flask(__name__)


about_content =[
{
"content": '''
Externally Visible Server
If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

flask run --host=0.0.0.0
This tells your operating system to listen on all public IPs.
'''
}
]

content = [
		"This is test content number_1",
		"This is test content number_2",
		"This is test content number_3"
]

blog_items = [
		{
		"title": "Author1\'s BLOG TITLE",
		"author": "Authro1 Lastname",
		"date": "Feb, 26, 2019",
		"blog_posts": content[0]
		},
		{
		"title": "Author2\'s BLOG TITLE",
		"author": "Authro2 Lastname",
		"date": "Feb, 3 1984",
		"blog_posts": content[1]
		}

]

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", posts=blog_items, title="JEFF\'S NEW BLOG!")

@app.route("/about")
def about():
	return render_template("about.html", posts=about_content)

@app.route("/login")
def login():
	pass

@app.route("/contact")
def contact():
	pass






if __name__ == "__main__":
	app.run(debug=True)

