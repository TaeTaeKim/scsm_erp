var clicked_item;

$(document).ready(function(){
    $('#addimg').on('change',function(){
        var file = this.files[0];

        var reader = new FileReader();


        reader.onload = function(e){
            $('#stockimg_add').attr('src',e.target.result);
        };

        reader.readAsDataURL(file);
    });

    get_stock();
});


$("#add_button").on('click',function(e){
    e.preventDefault();
    
    var item_code = $('#stock_id').val();
    var item_name = $('#stock_name').val();
    var item_stock = $('#stock_num').val();
    var item_unit = $('#stock_unit').val();
    var item_manufact = $('#stock_manufacture').val();
    var item_phone0 = $('#purchase_num_0').val();
    var item_phone1 = $('#purchase_num_1').val();
    var item_phone2 = $('#purchase_num_2').val();
    var item_email = $('#purchase_email').val();
    var item_price = $('#stock_price').val();
    var item_descript = $('#stock_descript').val();
    var item_purchase = $('#stock_purchase').val();

    var item_phone = item_phone0 +'-'+item_phone1+'-'+item_phone2;

    var fileInput = $('#addimg')[0];
    var file = fileInput.files[0]

    if(!item_code | !item_name | !item_unit |!item_stock){
        alert('필수 정보를 입력하세요 (품명, 품번, 단위)')
    } 
    data = JSON.stringify({
        item_code : parseInt(item_code),
        item_name : item_name,
        item_stock : parseFloat(item_stock),
        item_unit : item_unit,
        item_manufact : item_manufact,
        item_phone : item_phone,
        item_email : item_email,
        item_price : parseInt(item_price),
        item_descript : item_descript,
        item_purchase : item_purchase,
        item_img :""
    })
    $.ajax({
        url:'/item/add_item',
        type:'POST',
        contentType:'application/json; charset=utf-8',
        dataType:'json',
        async:false,
        data:data,
        success:function(res){
            if(!res.result){
                alert(`아이템등록 실패 ${res.message}`)
            }else{
                alert('아이템 등록성공')
            }
        }
    })
    if (file){
        add_img(item_code,file);
    }
    window.location.reload()
});

$('#update_button').on('click', (e)=>{
    e.preventDefault();

    var item_code = $('#stock_id').val();
    var item_name = $('#stock_name').val();
    var item_stock = $('#stock_num').val();
    var item_unit = $('#stock_unit').val();
    var item_manufact = $('#stock_manufacture').val();
    var item_phone0 = $('#purchase_num_0').val();
    var item_phone1 = $('#purchase_num_1').val();
    var item_phone2 = $('#purchase_num_2').val();
    var item_email = $('#purchase_email').val();
    var item_price = $('#stock_price').val();
    var item_descript = $('#stock_descript').val();
    var item_purchase = $('#stock_purchase').val();

    var item_phone = item_phone0 +'-'+item_phone1+'-'+item_phone2;

    var fileInput = $('#addimg')[0];
    var file = fileInput.files[0]
    

    if(!item_code | !item_name | !item_unit |!item_stock){
        alert('필수 정보를 입력하세요 (품명, 품번, 단위)')
    } 
    data = JSON.stringify({
        item_code : parseInt(item_code),
        item_name : item_name,
        item_stock : parseFloat(item_stock),
        item_unit : item_unit,
        item_manufact : item_manufact,
        item_phone : item_phone,
        item_email : item_email,
        item_price : parseInt(item_price),
        item_descript : item_descript,
        item_purchase : item_purchase,
        item_img :""
    })

    console.log(data);

    $.ajax({
        url:"/item/update_item?original_item=" + clicked_item,
        type:'POST',
        data:data,
        async:false,
        contentType:'application/json; charset=utf-8',
        dataType:'json',
        success:function(res){
            if(!res.result){
                alert(`아이템등록 실패 ${res.message}`)
            }else{
                alert('아이템 등록성공')
            }
        }
        
    });
    if(file){
        add_img(item_code,file)
    }

    window.location.reload()
})



$("#delete_button").on('click', (e)=> {
    e.preventDefault();
    var item_code = $('#stock_id').val();
    if (!item_code){
        alert('삭제할 품목을 선택하세요');
        window.location.reload();

    }
    
    $.ajax({
        url:'/item/delete_item',
        type:'GET',
        data : {
            item_id: item_code
        },
        async:true,
        success:function(res){
            if(!res.result){
                alert(`품목 삭제실패`)
            }
            else{
                alert(`${item_code} 삭제 성공`)
            }
        },
        complete:()=>{
            window.location.reload();
        }

    })
    console.log('delete clicked');
})

function add_img(item_id,file){
    
    var data = new FormData();
    data.append('file',file);
    // 이미 사진이 존재하면 지워야하는 코드가 필요.
    $.ajax({
        url:'/item/add_image?item_id=' + item_id,
        type:'POST',
        data:data,
        contentType:false,
        processData: false,
        async:false,
        success:function(res){
            console.log(res['message']);
            if(res.result!==true){
                alert(`사진등록 실패 ${res.message}`)
            }
            else{
                alert('사진등록 성공')
            }
        }
    })
}


function get_stock(){
    $.ajax({
        url:'/stocklist/get_stock',
        type:'get',
        async:true,
        success:function(res){
            res.forEach(e => {

                $('#right_stock_list_tbody').append(
                    `
                    <tr id='${e.item_code}' onclick="click_item(this.id)">
                        <td>${e.item_name}</td>
                        <td>${e.item_code}</td>
                    </tr>
                    `
                )
            })
        }
    })
}


function click_item(id){
    clicked_item = id
    console.log(clicked_item)
    $.ajax({
        url:'/stocklist/find_by_id',
        type:'GET',
        data :{
            id : id
        },
        success:function(item){
            fill_management(item);
            fill_itemdetail(item);
        }
    })
}

function fill_management(item){
    $('#stock_id').val(item.item_code);
    $('#stock_name').val(item.item_name);
    $('#stock_num').val(item.item_stock);
    $('#stock_unit').val(item.item_unit);
    $('#stock_manufacture').val(item.item_manufact);
    var phonelist = item['item_phone'].split('-')
    $('#purchase_num_0').val(phonelist[0]);
    $('#purchase_num_1').val(phonelist[1]);
    $('#purchase_num_2').val(phonelist[2]);
    $('#purchase_email').val(item.item_email);
    $('#stock_price').val(item.item_price);
    $('#stock_descript').val(item.item_descript);
    $('#stock_purchase').val(item.item_purchase);
    var path = item.item_img
    if (path) {
        var imgpath = path.split('/');
        var filename = imgpath[imgpath.length -1];
        var relativePath = "../static/img/stockimg/" +filename;
        var img = new Image();
        img.onload = function() {
            $('#stockimg_add').attr('src', img.src);
        };
        img.src = relativePath;
    } else {
        $('#stockimg_add').attr('src', '');
    }

}

function fill_itemdetail(item){
    var path = item.item_img
    if (path) {
        var imgpath = path.split('/');
        var filename = imgpath[imgpath.length -1];
        var relativePath = "../static/img/stockimg/" +filename;
        var img = new Image();
        img.onload = function() {
            $('#stock_img_detail').attr('src', img.src);
        };
        img.src = relativePath;
    } else {
        $('#stock_img_detail').attr('src', '');
    }

    $('#stock_info').html(
        `
        <p>품명 : ${item.item_name}</p>
        <p>품번 : ${item.item_code}</p>
        <p>재고 : ${item.item_stock}<span>${item.item_unit}</span></p>
        <p>제조사 : ${item.item_manufact}</p>
        <p>구매처 : ${item.item_purchase}</p>
        <p>구매처전화번호 : ${item.item_phone}</p>
        <p>구매처이메일 : ${item.item_email}</p>
        <p>설명 : ${item.item_descript}</p>
        `
    )
}

