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
      echo "form submission successful";
      }
    else{
      echo "Form not submitted";
    }
  }
  else{
    echo "All fields required";
  }
  
}
?>
