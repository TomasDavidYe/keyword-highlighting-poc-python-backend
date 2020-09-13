function nativeClick(){
  alert('Clicked vanilla javascript function!')
}

function nativeHttpCall(){
  const Http = new XMLHttpRequest();
  const url='http://127.0.0.1:5000/';
  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange = (e) => {
    console.log(Http.responseText)
  }
}


