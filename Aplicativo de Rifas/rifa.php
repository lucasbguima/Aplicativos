<!DOCTYPE html>
<html lang="en">
<style>
#but{
  padding: 5px;

}

#but:hover {
  background-color: yellow;
}

#gridrifa{
  display: grid;
  grid-template-columns: repeat(20, 1fr [col-start]);
  grid-template-rows: repeat(50, 30px [col-start]);
  
}
#numero{
  height: 20px;
  margin: 20px;
}
</style>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rifa</title>
    <link rel="stylesheet" type="text/css" href="rifastyle.css" media="screen" />
</head>
<body>
  <div id="formrifa">
    <form>
    <input type="number" placeholder="Número de Rifas" id="numero">
    <button type="submit">Criar Rifas</button>
    </form>
  </div>
  <div id="gridrifa">
  <?php
  include 'classerifa.php';
  ?>
  </>
</body>

</html>