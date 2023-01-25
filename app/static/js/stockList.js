$(document).ready(function(){
    var popupButtons = $('.popup-button');
    var closeButton = $('.popup-close');

    popupButtons.on('click',function(){
        $("#side-var").css("width",'30%');
        $("#side-var").removeClass('hidden');

        $('#stock-div').css("width",'70%');
    });

    closeButton.on('click',function(){
        $("#side-var").css("width",'0%');
        $("#side-var").addClass('hidden');

        $('#stock-div').css("width",'100%');
    })

    
})