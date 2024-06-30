#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const count = (list.filter(item => item === searchElement)).length;
  return count;
};
