// consider one strings length will ALWAYS be bigger or smaller than the other string.
// assume you will always receive strings
var shortLongShort = function (a, b) {
    return a.length < b.length ? a + b + a : b + a + b;
};
console.log(shortLongShort('45', '1') === '1451');
console.log(shortLongShort('13', '200') === '1320013');
console.log(shortLongShort('Soon', 'Me') === 'MeSoonMe');
console.log(shortLongShort('U', 'False') === 'UFalseU');
