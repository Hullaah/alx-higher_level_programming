#!/usr/bin/node
exports.callMeMoby = function (n, f) {
  for (let i = 0; i < n; i++) {
    f();
  }
};
