$(document).ready(function(){
    get_orderData()
});

/* 
처음 render시에 모든 데이터를 가져오는 ajax request
*/
function get_orderData(){
    $.ajax({
        url:'/order/get_order',
        type:'get',
        async:true,
        success:function(res){
            res.forEach(e => {
                console.log(e);
                var request_no = 1
                var purchase_no = 1
                if(e.order_status==0){
                    $("#require-tbody").append(
                        `
                        <tr>
                            <th scope="row">${request_no}</th>
                            <td>${e.item_name}</td>
                            <td>${e.order_item}</td>
                            <td>${e.order_num}${e.item_unit}</td>
                            <td>${e.order_requestdate}</td>
                            <td id="${e.order_index}-status" >구매요청</td>
                            <td>
                                <label for="buycheck">발주</label>
                                <input type="checkbox"  name="buycheck" id="${e.order_index}-buycheck" onclick="buycheck(this.id)">
                                <label for="instockcheck">입고</label>
                                <input type="checkbox"  name="instockcheck" id="${e.order_index}-instockcheck">
                                <label for="cancelcheck">취소</label>
                                <input type="checkbox"  name="cancelcheck" id="${e.order_index}-cancelcheck">
                            </td>
                            <td>${e.order_purchasedate}</td>
                            <td>${e.order_instockdate}</td>
                            <td>${e.order_canceldate}</td>
                        </tr>
                        `
                    )
                    request_no ++;
                }else{
                    $("#purchase-tbody").append(
                        `
                        <tr>
                            <th scope="row">${purchase_no}</th>
                            <td>${e.item_name}</td>
                            <td>${e.order_item}</td>
                            <td>${e.order_num}${e.item_unit}</td>
                            <td>${e.order_requestdate}</td>
                            <td id="${e.order_index}-status" ></td>
                            <td>
                                <label for="buycheck">발주</label>
                                <input type="checkbox"  name="buycheck" id="${e.order_index}-buycheck" onclick="buycheck(this.id)">
                                <label for="instockcheck">입고</label>
                                <input type="checkbox"  name="instockcheck" id="${e.order_index}-instockcheck" onclick="instockcheck(this.id)">
                                <label for="cancelcheck">취소</label>
                                <input type="checkbox"  name="cancelcheck" id="${e.order_index}-cancelcheck" onclick="cancelcheck(this.id)">
                            </td>
                            <td>${e.order_purchasedate}</td>
                            <td>${e.order_instockdate}</td>
                            <td>${e.order_canceldate}</td>
                        </tr>
                        `
                    )
                    purchase_no ++;
                }

                // 상태값을 넣는 부분
                if(e.order_status ==1){
                    $(`#${e.order_index}-status`).text('발주완료')

                }else if(e.order_status==2){
                    $(`#${e.order_index}-status`).text('입고완료')
                }
                else if(e.order_status==3){
                    $(`#${e.order_index}-status`).text('취소처리')
                }
                // 체크박스 체크

                if(e.order_purchasedate){
                    $(`#${e.order_index}-buycheck`).attr('checked','checked')
                }
                if(e.order_instockdate){
                    $(`#${e.order_index}-instockcheck`).attr('checked','checked')
                }
                if(e.order_canceldate){
                    $(`#${e.order_index}-cancelcheck`).attr('checked','checked')
                }
            })
        }
    })
}

// 발주 클릭시 옮기고 값을 저장하는 서비스 호출
function buycheck(id){
    var ischecked = $(`#${id}`).prop('checked')
    var order_index = id.split('-')[0]
    // 발주를 체크시 체크해제시
    $.ajax({
        url:'/order/check_purchase',
        type:'get',
        async:true,
        data:{
            order_id : order_index,
            ischeck : ischecked
        },
        success:function(res){
            if(!res){
                alert("변경 실패 다시 시도해주세요");
            }else{
                window.location.reload();
            }
        }
    })
}

function instockcheck(id){
    var ischecked = $(`#${id}`).prop('checked')
    var order_index = id.split('-')[0]
    // 발주를 체크시 체크해제시
    $.ajax({
        url:'/order/check_instock',
        type:'get',
        async:true,
        data:{
            order_id : order_index,
            ischeck : ischecked
        },
        success:function(res){
            if(!res){
                alert("변경 실패 다시 시도해주세요");
            }else{
                window.location.reload();
            }
        }
    })
}

function cancelcheck(id){
    var ischecked = $(`#${id}`).prop('checked')
    var order_index = id.split('-')[0]
    // 발주를 체크시 체크해제시
    $.ajax({
        url:'/order/check_cancel',
        type:'get',
        async:true,
        data:{
            order_id : order_index,
            ischeck : ischecked
        },
        success:function(res){
            if(!res){
                alert("변경 실패 다시 시도해주세요");
            }else{
                window.location.reload();
            }
        }
    })
}