// Copied and Pasted from the following:
// http://stackoverflow.com/questions/23822170/getting-unique-clientid-from-chrome-extension

//global user object
var user = {
  // generates a random id for each user.
  getRandomToken : function(){
    // E.g. 8 * 32 = 256 bits token
    var randomPool = new Uint8Array(32);
    crypto.getRandomValues(randomPool);
    var hex = '';
    for (var i = 0; i < randomPool.length; ++i) {
        hex += randomPool[i].toString(16);
    }
    return hex;
  },
  // will execute a function callback which has the user id as input.
  // Gets the user id from storage.sync so it should be available if the user
  // logs into a different chrome browser.
  useUserId : function(callback){
    chrome.storage.sync.get('userid', function(items) {
        var userid = items.userid;
        if (userid) {
            useToken(userid);
        } else {
            userid = getRandomToken();
            chrome.storage.sync.set({userid: userid}, function() {
                useToken(userid);
            });
        }
        function useToken(userid) {
          callback(userid)
        }
    });
  }
}
