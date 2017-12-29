(function () {
    'use strict';

    angular.module('RaspiSmartHouse').controller('funcController', funcController);

    funcController.$inject = ['$http', '$scope'];
    function funcController($http, $scope) {

        // var prefix="http://raspi:5000";
		var prefix="http://raspi:5000";
     	var date = "";

		$scope.temp = "";
		$scope.lcdtext1 = "";
		$scope.lcdtext2 = "";
		$scope.lcdtext3 = "";
		$scope.lcdtext4 = "";
		$scope.events = [];

		$scope.ledOn = ledOn;
		$scope.ledOff = ledOff;
		$scope.relayOn = relayOn;
		$scope.relayOff = relayOff;
		$scope.consoleGo = consoleGo;
		$scope.getTemp = getTemp;
		$scope.sendlcdmsg = sendlcdmsg;

        initController();

        function initController() {
        }

        function ledOn() {
		console.log("ledOn");
			return $http.get(prefix+'/ledon');
		}

        function ledOff() {
    	console.log("ledOff");
			return $http.get(prefix+'/ledoff');
		}

        function relayOn() {
    	console.log("relayOn");
			return $http.get(prefix+'/relayon');
		}

        function relayOff() {
    	console.log("relayOff");
			return $http.get(prefix+'/relayoff');
		}

		function consoleGo() {
    	console.log("Console app launched");
			return $http.get(prefix+'/consolego')
				.then(function(response) {
                    $scope.date = response.data;
                    console.log(date);
                }, function(response) {
					console.log("Error!")
                });
		}

		function getTemp() {
    	console.log("DS18B20 test");
			return $http.get(prefix+'/gettemp')
				.then(function(response) {
                    $scope.temp = response.data;
                    console.log(date);
                }, function(response) {
					console.log("Error!")
                });
		}

		function sendlcdmsg() {
    	console.log("LCD test");
    	var j={"lcd1":$scope.lcdtext1, "lcd2":$scope.lcdtext2, "lcd3":$scope.lcdtext3, "lcd4":$scope.lcdtext4};

    	$http({
				method: 'POST',
				url: prefix+'/sendmsg',
				data: JSON.stringify(j)
			}).then(function(response) {
					console.log("Ok!")
                }, function(response) {
					console.log("Error!")
                });
		}
    }

})();

