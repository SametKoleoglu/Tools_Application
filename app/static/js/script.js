document.getElementById("pingForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Sayfanın yenilenmesini önler

  // Div'i görünür hale getir
  document.getElementById("result").style.display = "block";
});
