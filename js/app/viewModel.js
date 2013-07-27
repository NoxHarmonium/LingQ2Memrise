// Main viewmodel class
define(['knockout', 'knockout-validation', 'jquery', 'app/api'], function (ko, koval, $, APIClass) {
    return function ViewModelClass() {
        this.api = null;

        this.lingQAPIKey = ko.observable("")
            .extend({
                throttle: 500,
                required: true,
                pattern: {
                    message: 'You need to enter a valid LingQ API key.',
                    params: '[a-z0-9]{40}'
                },

                maxLength: 40,
                minLength: 40

            });

        this.loading_Languages = ko.observable(false);

        this.handleLoadLanguages = function(data)
        {
            this.loading_Languages(true);
            var languages = [];
            for (var i = 0; i < data.length; i++)
            {
                languages.push(data.title);

            }
            this.languages(languages);

        };


        this.lingQAPIKey.subscribe(function (value) {
            if (typeof this.lingQAPIKey.isValid !== 'undefined' && this.lingQAPIKey.isValid() && !this.loading_Languages())  {
                this.loading_Languages(true);
                this.api = new APIClass(this.lingQAPIKey());
                this.api.GetLanguages($.proxy(this.handleLoadLanguages,this));

            }


        }, this);

        this.lingQAPIKeyClass = ko.computed(function () {
                return "control-group info";


            }
            , this);
        this.selectedLanguage = ko.observable("");
        this.lingQAPIKeyMessage = ko.observable("Info message");
        this.languages = ko.observableArray([]);
        this.languagesEnabled = ko.computed(function () {
            return (this.languages != null &&
                typeof this.languages === "array" &&
                this.languages.length > 0);
        }, this);


    };
});