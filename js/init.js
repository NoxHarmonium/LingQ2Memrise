require.config({
    "baseUrl": "js/lib",
    "paths": {
        "app": "../app",
        "jquery": "http://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min",
        "bootstrap": "boostrap/boostrap.min",
        "knockout": "knockout-2.3.0",
        "knockout-validation": "knockout.validation"


    },
    map: {
        // '*' means all modules will get 'jquery-private'
        // for their 'jquery' dependency.
        '*': { 'jquery': 'jquery-private' },

        // 'jquery-private' wants the real jQuery module
        // though. If this line was not here, there would
        // be an unresolvable cyclic dependency.
        'jquery-private': { 'jquery': 'jquery' }
    }
});

// Load the main app module to start the app
requirejs(["app/main"]);

require(['knockout', 'knockout-validation', 'app/viewModel', 'domReady'], function (ko, koval, ViewModelClass) {
    ko.applyBindings(new ViewModelClass());
});