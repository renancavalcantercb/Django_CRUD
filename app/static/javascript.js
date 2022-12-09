(function (win, doc) {
        'use strict';
        if (doc.querySelector('.btnDel')) {
            let btnDelete = doc.querySelectorAll('.btnDel');
            for (let i = 0; i < btnDelete.length; i++) {
                btnDelete[i].addEventListener('click', function (event) {
                    if (confirm('Do you really want to delete this item?')) {
                        console.log('Cancel');

                    } else {
                        event.preventDefault();
                    }
                });
            }
        }

        if (doc.querySelector('#form')) {
            let form = doc.querySelector('#form');
            function sendForm(event) {
                event.preventDefault();
                let data = new FormData(form);
                let ajax = new XMLHttpRequest();
                let token = doc.querySelectorAll('input')[0].value;
                ajax.open('POST', form.action);
                ajax.setRequestHeader('X-CSRFToken', token);
                ajax.onreadystatechange = function () {
                    if (ajax.readyState === 4 && ajax.status === 200) {
                        let result = doc.querySelector('#result');
                        result.innerHTML = 'Item added with success!';
                        result.classList.add('alert');
                        result.classList.add('alert-success');
                    }
                }
                ajax.send(data);
                form.reset();
            }

            form.addEventListener('submit', sendForm, false);
        }
    }
)
(window, document);