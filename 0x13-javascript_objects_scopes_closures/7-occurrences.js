#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, ind) => ind === searchElement ? count + 1 : count, 0);
};
