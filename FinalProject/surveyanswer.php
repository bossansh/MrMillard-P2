<?php 
session_start(); 
include "db_connection.php";

if (isset($_POST['FavOpening'])) {

	function validate($data){
       $data = trim($data);
	   $data = stripslashes($data);
	   $data = htmlspecialchars($data);
	   return $data;
	}

	$FavOpening = validate($_POST['FavOpening']);

	if (empty($FavOpening)) {
		header("Location: survey.php?error=Please type a valid opening.");
	    exit();
	}else{
		$sql = "SELECT * FROM users WHERE user_name='$uname' AND password='$pass'";

		$result = mysqli_query($conn, $sql);

		
	}
	
}else{
	header("Location: survey.php");
	exit();
}
