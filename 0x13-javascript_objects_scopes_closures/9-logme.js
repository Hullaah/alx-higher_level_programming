#!/usr/bin/node
exports.logMe = (function () {
  let counter = 0;
  return function (item) {
    console.log(counter++ + ':', item);
  };
}());
