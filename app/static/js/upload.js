$(function() {
    $('#img_file').css({
        'position': 'absolute',
        'top': '-9999px'
    }).change(function() {
        var val = $(this).val();
        var path = val.replace(/\\/g, '/');
        var match = path.lastIndexOf('/');
   $('#filename').css("display","inline-block");
        $('#filename').val(match !== -1 ? val.substring(match + 1) : val);
    });
    $('#filename').bind('keyup, keydown, keypress', function() {
        return false;
    });
    $('#filename, #btn').click(function() {
        $('#img_file').trigger('click');
    });
});