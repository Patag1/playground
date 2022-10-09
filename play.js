// const str = 'Hello World!';
// let arr = [];

// for (let i = 0, n = str.length; i < n; i++) { // no calculamos .length todas las iteraciones
//     arr.push(str[i], str[i+1]);
// }

// console.log(arr);



// const str = 'div.class';

// const point = str.indexOf('.');

// console.log(str.match(/[a-z]+[.]/g).join().slice(0, point));

// console.log(str.match(/[.][a-z]+/g).join().slice(1));

// console.log(str.match(/[a-z]+/ig));



// document.querySelector('.class').addEventListener('click', function(){})...
// $('.class').click(function(){})...



// $('.pedidos').click(() => {                                                                           // click con clase pedidos
//     $.get('https://jsonplaceholder.typicode.com/posts', response => {                                 // get info de la database
//         response.forEach(r => $(`<div id="${r.id}"><p>title: ${r.title}</p><p>${r.body}</p></div>`)).appendTo('body');
                                                                                                         // para cada info todo eso
//     });
// });

// $('.pedido').click(() => {
//     let input = $('input');
//     $.get(`https://jsonplaceholder.typicode.com/posts/${input[0].value}`, data => {
//         data.forEach(d => $(`<div id="${d.id}"><p>title: ${d.title}</p><p>${d.body}</p></div>`)).appendTo('body');
//     });
//     input[0].value = '';
// });