#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight(function (array, ind) {
    array.push(ind);
    return array;
  }, []);
};
