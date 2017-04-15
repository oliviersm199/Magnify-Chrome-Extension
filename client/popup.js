

function renderStatus(statusText) {
  document.getElementById('status').textContent = statusText;
}


document.addEventListener('DOMContentLoaded', function() {
  getCurrentTabHtml(function(results){
    var htmlPage = results;
    request.post("http://127.0.0.1:5000",htmlPage,function(httpResponse){
      
    });
  });
});
