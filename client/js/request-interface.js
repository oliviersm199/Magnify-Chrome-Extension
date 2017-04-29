// abstracts away requests for get and post.
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

        // organize into this structure: param1=value1&param2=value2.....
        var contentSend = "";
        for (var property in content) {
          if (content.hasOwnProperty(property)) {
            contentSend += property.toString() + "=" + encodeURIComponent(content[property]);
            contentSend += "&"
          }
        }

        //remove the extra & at the end.
        contentSend = contentSend.substring(0,contentSend.length-1);

        req.send(contentSend);
    }
}
