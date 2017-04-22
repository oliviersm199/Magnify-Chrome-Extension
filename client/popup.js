

function renderStatus(statusText) {
  document.getElementById('status').textContent = statusText;
}

function deleteElementById(id){
  var element = document.getElementById(id);
  var elementParent = element.parentElement;
  elementParent.removeChild(element);
}

function updatePageWithLinks(jsonObject){
  deleteElementById('progressbar');
  for(var i in jsonObject['ny_times']){
    renderLink(jsonObject['ny_times'][i]['headline'],jsonObject['ny_times'][i]['url']);
  }
}


function renderLink(link_text,link_url){
  var a = document.createElement('a');
  var linkText = document.createTextNode(link_text);
  a.appendChild(linkText);
  a.title = link_text;
  a.href = link_url;
  a.className = "collection-item";
  a.onclick = function(){chrome.tabs.create({url:this.href})};
  document.getElementById('status').appendChild(a);
}


document.addEventListener('DOMContentLoaded', function() {
  getCurrentTabHtml(function(results){
    var htmlPage = results;
    request.post("http://127.0.0.1:5000/article",htmlPage,function(httpResponse){
      var jsonObject = JSON.parse(httpResponse.response);
      console.log(jsonObject);
      updatePageWithLinks(jsonObject);
    });
  });
});
