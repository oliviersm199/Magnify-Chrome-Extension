// returns the tab information of the current tab.
function getCurrentTab(callback) {
    // Query filter to be passed to chrome.tabs.query - see
    // https://developer.chrome.com/extensions/tabs#method-query
    var queryInfo = {
        active: true,
        currentWindow: true
    };

    chrome.tabs.query(queryInfo, function(tabs) {
        var tab = tabs[0];
        return tab;
    });
}

function getCurrentTabHtml(callback) {
    function modifyDOM() {
        return document.body.innerHTML;
    }
    try {
        //We have permission to access the activeTab, so we can call chrome.tabs.executeScript:
        chrome.tabs.executeScript({
            code: '(' + modifyDOM + ')();' //argument here is a string but function.toString() returns function's code
        }, (results) => {
            callback(results);
        });
    } catch (e) {
        throw "Woops this site isn't valid";
    }
}

function newPage(page) {
    chrome.tabs.create({
        url: chrome.extension.getURL(page)
    });
}
