$(document).ready(function(){
    $('#addimg').on('change',function(){
        var file = this.files[0];
        console.log(file);

        var reader = new FileReader();


        reader.onload = function(e){
            $('#stockimg_add').attr('src',e.target.result);
        };

        reader.readAsDataURL(file);
    });


    $('#editimg').on('change',function(){
        var file = this.files[0];

        var reader = new FileReader();

        reader.onload = function(e){
            $("#stockimg_edit").attr('src',e.target.result);

        };

        reader.readAsDataURL(file);
    })
})