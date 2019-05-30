$(function () {
    var $messages = $('.messages-content');

    $(window).load(function () {
        $messages.mCustomScrollbar();
    });


    var namespace = '';
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    socket.on('connect', function () {
        //console.log('connected!');
        socket.emit('join', {room: 'A_Room'});
    });

    function updateScrollbar() {
        $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
            scrollInertia: 10,
            timeout: 0
        });
    }

    function setDate(time) {
        $('<div class="timestamp">' + time + '</div>').appendTo($('.message:last'));
    }

    function insertMessage() {
        //console.log('insertMessage');
        var msg = $('.message-input').val();
        console.log(msg);
        msg = unescape(decodeURIComponent(msg));
        console.log(msg);

        if ($.trim(msg) == '') {
            return false;
        }
        //console.log('send Inqueiry');
        var obj = {
            msg: msg,
            room: 'A_Room'
        };
        console.log(obj);
        socket.emit('sendInquiry', obj);
    }


    socket.on('getInquiry', function (msg) {
        //console.log(msg.msg);
        $('<div class="message new"><figure class="avatar"><img src="/static/mugshot/' + msg.PictureUrl + '" /></figure>' + msg.msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
        setDate(msg.time);
        updateScrollbar();
    });


    $('.message-submit').click(function () {
        insertMessage();
        $('.message-input').val(null);
    });

    $(window).on('keydown', function (e) {
        if (e.which == 13) {
            insertMessage();
            $('.message-input').val(null);
            return false;
        }
    });


});