const showText = document.querySelector('show-text');
const text = document.getElementsByClassName('joining')
var a;

showText.addEventListener("click", function(){
  if(a==1){
    this.classList.toggle("fa-eye-slash");
    text.style.display = 'none'
    return a=0
  }else{
    this.classList.toggle("fa-eye");
    text.style.display = 'flex'
    return a=1
  }
})

