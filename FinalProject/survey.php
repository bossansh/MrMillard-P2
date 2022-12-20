<!DOCTYPE html>
<html>
  <head>
    <title>Survey</title>
    <link rel="stylesheet" href="phpcss.css"> <!-- external style -->
    <style>
      html {
        background-image: url('IMAGES/kingdown.jpeg');
        background-size: cover;
        min-height: 100%;
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
      }
    </style>
  </head>
  <body>
    <form action="surveyanswer.php" method="post">
       <h2>What is your favorite chess opening?</h2>
       <label>Favorite Opening</label>
       <input type="text" name="FavOpening" placeholder="Opening name"><br>
       <button type="submit" name = "submit">Submit</button>
    </form>
  </body>
  </html>

