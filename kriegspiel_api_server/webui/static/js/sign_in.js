"use strict";

webix.proxy.Api = {
  $proxy:true,
  load: function(view, callback) {
    console.log(this.source, view);
    webix.ajax(this.source, callback, view);
  }
};


function sign_in_error_callback(text, data) {
  var json = data.json();
  webix.message({
    type: 'error',
    text: json.error.code
  });
}


function sign_in_success_callback(text, data) {
  var json = data.json();
  var token = json.data.token;
  webix.message({
    text: token
  });
  webix.storage.local.put('auth_token', token);
  window.location.href = "/static/app.html";
}