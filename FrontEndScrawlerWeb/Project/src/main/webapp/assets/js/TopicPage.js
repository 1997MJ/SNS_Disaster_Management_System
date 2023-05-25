

 if(localStorage.getItem("TXT")){
    let txt=localStorage.getItem("TXT");
    document.getElementById("input_val").value=txt;
    let local=document.getElementsByClassName("localName");
    for(i=0;i<local.length;i++){
     local[i].innerHTML=txt;
    }
    writeList(txt,0);
    //localStorage.removeItem("TXT");
  }else{
      writeList(" ",0);
  }


  

function show_input_page(e){
  let txt=document.getElementById("input_val").value;
  localStorage.setItem("TXT",txt);
  if(e.keyCode==13){
    let local=document.getElementsByClassName("localName");
   for(i=0;i<local.length;i++){
    local[i].innerHTML=txt;
   }
    writeList(txt,0);
  }
 

  }
  
  
function writeList(txt,pn){
  $.ajax({
    url:"http://localhost:2000/WriteList",
    type:"post",
    data:{"tag":txt,
    "pageNumber":pn},
    success:function(map){
      console.log(map);
      let list=map.list;
      let cnt=map.cnt;
      $("#writeBody").html("");
    	$.each(list,function(index,dto){
        
         let trClass='<tr>'
         let tr=trClass+
         "<td class="+dto.service+"> 🔔 "+dto.service+"</td>"+
         "<td class="+ 
         returnKeywordName(dto.keyword)
         +">"+returnKeywordEmogi(dto.keyword)+ dto.keyword+"</td>"+
         "<td> <a href='"+ dto.link +"'>"+dto.content+"</a></td>"+
         "</tr>";
      
     
      
      $("#writeBody").append(tr)
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
      writeList(txt,page-1);
	    
	    }
	});
}


// 실시간 재난 문자 방송 
let queryParams = '?' + encodeURIComponent('serviceKey') + '='+'3ChneiHFfHc3Z1V0ZbC6S%2FhQsTLZnr3fx9WvnVcLD%2BeRxG3v2fosUudwVVXQglhuQ71jaypWmhXYUT4j66A9%2BA%3D%3D'; /*Service Key*/
        queryParams += '&' + encodeURIComponent('pageNo') + '=' + encodeURIComponent('1'); /**/
        queryParams += '&' + encodeURIComponent('numOfRows') + '=' + encodeURIComponent('5'); /**/
        queryParams += '&' + encodeURIComponent('type') + '=' + encodeURIComponent('json'); /**/
        
        const url = "http://apis.data.go.kr/1741000/DisasterMsg3/getDisasterMsg1List" + queryParams

        $.ajax({
          type: 'get', //get방식으로 명시
          dataType:'json', //문자형식으로 받기
          url: url,
          success: function(data){ //데이터 주고받기 성공했을 경우 실행할 결과
            const rowData = data?.DisasterMsg[1]?.row
            $.each(rowData, function(idx, value) {
              $("#DisasterHTML").append("<li style='list-style:none'> "+value.create_date+' : '+ value.msg +"</li>")
            })
          },
          error:function(e){ //데이터 주고받기가 실패했을 경우 실행할 결과
            console.log("e: ", e)
          }
        })


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