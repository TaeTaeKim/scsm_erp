$(document).ready(function(){
    getStockData();
    
})


// 전체 데이터를 로드하는 부분
function getStockData(){
    $.ajax({
        url:'/stocklist/get_stock',
        type:'get',
        success:function(res){
            var index = 1
            res.item.forEach(e =>{
                $('#stock_tbody').append(
                    `
                    <tr>
                        <th scope="row">${index}</th>
                        <td>${e.item_name}</td>
                        <td>${e.item_code}</td>
                        <td id="${e.item_code}-num">${e.item_stock}${e.item_unit}</td>
                        <td><button class="popup-button" id="${e.item_code}" onclick='popupButton(this.id)'>상세보기</button></td>
                        <td>${e.item_descript}</td>
                    </tr>
                    `
                )
                index ++;
            })

            res.usage.forEach(e=>{
                console.log(e)
                $(`#${e.item_code}-num`).append(
                    `
                    <span style="color:red;">(${e.count}건)</span>
                    `
                )
            })
        }
    })
};

// 상세보기 눌렀을 때 아이템 정보를 가져오는 부분
function getDataById(id){
    $.ajax({
        url:'/stocklist/find_by_id',
        type:'get',
        async:true,
        data:{
            id:id
        },
        success:function(res){
            if(!res){
                alert('찾는 모델이 없습니다.')
            }else{
                // path가 없을 경우 문제가 생김.
                var path = res["item_img"].split('/')
                var filename =path[path.length -1]
                var relativePath = "../static/img/stockimg/" +filename
                $('#stock-sidename').text(res.item_name)
                $('#stock_img').attr('src',relativePath)
                $('#stock-detail').html(
                    `
                    <div>제조사: ${res.item_manufact}</div>
                    <div>단가: ${res.item_price}</div>
                    <div id="side-itemcode">분류코드 : ${res.item_code}</div>
                    <div>연락처: ${res.item_phone}</div>
                    <div>email: ${res.item_email}</div>
                    `
                );
            }
        }
    })
};


//팝업을 띄우는 함수
function popupButton(id){
    $("#side-var").css("width",'30%');
    $("#side-var").removeClass('hidden');

    $('#stock-div').css("width",'70%');
    
    getDataById(id);
    getUsage(id);

}
function closeButton(){
    $("#side-var").css("width",'0%');
    $("#side-var").addClass('hidden');

    $('#stock-div').css("width",'100%');
    $('#stock_img').attr('src',"")
}
// 발주를 올리는 함수
function makeOrder(){
    var item = $("#side-itemcode").text();
    var item_code = item.split(':')[1].trim();

    var order_num = $("#buy-number").val();

    $.ajax({
        url:'/stocklist/order_stock',
        type:'POST',
        dataType:'json',
        contentType:'application/json; charset=utf-8',
        data : JSON.stringify({
            order_item : item_code,
            order_num : order_num
        }),
        success:function(res){
            if(res.result){
                alert(`${item_code}품목 ${order_num}개 발주 성공`);
                window.location.reload();
            }
        }
    })
}
// 사용등록을 하는 함수
function makeUsage(){
    var item = $("#side-itemcode").text();
    var item_code = item.split(':')[1].trim();

    var usage_num = $("#use-number").val();

    $.ajax({
        url:'/stocklist/use_stock',
        type:'GET',
        data : {
            item_code : item_code,
            use_num : usage_num
        },
        success:function(res){
            if(res.result){
                alert(`${item_code} 품목 ${usage_num}개 사용등록 완료`);
                window.location.reload();
            }
        }
    })
}

// 상세보기 클릭시 사용등록울 가져오는 함수
function getUsage(id){
    $('#stock_usage_tbody').html('');
    $.ajax({
        url:'/stocklist/get_stock_usage',
        type:'GET',
        data : {
            item_code : id
        },
        success:function(res){
            if(res.result){
                res.usages.forEach( e => {
                    $('#stock_usage_tbody').append(
                        `
                        <tr>
                            <td id="${e.usage_id}-num">${e.usage_num}</td>
                            <td>${e.usage_date}</td>
                            <td><input type="checkbox" onclick="usageCheck(this.id)" id="${e.usage_id}-${e.usage_item}"></td>
                            <td><input type="checkbox" onclick="cancelCheck(this.id)" id="${e.usage_id}-cancel"></td>
                        </tr>
                        `
                    )
                    if(e.usage_check){
                        $(`#${e.usage_id}-${e.usage_item}`).attr('checked','checked');
                    }
                })
            }
        }
    })
}

function usageCheck(id){
    var usage_id = id.split('-')[0];
    var item_id = id.split('-')[1];
    var ischeck = $(`#${id}`).prop('checked');
    var use_num = $(`#${usage_id}-num`).text();

    $.ajax({
        url:'/stocklist/use_check',
        type:'GET',
        data:{
            usage_id : usage_id,
            item_code : item_id,
            ischeck : ischeck,
            use_num : use_num

        },
        success:function(){
            window.location.reload();
        }
    })
}

function cancelCheck(id){
    var usage_id = id.split('-')[0];
    $.ajax({
        url:'/stocklist/cancel_usage',
        type:'GET',
        data:{
            usage_id : usage_id
        },
        success:function(){
            window.location.reload();
        }
    })
}
