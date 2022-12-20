<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    
    <?php 
    $server = "localhost"; //Please edit the username and password to what suits your computer.
    $username = "root";
    $password = "";
    $dbname = "Chess";

    $conn = mysqli_connect($server, $username, $password, $dbname);

    if(isset($_POST['submit'])){
      if(!empty($_POST['FavOpening'])){
        $FavOpening = $_POST['FavOpening'];
        $query = "insert into favorite_chess_opening?_(Chess_answers) values('$FavOpening')";
        $run = mysqli_query($conn, $query) or die(mysqli_error());
        if($run){
          echo "<h2>Hi</h2>";
          $sql = "SELECT * FROM Chess WHERE Chess_answers = '$FavOpening'";
          echo "<h2>We will try to add" . $sql . "to this website!</h2>";
          }
        else{
          echo "<h2>Form not submitted</h2>";
        }
      }
      else{
        echo "<h2>All fields required</h2>";
      }

    }
  ?>
  </body>
</html>
