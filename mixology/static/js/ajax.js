$(function(){

    $('#search').keydown(function (e){
        if(e.keyCode == 13){
            console.log("ajax_enter")
            $.ajax({
                type: "POST",
                url: "drink/search/",
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
    $('#add-tag').keydown(function (e){
        if(e.keyCode == 13){
            console.log("ajax_addTag")
            $.ajax({
                type: "POST",
                url: "add-tag/",
                data: {
                    'tag' : $('#add-tag').val(),
                    'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
                    },
                success: tagSearchSuccess,
                error: function(xhr, textStatus, errorThrown){
                    alert(errorThrown);
                },
                dataType: 'html'
            });
        };

    });
    $('#cabinetSearch').submit(function(e){

        console.log("ajax_submit")
        $.ajax({
            type: "POST",
            url: "drink/advancedsearch/",
            data: $(this).serialize(),
            success: searchSuccess,
            error: function(xhr, textStatus, errorThrown){
                alert(errorThrown);
            },
            dataType: 'html'
        });
        return false;
    });

});
function tagSearchSuccess(data, textStatus, jqXHR){
    console.log("tagSearchSuccess")

    $('#tag-list').html(data)

}
function searchSuccess(data, textStatus, jqXHR){
            console.log("searchSuccess")

    $('#search-results').html(data);
}