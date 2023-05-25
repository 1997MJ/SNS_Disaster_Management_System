if(localStorage.getItem("TXT")){
  let txt=localStorage.getItem("TXT");
  document.getElementById("input_val").value=txt;
  let local=document.getElementsByClassName("localName");
  for(i=0;i<local.length;i++){
   local[i].innerHTML=txt;
  }
  newsList(txt,0);

}else{
  newsList(" ",0);
}


function show_input_page(e){
  let txt=document.getElementById("input_val").value;
  localStorage.setItem("TXT",txt);
  if(e.keyCode==13){
    let local=document.getElementsByClassName("localName");
   for(i=0;i<local.length;i++){
    local[i].innerHTML=txt;
   }}
   newsList(txt);

  }

function newsList(txt,pn){
  $("#newsBody").html("");
  $.ajax({
    url:"http://localhost:2000/newsList",
    type:"post",
    data:{"tag":txt,
    "pageNumber":pn},
    success:function(map){
      let list=map.list;
      let cnt=map.cnt;
      $("#newsBody").html("");
      $.each(list,function(index,dto){
        let tr="<tr>"
        +"<td class="+ returnKeywordName(dto.keyword)+">"
        +
        returnKeywordEmogi(dto.keyword)+dto.keyword+"</td>"
        +"<td> <a href='"
        +dto.link
        +"'>"
        +dto.title
        +"</a>"
        +"</td>"
        "</tr>";
        $("#newsBody").append(tr)
      });
      loadPaging(cnt,pn);
  
    },error:function(){
      console.log('error')
    }
  });
  
  }

  function loadPaging(cnt,pn){
    $('#pagination').twbsPagination("destroy");
    $('#pagination').twbsPagination({
        startPage: pn+1,
        totalPages: cnt,
        visiblePages: 20,
        first:'<span srid-hidden="true">«</span>',
        prev:"이전",
        next:"다음",
        last:'<span srid-hidden="true">»</span>',
        initiateStartPageClick :false,
        onPageClick: function (event, page) {
        txt=document.getElementById("input_val").value;
        newsList(txt,page-1);
         
        }
    });
  }
  
  
function returnKeywordName(keyword){

  let name;
  if(keyword=='폭설'){
    name='heavysnow';
  }else if(keyword=='교통사고'){
    name='Traffic';
  }else if(keyword=='화재'){
    name='fire';
  }else if(keyword=='태풍'){
    name='typhoon';
  }else if(keyword=='지진'){
    name='earthquake';
  }else if(keyword=='압사'){
    name='stampede';
  }
return name;
}

function returnKeywordEmogi(keyword){

  let emogi;
  if(keyword=='폭설'){
    emogi='⛄️';
  }else if(keyword=='교통사고'){
    emogi='🚗';
  }else if(keyword=='화재'){
    emogi='🔥';
  }else if(keyword=='태풍'){
    emogi='🌀';
  }else if(keyword=='지진'){
    emogi='⛰️';
  }else if(keyword=='압사'){
    emogi='👨‍👦‍👦';
  }
return emogi;
}