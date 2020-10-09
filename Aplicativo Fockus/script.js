// Função de Criar Tarefas
function criarTarefa(){
  
  //Criar o Modelo de tarefa a Ser Gerada
  var newtask = document.createElement("div");
  newtask.setAttribute("id", "tarefa");
  var newact = document.createElement("div");
  newact.setAttribute("id", "act");
  var newtext = document.createElement("p");
  newtext.setAttribute("id", "text");
  var newcard = document.createElement("div");
  newcard.setAttribute("id", "card");
  var newverde = document.createElement("div");
  newverde.setAttribute("id", "verde");
  var newazul = document.createElement("div");
  newazul.setAttribute("id", "azul");
  var newcontent = document.createTextNode(nomeTarefa());

  // Cria o Modelo de Act a Ser Gerado
  var newplay = document.createElement("button");
  newplay.setAttribute("id", "play");
  var newstop = document.createElement("button");
  newstop.setAttribute("id", "stop");
  var newedit = document.createElement("button");
  newedit.setAttribute("id", "edit");
  var newclear = document.createElement("button");
  newclear.setAttribute("id", "clear");
  var newtime = document.createElement("input");
  newtime.setAttribute("type", "time");
  newtime.setAttribute("id", "time");
  newtime.setAttribute("step", "1");
  newtime.setAttribute("oninput", "getTime()");

  var playcontent = document.createTextNode("Play");  
  var stopcontent = document.createTextNode("Stop");
  var editcontent = document.createTextNode("Edit");
  var clearcontent = document.createTextNode("Clear");

  //Insere os Nós
  newtask.appendChild(newact);
  newact.appendChild(newtext);

  newact.appendChild(newplay);
  newact.appendChild(newstop);
  newact.appendChild(newedit);
  newact.appendChild(newclear);
  newact.appendChild(newtime);

  newplay.appendChild(playcontent);
  newstop.appendChild(stopcontent);
  newedit.appendChild(editcontent);
  newclear.appendChild(clearcontent);

  newtext.appendChild(newcontent);
  newtask.appendChild(newcard);
  newcard.appendChild(newverde);
  newcard.appendChild(newazul);

  // Adiciona o Elemendo Gerado no HTML atual
  var oldtask = document.getElementById("tarefa"); 
  document.body.insertBefore(newtask, oldtask);
}

// Função de Pegar Tempo do Usuário
function getTime(){

  var tempo = document.activeElement.value;

  var user_h = tempo.slice(0,2);
  var user_m = tempo.slice(3,5);
  var user_s = tempo.slice(6,8);
  var user_tempo = user_h*3600 + user_m*60 + user_s*1;
  
  temporeal = new Date();
  real_h = temporeal.getHours();
  real_m = temporeal.getMinutes();
  real_s = temporeal.getSeconds();
  var real_tempo = real_h*3600 + real_m*60 + real_s*1;

  // Parte de Atualizar Barra
    var barraverde = document.activeElement.parentElement.nextElementSibling.firstElementChild;
    var barraazul = document.activeElement.parentElement.nextElementSibling.firstElementChild.nextElementSibling;

    if (user_tempo>real_tempo){
    barraverde.style.width = ((real_tempo*200)/user_tempo)+"%";
    barraazul.style.width = (200 - ((real_tempo*200)/user_tempo))+"%";
    /* alert("Você deve terminar sua tarefa até " + tempo); */
    }
    else if(user_tempo<real_tempo){
    barraverde.style.width = ((real_tempo*200)/(user_tempo+86400))+"%";
    barraazul.style.width = (200 - ((real_tempo*200)/(user_tempo+86400)))+"%";
    /* alert("Você deixou sua tarefa pra amanhã!"); */
    } 
    else{
    barraverde.style.width = 200+"%";
    barraazul.style.width = 0+"%";
    /* alert("O tempo de conclusão da sua tarefa acabou!"); */
    }
    
}

// Função de Nomear Tarefas
function nomeTarefa(){
        var x = document.getElementById("form");
        var texto = "";
        var i;
        for (i = 0; i < x.length ;i++) {
          texto += x.elements[i].value;
        }
        return texto;
} 
// Criando Funções de Interação com Tarefas

// Função de Play Tarefa
function playTarefa(){

}
// Função de Stop Tarefa
function stopTarefa(){

}
// Função de Excluir Tarefa
function clearTarefa(){
  var lixo = document.activeElement.parentElement.parentElement;
  lixo.remove();
}

// Função de Editar Tarefa
function editTarefa(){

}

// ############## Refatorando Eventos - Event Listener ###############

// Criar Tarefa 
document.querySelector("#add").addEventListener('click', function(){
  criarTarefa();
    // Clear Tarefa Criada
    document.querySelector("#clear").addEventListener('click', function(){
    clearTarefa();
    })
    // Time Tarefa Criada
    document.querySelector("#time").addEventListener('input', function(){
    getTime();
    })
})

// Clear Tarefa Inicial
document.querySelector("#clear").addEventListener('click', function(){
   clearTarefa();
})

// Get Time Inicial
document.querySelector("#time").addEventListener('input', function(){
  getTime();
})

// Enter Input Geral
document.querySelector("#myInput").addEventListener('keyup', function(event){
  if (event.keyCode === 13) {
    event.preventDefault();
    document.querySelector("#add").click();
   }
})

document.querySelector("#form").addEventListener('submit', function(event){
  event.preventDefault();
  return false;
})

// Exemplo de cards com cores aleatorias

/* setInterval(
  function () {
    var randomColor = Math.floor(Math.random()*16777215).toString(16);
    
    document.querySelectorAll("#tarefa").forEach(element => {
      document.querySelector("#tarefa").style.backgroundColor = "#"+randomColor;
    });
    
  },1000); */

