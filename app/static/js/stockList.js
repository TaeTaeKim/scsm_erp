$(document).ready(function(){
    getStockData()
    
})


// 전체 데이터를 로드하는 부분
function getStockData(){
    $.ajax({
        url:'/stocklist/get_stock',
        type:'get',
        success:function(res){
            res.forEach(e =>{
                var index = 1
                $('#stock_tbody').append(
                    `
                    <tr>
                        <th scope="row">${index}</th>
                        <td>${e.item_name}</td>
                        <td>${e.item_code}</td>
                        <td>${e.item_stock}${e.item_unit}</td>
                        <td><button class="popup-button" id="${e.item_code}" onclick='popupButton(this.id)'>상세보기</button></td>
                        <td>${e.item_descript}</td>
                    </tr>
                    `
                )
                index ++;
            })
        }
    })
}
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
                $('#stock-sidename').text(res.item_name)
                $('#stock_img').attr('src',`../static/img/stockimg/${res.item_img}`)
                $('#stock-detail').html(
                    `
                    <div>제조사: ${res.item_manufact}</div>
                    <div>단가: ${res.item_price}</div>
                    <div>분류코드 : ${res.item_code}</div>
                    <div>연락처: ${res.item_phone}</div>
                    <div>email: ${res.item_email}</div>
                    `
                );
            }
        }
    })
}

function popupButton(id){
    $("#side-var").css("width",'30%');
    $("#side-var").removeClass('hidden');

    $('#stock-div').css("width",'70%');
    
    getDataById(id);

}
function closeButton(){
    $("#side-var").css("width",'0%');
    $("#side-var").addClass('hidden');

    $('#stock-div').css("width",'100%');
    $('#stock_img').attr('src',"")
}