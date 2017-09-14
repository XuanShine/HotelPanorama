//
// $(function () {
//  $('#datetimepicker').datetimepicker();
//     $('#datetimepicker1').datetimepicker({
//         useCurrent: false //Important! See issue #1075
//     });
//     $("#datetimepicker").on("dp.change", function (e) {
//         $('#datetimepicker1').data("DateTimePicker").minDate(e.date);
//     });
//     $("#datetimepicker1").on("dp.change", function (e) {
//         $('#datetimepicker').data("DateTimePicker").maxDate(e.date);
//    });
//     // // $('#dateA').datetimepicker();
//     // $('#dateD').datetimepicker();
// });

$(function() {
  // $(".form_datetime").datetimepicker({
  //   format: "dd MM yyyy"
  // });

  $('#dateA').datetimepicker(
    {format: "dd/mm/yyyy"}
  );
  $('#dateD').datetimepicker();
});


$('#dateA').change(function() {
  $.get('getPrice.php',
        {arrivee: $('#dateA').prop('value'), type: $("type_room").prop('value')}, function (data) {
          $('#prix').prop('value', data);
        });
});

$('#dateD').change(function() {
  $.get('getPrice.php',
      {arrivee: $('#dateA').prop('value'), type: $("type_room").prop('value'), depart: $('#dateD').prop('value')},
      function (data) {
        $('#prix').prop('value', data);
  });
});

$('#type_room').change(function() {
  $.get('getPrice.php',
        {arrivee: $('#dateA').prop('value'), type: $("type_room").prop('value')}, function (data) {
          $('#prix').prop('value', data);
        });
});

$('#btnContactUs').click(function(){
    alert("Merci! Votre message a été bien enregistré ");
});



$.get("ReceptionMessage.php", {
  id: "1",
  email: "nguyenthanhmary@yahoo.fr",
   "subject", "message"},
       function(ReceptionMessage){
         $("div#result").html(data);
       });
});
