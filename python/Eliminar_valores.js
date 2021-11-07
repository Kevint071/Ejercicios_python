const clean = (arr) => arr.reduce((acc, el) => {

    if (el) {

        acc.push(el)
    }
    return acc
}, [] )

const c = clean([1, undefined, null, 0, 2, 4])

console.log(c)