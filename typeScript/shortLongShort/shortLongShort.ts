// consider one strings length will ALWAYS be bigger or smaller than the other string.
// assume you will always receive strings
const shortLongShort = (a: string, b: string): string => {
  return a.length < b.length ? a + b + a : b + a + b;
};
