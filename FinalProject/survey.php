<!DOCTYPE html>
<html> 
  <head>
    <title>Survey</title>
    <link rel="stylesheet" href="phpcss.css"> <!-- external style -->
    <style>
      html {
        background-image: url('IMAGES/kingdown.jpeg'); /*background image*/
        background-size: cover;      
        min-height: 100%;
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
      }
    table, th, td {
        border: 1px solid black;
        }
    </style>
  </head>
  <body>
    
    <?php 
        ini_set('display_errors', 1);
        ini_set('display_startup_errors', 1);
        error_reporting(E_ALL);

        $server = "localhost"; 
        $username = "root";
        $password = "";
        $dbname = "Chess";

        $conn = mysqli_connect($server, $username, $password, $dbname); //connects to sql file based on these constraints
        $sql = "SELECT * FROM `favorite chess opening?`"; //takes the answer that is equal to the survey input...
        $result = mysqli_query($conn, $sql);
        $list = 1;
        ?>
        <form>
            <h2>Other users' favorite openings</h2>
            <table id="myTable"> <!--makes a table with two rows and only one column-->
              <tr>
                <th>Name</th>
                <th>Their answers</th>
              </tr>
            </table>
            <script>
                function myFunction(column1, column2) {  
                  var table = document.getElementById("myTable");
                  var row = table.insertRow(1); //function that takes in 2 parameters, creates two new boxes, one in each row, and then adds the parameters' values into those boxes.
                  var cell1 = row.insertCell(0);
                  var cell2 = row.insertCell(1);
                  cell1.innerHTML = column1;
                  cell2.innerHTML = column2;                
                }
            </script>
            <?php
    
            while ($row = $result->fetch_assoc()) { //fetches values from database one at a time until the table has been fully fetched
                $column1 = $row["Name"]; //stores the name
                $column2 = $row["Chess_answers"]; //stores chess answers
                ?>
                <script>
                    myFunction(<?php echo(json_encode($column1)) ?>, <?php echo(json_encode($column2)) ?>); //adds chess answers to 2nd column of table and names to first column
                </script>
            <?php
            }
        ?></form>
    <form action="surveyanswer.php" method="post"> <!-- creates a form with inputs of name and favorite opening, and sends results to surveyanswer.php when submitted.-->
        <label>Your name</label>
       <input type="text" name="name" placeholder="name"><br>
       <label>Favorite Opening</label>
       <input type="text" name="FavOpening" placeholder="Opening name"><br>
       <button type="submit" name = "submit">Submit</button>
    </form>
    <a href="index.html" style="background-color: #1a1a1a;">Back</a> <!-- button back to home page-->
  </body>
</html>
