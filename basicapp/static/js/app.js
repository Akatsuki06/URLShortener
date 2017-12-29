function copyText() {
  var copyText = document.getElementById("copy-input");
  copyText.select();
  document.execCommand("Copy");
  // var tooltip=document.getElementById("copy-input");
  // $(".hover-tooltip a").tooltip('show');
  // alert("Copied the text: " + copyText.value);
}
