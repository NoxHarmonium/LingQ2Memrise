define(['jquery'], function ($) {
    return function APIClass(key) {
        this.key = key;
        this.URL_GET_LANG = "https://www.lingq.com/api/languages/";

        this._apiCall = function(url, callback)
        {
            var self = this;
            $.ajax({
                type: "GET",
                url: url,
                contentType: "application/json",
                beforeSend: function(jqXHR, settings){
                    jqXHR.setRequestHeader("Authorization", "Token " + self.key);
                },
                success: callback
            });


        };

        this.GetLanguages = function(callback)
        {
            var self = this;
            self._apiCall(self.URL_GET_LANG, callback);


        };


    }
});