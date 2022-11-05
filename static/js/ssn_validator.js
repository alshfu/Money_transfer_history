// Validate Swedish Social Security Number (personnummer) using checksum
//   Note: this is somewhat simplified because it does not take into account
//   that the date of the number is valid (e.g. "000000-0000" does return as true)
function isValidSwedishSSN(ssn) {
    ssn = ssn
        .replace(/\D/g, "")     // strip out all but digits
        .split("")              // convert string to array
        .reverse()              // reverse order for Luhn
        .slice(0, 10);          // keep only 10 digits (i.e. 1977 becomes 77)

    // verify we got 10 digits, otherwise it is invalid
    if (ssn.length !== 10) {
        return false;
    }

    let sum = ssn
        // convert to number
        .map(function (n) {
            return Number(n);
        })
        // perform arithmetic and return sum
        .reduce(function (previous, current, index) {
            // multiply every other number with two
            if (index % 2) current *= 2;
            // if larger than 10 get sum of individual digits (also n-9)
            if (current > 9) current -= 9;
            // sum it up
            return previous + current;
        });

    // sum must be divisible by 10
    return 0 === sum % 10;
}

$(function () {
    $('form').submit(function () {
        $('body').append('<br>Result: ' + isValidSwedishSSN($('input[type="text"]').val()))
        return false;
    });
});