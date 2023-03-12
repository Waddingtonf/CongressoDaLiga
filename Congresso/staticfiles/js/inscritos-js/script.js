function changeImage(){

    img = document.getElementById('eye').src;

    if(img == "localhost/img/inscritos/OlhoNotSelected.svg" ){
        img = "localhost/img/inscritos/OlhoSelected.svg";
        document.getElementById('eye').src = "img/inscritos/OlhoSelected.svg"
    }

    else if(img == "img/inscritos/OlhoSelected.svg" ){
        img = "localhost/img/inscritos/OlhoNotSelected.svg"
        document.getElementById('eye').src = "localhost/img/inscritos/OlhoNotSelected.svg"
    }

}

const courses = document.getElementsByClassName('courses')
const information = document.getElementsByClassName('information')
const cronogram = document.getElementsByClassName('cronogram')

var section1 = document.getElementById('courses')
var section2 = document.getElementById('informations')
var section3 = document.getElementById('cronograms')

  // Loop through the buttons and add the active class to the current/clicked button

for(let item of document.querySelectorAll('li')) {
    item.addEventListener('click', event => {
      // Remove active class from all li
      for(let i of document.querySelectorAll('li')) {
        i.classList.remove('active')
      }
      item.classList.add('active')
    })
  }

curso = document.getElementsByClassName('information').disabled = true;
curso = document.getElementsByClassName('cronogram').disabled = true;

