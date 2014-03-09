$(function(){

    $('#search').keydown(function (e){
        if(e.keyCode == 13){
            console.log("ajax")
            $.ajax({
                type: "POST",
                url: "search/",
                data: {
                    'search_text' : $('#search').val(),
                    'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
                    },
                success: searchSuccess,
                error: function(xhr, textStatus, errorThrown){
                    alert(errorThrown);
                },
                dataType: 'html'
            });
        };
    });
});

function searchSuccess(data, textStatus, jqXHR){
            console.log("searchSuccess")

    $('#search-results').html(data);
}