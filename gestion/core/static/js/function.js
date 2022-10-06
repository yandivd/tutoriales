function message_error(obj){

    var html='';

    if(typeof(obj)=='object'){
        var html= '<ul style="text -align: left;">';

        $.each(obj, function(key, value){
            html+='<li>'+key+' : '+value+ '</li>';
            console.log(key);
            console.log(value);
            console.log(html);
        });
        html+='</ul>';
    
    }
    else{
        html='<p>'+obj+'</p>'
    }

    Swal.fire({
        icon: 'error',
        title: 'Oops...', 
        html: html,
        });
}

