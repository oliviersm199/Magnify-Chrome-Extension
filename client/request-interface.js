// makes a simple http request
var request = {
    get: function(url, callback) {
        var req = new XMLHttpRequest();
        req.open("GET", url);
        req.onreadystatechange = function() {
            if (req.readyState == 4) {
                if (req.status == 200) {
                    callback(req);
                }
            }
        };
        req.send();
    },

    post: function(url, content, callback_success,callback_failure) {
        var req = new XMLHttpRequest();
        req.open("POST", url);
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        req.onreadystatechange = function() {
            if (req.readyState == 4) {
                if (req.status == 200) {
                    callback_success(req);
                }else{
                  callback_failure(req);
                }
            }
        }
        req.send(content);
    }
}
