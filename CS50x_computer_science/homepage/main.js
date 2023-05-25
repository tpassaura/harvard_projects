sendButton = document.getElementsByClassName("btn btn-primary")
fields = document.querySelectorAll(".contact")


sendButton[0].addEventListener("click", (evento)=>{
    fields.forEach( (elemento) =>{
    elemento.value = "";
    })
})