function Trie(data) {
    this.data = data;
}

Trie.prototype.add = function(data) {

    if (data.length == 1 && !this.data.hasOwnProperty(data)) this.Trie.data = data;
    if (data.length == 1 && this.data.hasOwnProperty(data)) {
        let aux = this.data;
        this.data = [aux, data];
    }

    if (this.data.hasOwnProperty(data)) {
        
    }
}

Trie.prototype.search = function(data) {

    if (typeof data !== 'string') return 'Not a string';

    for (let i = 0, l = data.length; i < l; i++) {
        this.array.splice(data.charCodeAt(i)%27, 0, []);
        if (i == l-1) return this.array.splice(data.charCodeAt(i)%27, 0, data);
    }
}

Trie.prototype.remove = function(data) {

    if (typeof data !== 'string') return 'Not a string';

    for (let i = 0; i < data.length; i++) {
        
    }
}