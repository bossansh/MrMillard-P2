<html>
<head>
</head>

<body>
<h1>Chess Page</h1>



<?php
$host = "localhost";
$username = "root";
$user_pass = "";
$database_in_use = "test";

$mysqli = new mysqli($host, $username, $user_pass, $database_in_use);

if ($mysqli->connect_errno) {
	echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
echo $mysqli->host_info . "\n";

$sql = "SELECT ChessID, Chess_answers, FROM favorite chess opening?";
$result = $mysqli->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "Chess id: " . $row["ChessID"]. " - Chess Answer: " . $row["Chess_answers"]. "<br>";
  }
} else {
  echo "0 results";
}
$mysqli->close();
	
?>

</body>

</html>
