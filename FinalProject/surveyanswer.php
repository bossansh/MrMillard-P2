<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="phpcss.css"> <!-- external style -->
    html {
        background-image: url('IMAGES/linedchess.webp');
        background-size: cover;
        min-height: 100%;
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
      }
  </head>
  <body>
    <?php 
    $server = "localhost";
    $username = "root";
    $password = "";
    $dbname = "Chess";

    $conn = mysqli_connect($server, $username, $password, $dbname);

    if(isset($_POST['submit'])){
      if(!empty($_POST['FavOpening'])){
        $FavOpening = $_POST['$FavOpening'];
        $query = "insert into favorite chess opening?(Chess_answers) values('$FavOpening')";
        $run = mysqli_query($conn, $query) or die(mysqli_error());
        if($run){
          echo "<h2>We will try to add" . $FavOpening . "to this website!</h2>";
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

  
