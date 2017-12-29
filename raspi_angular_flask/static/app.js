(function () {
    'use strict';

	angular.module('RaspiSmartHouse', [])
	.config(config);

	config.$inject = ['$routeProvider', '$locationProvider'];
	function config($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/landing.html',
			controller: 'funcController',
			controllerAs: 'vm'
		})
		.when('/about', {
			templateUrl: 'static/partials/about.html',
			controller:  'funcController'
		})
		.when('/func', {
			templateUrl: 'static/partials/func.html',
			controller:  'funcController'
		})
		.when('/getdata', {
			templateUrl: 'static/partials/event-list.html',
			controller:  'eventController',
		})
		.otherwise({
			redirectTo: '/'
		})
		;

		$locationProvider.html5Mode(true);
	}

})();