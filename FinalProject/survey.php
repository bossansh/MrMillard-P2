<!DOCTYPE html>
<html>
  <head>
    <title>Survey</title>
    <link rel="stylesheet" href="style.css"> <!-- external style -->
    <style>
      html {
        background-image: url('/IMAGES/kingdown.jpeg');
        background-size: cover;
        min-height: 100%;
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
      }
    </style>
  </head>
  <body>
    <form action = "surveyanswer.php" method = "post">
      <h1>What is your favorite opening?</h1>
      <input type="text" name="FavOpening" placeholder="Name of opening">
      <button type = "submit">Submit</button>
    </form>
  </body>
</html>
