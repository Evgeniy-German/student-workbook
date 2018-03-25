 $(document).ready(function () {
                mode();
                setInterval('mode()', 1000);
                $.scrollTo('#scroll_down');
            });
function mode() {
     $.ajax({
         url:'/messages',
         success:function (html) {
             $('#display').html(html);
             }
             })
}
function scrollDown() {
    $('#display').scrollTop(99999);
 }
 function submit() {
     $.ajax({
         type: "POST",
         data: $('#messages_form').serialize(),
         url: "/chat",
         success: function (data) {
             $('#messages_form').html(data);
         }
     });
         $('#message_form')[1].reset();
 }
