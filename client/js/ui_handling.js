// This file adds event listeners for different user actions in the chrome extension.

document.addEventListener('DOMContentLoaded', function() {
  //x button close page 
  document.getElementById("close-page").addEventListener('click', function() {
    window.close()
  });
  //settings button
  document.getElementById("settings-page").addEventListener('click', function() {
    chrome.tabs.create({
      url: "settings.html"
    })
  });
});
