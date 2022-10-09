function List() { //                                                     list
    this.head = null;
}

function Node(data) { //                                                 node
    this.data = data;
    this.next = null;
}

function HashT() { //                                                  hashtable
    this.table = new Array(100);
    for (let i = 0, len = this.table.length; i < len; i++){
      this.table.push(new List());
    };
}

let hashTable = new HashT();
hashTable;

HashT.prototype.hash = function(data) { //                               hash
    let rst = 0;
    for (var i = 0, len = str.length; i < len; i++) {
      rst += data.charCodeAt(i);
    }
    return Math.floor(rst/i)%101;
}

HashT.prototype.add = function(data) { //                                 add
    const hashed = this.hash(data);
    // this.table[]
}