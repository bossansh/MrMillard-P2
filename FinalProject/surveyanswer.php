<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="phpcss.css"> <!-- external style -->
    <style>
      html {
        background-image: url('IMAGES/leader-success-chess-pieces.jpeg');
        background-size: cover; /* adds background image to the page */
        min-height: 100%;
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
      }
    </style>
  </head>
  <body>
    <a href="index.html" style="background-color: #1a1a1a;">Home</a><!-- button to go back to home page -->
    <?php 

    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
      
    $server = "localhost"; 
    $username = "root";
    $password = "";
    $dbname = "Chess";

    $conn = mysqli_connect($server, $username, $password, $dbname); //connects to sql file based on these constraints
    

    if(isset($_POST['submit'])){ //checks if survey was submitted
      if(!empty($_POST['FavOpening'] && !empty($_POST['name']))){
        $FavOpening = $_POST['FavOpening'];
        $name = $_POST['name'];
        $sql = "SELECT count(*) as cnt FROM `favorite chess opening?` WHERE Chess_answers = '$FavOpening'"; //takes the number of values in database that is equal to $FavOpening
        $result = mysqli_query($conn, $sql);
        while ($row = $result->fetch_assoc()) {
                $column = $row["cnt"];
        }
        if($column == 0) //if there are no values that are equal to users input then runs this code
        {
            $query = "insert into `favorite chess opening?` (Name, Chess_answers) values('$name', '$FavOpening')"; //inserts results of survey into the sql in Chess_answers column
            $run = mysqli_query($conn, $query) or die(mysqli_error()); //runs the query if possible, otherwise yields an error
            if($run)
            {
                echo '<span style="color:#FFF;text-align:center;"><h2>We will try to add ' . $FavOpening . ' to our website.</h2></span>'; //message for user
            }
            else
            {
                echo "<h2>Unable to enter value.</h2>";
            }
        }
       else{
            echo '<span style="color:#FFF;text-align:center;"><h2>We are already working on adding ' . $FavOpening . ' to our website.</h2></span>'; //if the value is in database, runs this code
       }
      
        
          
        
      }
      else{
        echo '<span style="color:#FFF;text-align:center;"><h2>All fields required</h2></span>'; //if the input bar is empty, this error message will pop up
      }

    }
      
    ?>
  </body>
</html>
