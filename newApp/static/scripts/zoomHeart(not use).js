const catButton = document.querySelector(".btn-cat");

const zoomIn = () => {
  console.log();
  catButton.childNodes[1].classList.add("animate-like");
  catButton.childNodes[2].textContent = " 좋다냥~(good Nya~)";
}

const reset = () => {
  if (!catButton.childNodes[1].classList.contains("animate-like"))
    return
  catButton.childNodes[1].classList.remove("animate-like")
  catButton.childNodes[2].textContent = " 눌러(Push)!"

}

catButton.addEventListener("click", zoomIn);
setInterval(reset, 5000); 