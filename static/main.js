(function () {

  'use strict';

  angular.module('myApp', [])

  .controller('myController', ['$scope', '$log',
    function($scope, $log) {
    $scope.getResults = function() {
      $log.log("test");
    };
  }

  ]);

}());
