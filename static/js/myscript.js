$( function() {
  $( "#dateA" ).datepicker();
  $( "#dateD" ).datepicker();
} );


let app = new Vue({
    el: '#reservation_form',
    data: {
        message: "hello"
    }
});
