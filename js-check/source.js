// Look's like weak JavaScript auth script :)

$('.c_submit')['click'](function() {
    var first = $('#cpass')['val']();
    var second = 'alk3';
    if (first == '02l1' + second) {
        if (document['location']['href']['indexOf']('?p=') == -1) {
            document['location'] = document['location']['href'] + '?p=' + first;
        };
    } else {
        $('#cresponse')['html']('<div class=\'error\'>Wrong password sorry.</div>');
    };
});

// Password is 0211alk3
