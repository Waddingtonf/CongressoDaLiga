document.getElementById("quadro").addEventListener('click', (event) => {
    const target = event.target;
    if (target.matches("img")) {
      target.src = target.dataset.over;
    }
 });