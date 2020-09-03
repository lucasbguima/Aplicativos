<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rifa</title>
    <link rel="stylesheet" type="text/css" href="rifastyle.css"/>
</head>
<body>
  <div id="formrifa">
    <form action="./postrifa.php" method="post">
    <input type="number" placeholder="Número de Rifas" id="inputn" name="quantidade">
    <button type="submit" id="inputc">Criar Rifas</button>
    </form>
  </div>
  <div id="gridrifa">
  <?php
  $qtd = $_POST["quantidade"];
  include 'classerifa.php';
  ?>
  </div>
</body>

</html>
 
