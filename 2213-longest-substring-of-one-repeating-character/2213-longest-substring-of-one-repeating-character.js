/**
 * @param {string} s
 * @param {string} queryCharacters
 * @param {number[]} queryIndices
 * @return {number[]}
 */
var longestRepeating = function(s, queryCharacters, queryIndices) {
    let n = s.length;
    let tree = new Array(4 * n);

    function build(node, l, r) {
        if (l === r) {
            tree[node] = {
                leftChar: s[l],
                rightChar: s[l],
                prefix: 1,
                suffix: 1,
                best: 1,
                len: 1
            };
            return;
        }

        let mid = Math.floor((l + r) / 2);

        build(node * 2, l, mid);
        build(node * 2 + 1, mid + 1, r);

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    function merge(a, b) {
        let result = {
            leftChar: a.leftChar,
            rightChar: b.rightChar,
            prefix: a.prefix,
            suffix: b.suffix,
            best: Math.max(a.best, b.best),
            len: a.len + b.len
        };

        if (a.rightChar === b.leftChar) {
            result.best = Math.max(
                result.best,
                a.suffix + b.prefix
            );

            if (a.prefix === a.len) {
                result.prefix = a.len + b.prefix;
            }

            if (b.suffix === b.len) {
                result.suffix = b.len + a.suffix;
            }
        }

        return result;
    }

    function update(node, l, r, index, char) {
        if (l === r) {
            tree[node] = {
                leftChar: char,
                rightChar: char,
                prefix: 1,
                suffix: 1,
                best: 1,
                len: 1
            };
            return;
        }

        let mid = Math.floor((l + r) / 2);

        if (index <= mid) {
            update(node * 2, l, mid, index, char);
        } else {
            update(node * 2 + 1, mid + 1, r, index, char);
        }

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    build(1, 0, n - 1);

    let answer = [];

    for (let i = 0; i < queryIndices.length; i++) {
        let index = queryIndices[i];
        let char = queryCharacters[i];

        update(1, 0, n - 1, index, char);

        answer.push(tree[1].best);
    }

    return answer;
};