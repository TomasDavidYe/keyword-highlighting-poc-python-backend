function nativeClick(){
  alert('Clicked vanilla javascript function!')
}

function nativeHttpCall(){
  let content = document.getElementById('content-before').innerHTML;


  const Http = new XMLHttpRequest();
  const url=`http://127.0.0.1:5000/get-keywords-for-text?body=${content}`;
  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange = (e) => {
    let keywords = JSON.parse(Http.responseText);
    console.log('Keywords = ')
    console.log(keywords)
    document.getElementById('content-after').innerHTML = transformContent(content, keywords);
  }
}


function transformContent(content, keywords){
  let temp = content
  Object.keys(keywords).forEach(key => {
    temp = temp.replace(key, wrapKeywordWithLink(key, keywords[key]['link']))
  })
  return temp
}


function wrapKeywordWithLink(keyword, link){
  return `<span style="font-weight: bold"> <a href="${link}" target="_blank"> ${keyword} </a> </span>`
}


