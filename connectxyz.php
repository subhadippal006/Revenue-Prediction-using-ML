<?php
$host="127.0.0.1";
$user="root";
$password="";
$database="productdb";
$connection=mysqli_connect($host,$user,$password,$database);
if(!$connection)
{die("connection fails".mysqli_connect_error());
}
else
echo "connection successful";
?>