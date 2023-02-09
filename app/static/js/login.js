// $("#login-button").on('click',function(e){
//     e.preventDefault()
//     var id = $("#username").val();
//     var password = $("#password").val();
    
//     if (!id | !password){
//         alert('로그인 정보를 입력하세요')
//         window.location.reload();
//     }

//     $.ajax({
//         url:'/auth/login',
//         type:'post',
//         dataType:"json",
//         contentType:"application/json; charset-utf8",
//         data:JSON.stringify({
//             account_id : id,
//             account_passwd : password
//         })
//     })
// })