/**$(document).ready(function(){
    $('div').css('color','red');
    var data = $("input[name=csrfmiddlewaretoken]").val();
    $('#search-results').html("<li>" + data + "</li>");
});
*/
$(document).ready(function(){
    
    $('#search').keyup(function() {

        $.ajax({
            type: 'POST',
            url: '/ideas/search/',
            data: {
                'search' : $('#search').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR) {
    $('#search-results').html(data);
}
