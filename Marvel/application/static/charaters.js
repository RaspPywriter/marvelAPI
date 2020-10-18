var htmlString = ""
  var api_token = 'ce161d5698b47f739629a98e89765e12'
  var token = '8402777b696d20ea8929494ad7ae817d699ced22'
  var ts = new Date().getTime();
  var hash = CryptoJS.MD5(ts + token + api_token).toString();
  const state = 'http://gateway.marvel.com/v1/public/characters'
  const url = state + '?ts='+ts+'&apikey='+ api_token + '&hash=' + hash
  const Http = new XMLHttpRequest();
  Http.open("GET", url)
  Http.send();
  Http.onreadystatechange = (e) => {
  data = Http.responseText;
  var jsonResponse = JSON.parse(data);
  console.log(jsonResponse);
  //var name = jsonResponse.data.results[0];

  //for (i=0; i<jsonResponse.data.results.length; i++){
  //books.push(jsonResponse.data.results[i], jsonResponse.data.results[i].description, jsonResponse.data.results[i].comics, jsonResponse.data.results[i].stories, jsonResponse.data.results[i].events, jsonResponse.data.results[i].series)
  books.push(jsonResponse);
  //}

 // this just sends the names to routes: saveHero(books);

 //saveHero(jsonResponse)
 saveHero(jsonResponse)
        }

function saveHero(htmlString) {
//send books to database
    const xhttp = new XMLHttpRequest();
    xhttp.open("POST", 'SaveFile', true);
    xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify(htmlString));
    xhttp.onreadystatechange = (e) => {
    console.log(xhttp.responseText)
    }


}