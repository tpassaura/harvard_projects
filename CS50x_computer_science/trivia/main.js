const buttons = document.querySelectorAll(".housesNames");
const validationText1 = document.getElementById ("validationText");
const submit = document.querySelector("#submit");
const validationText2 = document.getElementById ("validationText2")


validation_quest_1();
validation_quest_2();




//FUNCTION TO VALIDADE THE AWNSER OF QUESTION 1
function validation_quest_1 () {
    //TO KNOW WHEN A BUTTON IS PRESSED
    buttons.forEach((element) => {
        element.addEventListener("click", (evento) => {
            //TO GET THE INFORMATION OF THE PRESSED BUTTON
            button = event.target;
            //TO RESET THE BUTTONS COLORS
            set_default_buttons_colors();
            //TO CHECK IF THE AWNSER IS THE RIGHT ONE
            if(button.textContent == "Gryffindor") {
                button.style.backgroundColor = "green";
                validationText1.textContent = "Correct";
            }
            else {
                button.style.backgroundColor = "red";
                validationText1.textContent = "Incorrect";
            }
        })
    })
}

//FUNCTION TO SET THE BUTTONS COLORS TO DEFAULT
function set_default_buttons_colors () {
    buttons.forEach(element =>{
        element.style.backgroundColor = "#d9edff";
    })
}

//FUNCTION TO VALIDADE THE AWNSER OF QUESTION 2
function validation_quest_2 () {
    //TO KNOW WHEN THE CHECK AWNSER BUTTON IS PRESSED
    submit.addEventListener("click", (evento) => {
        //TO GET THE INFORMATION OF THE IMPUT FIELD
        const awnser = document.querySelector("#awnser");
        //TO CONVERT THE AWNSER TO UPPER CASE
        const awnserValue = awnser.value.toUpperCase();
        //TO CHECK IF THE AWNSER IS THE RIGHT ONE
        if (awnserValue != "" && awnserValue != "SEEKER"){
            awnser.style.backgroundColor = "red";
            validationText2.textContent = "Incorrect";
        }
        else if (awnserValue == "SEEKER")  {
            awnser.style.backgroundColor = "green";
            validationText2.textContent = "Correct";
        }
        else if (awnserValue == "")
        {
            awnser.style.backgroundColor = "#ffffff";
            validationText2.textContent = "";
        }
    })
}