(function () {
    'use strict';

    angular.module('RaspiSmartHouse').controller('eventController', eventController);

    eventController.$inject = ['$http', '$scope'];
    function eventController($http, $scope) {

        // var prefix="http://raspi:5000";
		var prefix="http://raspi:5000";

		$scope.events = [];

		$scope.getEvents = getEvents;

        initController();

        function initController() {
        	getEvents()
        }

		function getEvents() {
        	console.log("Get events test");
			return $http.get(prefix+'/getevents')
				.then(function(response) {
                    $scope.events = response.data;
                }, function(response) {
					console.log("Error!")
                });
		}
    }

})();

