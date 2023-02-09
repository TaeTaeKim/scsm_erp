// 중복체크 여부
var idcheck = false;
// 중복여부
var isOverlap = true;
// user 클릭시 form에 넣어주는 함수
function clickaccount(id){
    var id = id.split('-')[0];
    var name = $(`#${id}-name`).text();

    $('#add_username').val(name);
    $('#add_id').val(id);
    

}

//유저를 불러오는 ajax
$(document).ready(function(){
    $.ajax({
        url:'/account/get_user',
        type:'get',
        async:true,
        success:function(res){
            res.forEach(e=>{
                $('#account-tbody').append(
                    `
                    <tr>
                        <td id="${e.account_id}-name" onclick="clickaccount(this.id)">${e.account_name}</td>
                        <td id="${e.account_id}-id" onclick="clickaccount(this.id)">${e.account_id}</td>
                        <td>
                            <div style="display:flex;">
                                <label  for="order">주문권환</label>
                                <input class='auth-label' type="checkbox" name="order" id="${e.account_id}-order">
                                <label  for="instock">재고관리</label>
                                <input class='auth-label' type="checkbox" name="instock" id="${e.account_id}-instock">
                                <label  for="item">물품관리</label>
                                <input class='auth-label' type="checkbox" name="management" id="${e.account_id}-item">
                                <label  for="management">계정관리</label>
                                <input class='auth-label' type="checkbox" name="account" id="${e.account_id}-management">
                            </div>
                        </td>
                        <td><input id="${e.account_id}" onclick='saveauth(this.id)'type="submit" name="auth-save" value="저장"></td>
                    </tr>
                    `
                )
                if(e.account_order){
                    $(`#${e.account_id}-order`).attr('checked','checked')
                }
                if(e.account_instock){
                    $(`#${e.account_id}-instock`).attr('checked','checked')
                }
                if(e.account_item){
                    $(`#${e.account_id}-item`).attr('checked','checked')
                }
                if(e.account_management){
                    $(`#${e.account_id}-management`).attr('checked','checked')
                }
            })
        }
    })
})

// 유저 등록 jquery
$("#add_user").on('click', function(e){
    e.preventDefault()
    var id = $('#add_id').val();
    var username = $('#add_username').val();
    var password = $("#add_pw").val();
    var password_check = $("#add_pwValid").val();

    if(!username | !password| !password_check){
        alert("값을 넣어야합니다");
        return
    }
    // id 등록시 중복체크여부
    if(!idcheck){
        alert("중복체크가 필요합니다.");
        return
    }else{
        // 비밀번호가 다른지 확인
        if(password != password_check){
            alert('비밀번호가 다릅니다');
            return
        }

        // 중복여부
        if(isOverlap){
            alert("이미 존재하는 아이디 입니다.");
        }else{
            // 등록하는 함수
            $.ajax({
                url:'/account/save',
                type:'post',
                async:true,
                dataType:'json',
                contentType:"application/json; charset=utf-8",
                data:JSON.stringify({
                    account_id : id,
                    account_passwd : password,
                    account_name : username
                }),
                success:function(res){
                    if(res){
                        alert("등록에 성공했습니다. 권한을 설정해주세요");
                        window.location.reload();
                        return
                    }else{
                        alert("등록 실패 다시 시도해주세요");
                    }
                }

            })
        }
    }
})



//중복체크 함수
$('#idcheck').click(
    function idValidation(e){
        e.preventDefault()
        id = $("#add_id").val()
        // 아아디 input이 없을 때
        if(!id){
            alert('아이디를 입력하세요')
        // validation api실행 후 중복 여부, 체크여부 변경
        }else{
            $.ajax({
                url:'/account/id_validation',
                type:'get',
                data:{
                    id: id
                },
                async:true,
                success:function(res){
                    isOverlap = res
                    if(!isOverlap){
                        idcheck = true
                        alert('사용할 수 있는 아이디 입니다.')
                        $("#add_id").prop('disabled',true);
                    }else{
                        alert('이미 존재하는 아이디 입니다.')
                    }
                }
            })
        }
    }

)

//권한 저장
function saveauth(id){
    var id = id;
    console.log(id);
    var order = $(`#${id}-order`).is(':checked');
    var instock = $(`#${id}-instock`).is(':checked');
    var item = $(`#${id}-item`).is(":checked");
    var management = $(`#${id}-management`).is(":checked");

    if(id=='admin'){
        alert('관리자 계정은 권한을 변경할 수 없습니다.');
    }else{
        $.ajax({
            url:'/account/user_auth',
            type:'post',
            dataType:'json',
            contentType:'application/json; charset=utf-8',
            data:JSON.stringify({
                account_id :id,
                account_order : order,
                account_instock : instock,
                account_item : item,
                account_management : management
            }),
            success : function(res){
                alert('권한을 변경하였습니다.');
                window.location.reload();
            }
        })
    }
}
//계졍 삭제
$("#delete_user").on('click',function(e){
    e.preventDefault();
    var id = $('#add_id').val();
    if(id=='admin'){
        alert("admin 계정은 삭제할 수 없습니다.");
    }

    $.ajax({
        url:'/account/delete',
        type:'get',
        data : {
            "id":id,
        },
        success:function(res){
            alert(`${id} 계정을 삭제했습니다.`);
            window.location.reload();
        },
        error:function(){
            alert("계정 삭제에 실패했습니다. 다시 시도해 주세요");
        }
    })
})
//비밀번호 변경
$("#update_user").on('click',function(e){
    e.preventDefault();
    var id = $('#add_id').val();
    var password = $("#add_pw").val();
    var password_valid = $('#add_pwValid').val();
    if(!id){
        alert("변경할 사용자를 선택해주세요");
        return
    }
    if (password != password_valid){
        alert("비밀번호가 다릅니다");
        return
    }

    $.ajax({
        url:'/account/update',
        type:'post',
        dataType:'json',
        contentType:'application/json; charset=utf-8',
        data:JSON.stringify({
            account_id : id,
            account_passwd : password
        }),
        success:function(res){
            alert("비밀번호 변경에 성공했습니다.");
        }
    })
})
