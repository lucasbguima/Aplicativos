<!DOCTYPE html>
<html lang="en">
<style>
* {
  padding: 0;
  margin: 0;
  border: 0;
  outline: none;

}

/* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type=number] {
  -moz-appearance: textfield;
}

input:focus, textarea:focus, select:focus{
        outline: none;
    }

#but{
  padding: 5px;
}

#but:hover {
  background-color: rgb(135,206,250);
  cursor: pointer;
}

#gridrifa{
  display: grid;
  grid-template-columns: repeat(20, 1fr [col-start]);
  grid-template-rows: repeat(50, 30px [col-start]);
  
}
#inputn{
  padding: 20px;
  margin: 20px;
  border: 1px solid;
  font-size: 20px;
}

#inputc{
  font-size: 20px;
  padding: 20px;
  border-radius: 10px;
  background-color: rgb(135,206,250);

}
#inputc:hover{
  background-color: rgb(0,191,255);

}
</style>
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

  </div>
</body>

</html>