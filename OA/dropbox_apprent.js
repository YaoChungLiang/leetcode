const escape = (wordlist, keypads) => {
        let newWordList = [];
        for (let i = 0; i < wordlist.length; i++) {
            let arr1 = wordlist[i].split("");
            let newWord = arr1.filter((v, i, a) => a.indexOf(v) === i);
            newWord.sort();
            newWordList = [...newWordList, newWord]
        }
        let newKeyPads = [];
        for (let j = 0; j < keypads.length; j++) {
            let newKeyPad = keypads[j].split("");
            newKeyPads = [...newKeyPads, newKeyPad]
        }
        let output = [];
        for (let k = 0; k < newKeyPads.length; k++) {
            let counter = 0;
            for (let l = 0; l < newWordList.length; l++) {
                let valid = newWordList[l].includes(newKeyPads[k][0]);
                let match = newWordList[l].every( ai => newKeyPads[k].includes(ai) )
                if (valid && match) {
                    counter ++ 
                }
            }
            output = [...output, counter]
        }
        return output
    }

let wordList = ['APPLES', 'PLEAS', 'PLEASE'];
let keypads = ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPRT', 'XAEBKSY'];
console.log(escape(wordList, keypads))