function buttonClick(color) {
  $.ajax('/api/change?color=' + color, {
    success: function() {
      if (color != 'reset') {
        $('.reset-msg').hide();
        $('.sent').show();
        $('.sent').css('visibility', 'visible');
        $('.sent').removeClass('green purple red');
        $('.sent').addClass(color);
      } else {
        $('.sent').hide();
        $('.reset-msg').show();
      }
    }
  });
}

$(function() {
  $('.action-button').click(function() {
    buttonClick($(this).data('color'));
  })
});
