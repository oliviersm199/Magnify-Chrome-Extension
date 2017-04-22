function renderStatus(statusText) {
    document.getElementById('status').textContent = statusText;
}

function deleteElementById(id) {
    var element = document.getElementById(id);
    var elementParent = element.parentElement;
    elementParent.removeChild(element);
}

function updatePageWithLinks(jsonObject) {
    deleteElementById('progressbar');
    for (var i in jsonObject['ny_times']) {
        renderLink(jsonObject['ny_times'][i]['headline'], jsonObject['ny_times'][i]['url']);
    }
}

function updatePageWithError(){
  deleteElementById('progressbar');
  renderStatus('Could not get the content for this page.');
}


function renderImg(parent, src, height, width, alt) {
    var oImg = document.createElement("img");
    oImg.setAttribute('src', src);
    oImg.setAttribute('alt', alt);
    oImg.setAttribute('height', height);
    oImg.setAttribute('width', width);
    parent.appendChild(oImg);
}

function renderLink(link_text, link_url) {
    var a = document.createElement('a');
    var linkText = document.createTextNode(link_text);
    renderImg(a, "img/content-providers/ny_times30.png", 30, 30, "New York Times");
    a.appendChild(linkText);
    a.title = link_text;
    a.href = link_url;
    a.className = "collection-item";
    a.onclick = function() {
        chrome.tabs.create({
            url: this.href
        })
    };
    document.getElementById('status').appendChild(a);
}


document.addEventListener('DOMContentLoaded', function() {
    getCurrentTabHtml(function(results) {
        var htmlPage = results;
        var function_success = function(httpResponse) {
            var jsonObject = JSON.parse(httpResponse.response);
            updatePageWithLinks(jsonObject);
        };
        var function_fail = function(httpResponse){
          updatePageWithError();
        }
        request.post("http://127.0.0.1:5000/article", htmlPage,function_success,function_fail);
    });
});
