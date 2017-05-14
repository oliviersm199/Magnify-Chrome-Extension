
var supported_sites = ['ny_times', 'guardian','hackernews'];

// Source: https://www.frankmitchell.org/2015/01/fisher-yates/
function shuffle(array) {
  var i = 0,
    j = 0,
    temp = null

  for (i = array.length - 1; i > 0; i -= 1) {
    j = Math.floor(Math.random() * (i + 1))
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
  }
}


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

  // get list of articles from all supported sites on the client
  var list_of_articles = []
  for (var i in supported_sites) {
    if (supported_sites[i] in jsonObject) {
      var articles_from_site = jsonObject[supported_sites[i]];
      for (var j in articles_from_site) {
        articles_from_site[j]['site'] = supported_sites[i];
        list_of_articles.push(articles_from_site[j])
      }
    }
  }

  // we have our list of articles, now put them in a random order
  shuffle(list_of_articles)

  for (var i in list_of_articles) {
    var link_img = list_of_articles[i]['site'] + '.png';
    renderLink(list_of_articles[i]['headline'], list_of_articles[i]['url'],link_img,list_of_articles['site']);
  }
}

function updatePageWithError() {
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

function renderLink(link_text, link_url,link_img,link_name) {
  var a = document.createElement('a');
  var linkText = document.createTextNode(link_text);
  renderImg(a, "img/content-providers/" + link_img, 30, 30,link_name);
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

function createChart(user_keywords){
  var keys = [];
  var values = [];
  for(var i in user_keywords){
    keys.push(user_keywords[i]['word']);
    values.push(user_keywords[i]['count']);
  }
  createBarChart(keys,values);
}


document.addEventListener('DOMContentLoaded', function() {
  getCurrentTabHtml(function(results) {
    var htmlPage = results;

    // if our http request suceeds, let's do this.
    var function_success = function(httpResponse) {
      var jsonObject = JSON.parse(httpResponse.response);
      console.log(jsonObject)

      updatePageWithLinks(jsonObject);

      var user_keywords = jsonObject['user_keywords'];
      createChart(user_keywords);
    };

    // if it fails, let's do that.
    var function_fail = function(httpResponse) {
      updatePageWithError();
    }

    //get the user id
    var user_id = user.useUserId(function(user_id){
      var sentToServer = {"page":htmlPage,"user_id":user_id};

      // make a post to the page
      request.post("http://127.0.0.1:5000/article", sentToServer, function_success, function_fail);
    });
  });
});
