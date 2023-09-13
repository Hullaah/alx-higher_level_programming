#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((x, i, a) => a[a.length - i - 1]);
};
