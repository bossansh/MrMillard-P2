<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="phpcss.css"> <!-- external style -->
    <style>
      html {
        background-image: url('IMAGES/blackchesspieces.jpeg');
        background-size: cover; /* adds background image to the page */
        min-height: 100%;
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
      }
    </style>
  </head>
  <body>
    <li style=""><a href="index.html" style="background-color: #1a1a1a;">Home</a></li> <!-- button to go back to home page -->
    <?php 
    $server = "localhost"; //Please edit the username and password to what suits your computer.
    $username = "root";
    $password = "";
    $dbname = "Chess";

    $conn = mysqli_connect($server, $username, $password, $dbname); //connects to sql file based on these constraints

    if(isset($_POST['submit'])){ //checks if survey was submitted
      if(!empty($_POST['FavOpening'])){
        $FavOpening = $_POST['FavOpening'];
        $query = "insert into favorite_chess_opening?_(Chess_answers) values('$FavOpening')"; //inserts results of survey into the sql in Chess_answers column
        $run = mysqli_query($conn, $query) or die(mysqli_error()); //runs the query if possible, otherwise yields an error
        if($run){
          $sql = "SELECT * FROM Chess WHERE Chess_answers = '$FavOpening'"; //takes the answer that is equal to the survey input...
          echo "<h2>We will try to add" . $sql . "to this website!</h2>"; //...and then places into here for this sentence
          }
        else{
          echo "<h2>Form not submitted</h2>";
        }
      }
      else{
        echo "<h2>All fields required</h2>"; //if the input bar is empty, this error message will pop up
      }

    }
    ?>
  </body>
</html>
