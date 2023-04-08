% rebase('layout.tpl', title='Home Page', year=year,error=error,quest=quest,name=name,email=email)

<div class="jumbotron">
    <img src="static\images\logo.png"> 
    <p> </p>
    <p class="lead">Bottle is a free web framework for building great Web sites and Web applications using HTML, CSS and JavaScript.</p>
    <p><a href="http://bottlepy.org/docs/dev/index.html" class="btn btn-primary btn-large">Learn more &raquo;</a></p>
</div>

<div class="row">
    <div class="col-md-4">

        <h2>Getting started</h2>
        <p>
            Bottle gives you a powerful, patterns-based way to build dynamic websites that
            enables a clean separation of concerns and gives you full control over markup
            for enjoyable, agile development.
        </p>
        <p><a class="btn btn-default" href="http://bottlepy.org/docs/dev/index.html">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Get more libraries</h2>
        <p>The Python Package Index is a repository of software for the Python programming language.</p>
        <p><a class="btn btn-default" href="https://pypi.python.org/pypi">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Microsoft Azure</h2>
        <p>You can easily publish to Microsoft Azure using Visual Studio. Find out how you can host your application using a free trial today.</p>
        <p><a class="btn btn-default" href="http://azure.microsoft.com">Learn more &raquo;</a></p>
    </div>
</div>
<h3> Ask a Question </h3>
<form action="/myform" method="post">
        <p><textarea rows="2" cols="50" name="QUEST" placeholder="Your question" >{{quest}}</textarea></p> 
        <p><input type="text" size="50" name="NAME" placeholder="Your name" value={{name}}></input></p>
        <p><input type="text" size="50" name="ADRESS" placeholder="Your email" value={{email}}></input></p>
        <p>{{error}}</p>
        <p ><input class="btn btn-default" type="submit" value="Send"></p>
</form>
   