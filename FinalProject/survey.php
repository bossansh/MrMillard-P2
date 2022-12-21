<!DOCTYPE html>
<html>
  <head>
    <title>Survey</title> <!--Title of page and referring to phpcss.css for the css -->
    <link rel="stylesheet" href="phpcss.css"> <!-- external style -->
    <style>
      html {
        background-image: url('IMAGES/kingdown.jpeg');
        background-size: cover; <!-- adds background image to the page -->
        min-height: 100%;
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
      }
    </style>
  </head>
  <body>
    <form action="surveyanswer.php" method="post">
       <h2>What is your favorite chess opening?</h2> <!-- makes survey with the question of the favorite opening, and when submitted, goes to surveyanswer.php -->
       <label>Favorite Opening</label>
       <input type="text" name="FavOpening" placeholder="Opening name"><br>
       <button type="submit" name = "submit">Submit</button>
    </form>
    <li style=""><a href="index.html" style="background-color: #1a1a1a;">Back</a></li> <!-- goes back to home if the user wishes to do so -->
  </body>
</html>

