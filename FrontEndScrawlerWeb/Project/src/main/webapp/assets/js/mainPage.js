/**
 * 
 */


// 스토리지 초기화
window.localStorage.clear();


/*페이지 카운트 */
 
let today = new Date();
let year = today.getFullYear();
let month = ('0' + (today.getMonth() + 1)).slice(-2);
let day = ('0' + today.getDate()).slice(-2);
var dateString = year + '-' + month + '-' + day;

$.ajax({
	url: "http://localhost:2000/countTotalAndToday",
	type: "get",
	data: { "date": dateString },

});

/*카운팅 불러오기*/
$.ajax({
	url: "http://localhost:2000/showToday",
	type: "get",
	data: { "date": dateString },
	success: function(dto) {
		$("#main_click_count_today").text(dto.today);
		$("#main_click_count_total").text(dto.total);
	},
	error: function() {
		alert("counting error");
	}
});



/*total sns 트윗수 불러오기*/

let main_total_SNS_click=document.getElementsByClassName("main_total_SNS_click");
let main_total_SNS_name=document.getElementsByClassName("main_total_SNS_name");

$.ajax({
	url: "http://localhost:2000/TweetCountNumberList",
	type: "get",
	success: function(list) {

		for(let i=0;i<list.length;i++){
 		 main_total_SNS_click[i].innerHTML=list[i];
}
	},
	error: function() {
		alert("counting error");
	}
});

//  실시간 인기 검색어 불러오기

let Popular_rank=document.getElementsByClassName("main_rank_name");
let rankName=[];
let rankCount=[];
let word_array = [];
$.ajax({
	url: "http://localhost:2000/PopularRankList",
	type: "get",
	success: function(list) {
		for(let i=0;i<list.length;i++){
    if(i<7){
 		 Popular_rank[i].innerHTML=list[i].tag+"  <mark>"+list[i].count+"</mark>";
    }

      word_array.push({ 'text': list[i].tag, 'weight': list[i].count});

}
$("#example").jQCloud(word_array);
	},
	error: function() {
		alert("counting error");
	}
 
});



$.ajax({
	url: "http://localhost:2000/PopularKeywordList",
	type: "get",
	success: function(list) {
    console.log(list);
		for(let i=0;i<list.length;i++){
    rankName.push(list[i].keyword);
    rankCount.push(list[i].count);

} 
showChart();
},
error: function() {
  alert("counting error");
}

});


// 실시간 인기 차트 불러오기

function showChart(){


var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {
      type: 'horizontalBar', 
      data: {
        labels: rankName,
        datasets: [{
          data: rankCount,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        legend:{ display:false

        },
        Response:false,

        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true,
              fontSize:20,
              fontFamily:'NanumSquareNeo',
              fontWeight: 'bold'
            }
          }]
        }
      }
    });
}

function show_input_main(e){
  
  let txt=document.getElementById("input_val").value;
  if(e.keyCode==13){
      localStorage.setItem("TXT",txt);
      location.href='TopicPage.html';
  }

};




// const chatContainer = document.querySelector("#chat-container");
// const outputArea = document.querySelector("#output-area");
const messageInput = document.querySelector("#message-input");
const sendButton = document.querySelector("#send-button");

const message = [];

function CharbotAnswer(respData){
    let element = document.createElement('div');
    element.innerHTML=respData;
    element.setAttribute("class",'botmsg');
    
    const chatbox = document.getElementById('chatbox');
    chatbox.appendChild(element);
    chatbox.appendChild(document.createElement('br'));
  // chatbox에 추가
}

sendButton.addEventListener("click", async () => {
  document.getElementById('message-input').setAttribute('disabled',"disabled");

  const message = messageInput.value.trim();
  if (!message) return;
  // displayMessage(message, true);
  let elementUser = document.createElement('div');
  elementUser.setAttribute('align', 'right');

  let element = document.createElement('div')
  element.innerHTML=message+"";
  element.setAttribute('class','usermsg');

  const chatbox = document.getElementById('chatbox');
  elementUser.appendChild(element);
  chatbox.appendChild(elementUser);
  chatbox.appendChild(document.createElement('br'));
  
  $.ajax({
    url :"http://localhost:2000/chatbot",
    method: "post",
    data:{'message':message+""},
    success:function(response){
      CharbotAnswer(response);
    document.getElementById('message-input').removeAttribute('disabled');
    }
  });
  document.querySelector("#message-input").value="";
 
});

messageInput.addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    sendButton.click();
  }
});

// $(document).ready(function() {
//   var word_array = [];
//   for (var i = 0; i < rankName.length; i++) {
//     var word = rankName[i];
//     var weight = rankCount[i];
//     word_array.push({ 'text': word, 'weight': weight });
//   }
// $(function() {
//   // When DOM is ready, select the container element and call the jQCloud method, passing the array of words as the first argument.
//   $("#example").jQCloud(word_array);
// });

// });