

function renderStatus(statusText) {
  document.getElementById('status').textContent = statusText;
}

function renderLink(ulList,link_text,link_url){
  var li = document.createElement('li')
  li.class = "list-group-item";
  var a = document.createElement('a');
  var linkText = document.createTextNode(link_text);
  a.appendChild(linkText);
  a.title = link_text;
  a.href = link_url;
  li.appendChild(a);
  ulList.appendChild(li);
}


document.addEventListener('DOMContentLoaded', function() {
  getCurrentTabHtml(function(results){
    var htmlPage = results;
    request.post("http://127.0.0.1:5000/article",htmlPage,function(httpResponse){
      var jsonObject = JSON.parse(httpResponse.response)
      console.log(jsonObject);
      var ulList = document.createElement("ul");
      ulList.class = "list-group";
      for(var i in jsonObject['ny_times']){
        renderLink(ulList,jsonObject['ny_times'][i]['headline'],jsonObject['ny_times'][i]['url']);
      }
      document.getElementById('status').appendChild(ulList);
      console.log(httpResponse.response);
    });
  });
});
