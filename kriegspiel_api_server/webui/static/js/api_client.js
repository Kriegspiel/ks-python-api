"use strict";

var api_client = {
  post: function(url, data, callback) {
    webix.ajax().post(url, data, function(text, data) {
      var response = data.json(),
          data = {},
          errors = {};

    })
  }
};
