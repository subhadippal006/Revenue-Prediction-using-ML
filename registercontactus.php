<?php
include"./connectxyz.php";
if($_SERVER["REQUEST_METHOD"]=="POST")
{
$name=$_POST[name];
$phnumber=$_POST[phnumber];	
$email=$_POST[email];
$subject=$_POST[subject];

$query="INSERT INTO contactus(`name`,`phnumber`,`email`,`subject`)VALUES('$name','$phnumber','$email','$subject')";
$query_exec=mysqli_query($connection,$query);
echo"your data is stored";
}
else
	echo"your data not stored";
?>