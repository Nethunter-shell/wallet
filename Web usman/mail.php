<?php
//get data from form  
$name = $_POST['name'];
$message = $_POST['message'];

$to = "michelleannsmith9@gmail.com";
$subject = "Mail From website";
$txt ="name = ". $name . "\r\n  message = " . $message;
$headers = "From: noreply@connectus.website";
if($email!=NULL){
    mail($to,$subject,$txt,$headers);
}
//redirect
header("Location:finish.html");
?>