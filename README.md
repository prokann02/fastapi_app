<h1>FastAPI App with Docker</h1>

<hr>

<p>This is a small application built with FastAPI, uvicorn, aiosqlite, and sqlalchemy.</p>
<p>The app showcases a customizable product list, adaptable to your needs.</p>
<p>Crafted for educational and demonstration purposes.</p>

<hr>

<h3>Installation instructions:</h3>
<p>git clone https://github.com/prokann02/fastapi_app.git</p>
<p>cd fastapi_app</p>

<p>docker build -t fastapi-app .</p>
<p>docker run -d -p 80:80 fastapi-app</p>

<hr>
<p>Once the container is running, you can access the FastAPI application at 
<b><a href="http://localhost:80">http://localhost:80</a></b>.</p>
<p>To see page with which you can interact, click <b><a href="http://localhost:80/docs">http://localhost:80/docs</a></b>.</p>
<p>You will see:</p>
<img src="img.png">




