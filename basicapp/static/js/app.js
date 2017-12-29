function copyText() {
  var copyText = document.getElementById("copy-input");
  copyText.select();
  document.execCommand("Copy");
  // alert("Copied the text: " + copyText.value);
}
