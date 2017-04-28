// event listener for closing the page

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("close-page").addEventListener('click', function() {
        window.close()
    });
    document.getElementById("settings-page").addEventListener('click', function() {
        chrome.tabs.create({
            url: "settings.html"
        })
    });
});
