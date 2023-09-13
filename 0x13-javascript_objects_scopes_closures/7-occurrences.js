#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((x, y) => y === searchElement ? ++x : x, 0);
};
