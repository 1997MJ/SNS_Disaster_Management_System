
keywordList=[];
keywordvalueList=[];
colorList=['#ADD8E6','#FF0000','#FFA500','#0000FF','#A52A2A','#A9A9A9'];


$.ajax({
  url:"http://localhost:2000/getKeyword",
  type:"get",
  success :function(map){
 
    $.each(map,function(index,dto){
      keywordList.push(dto.keyword);
      keywordvalueList.push(parseInt(dto.keywordvalue));
      
    });


    new Chart(document.getElementById("pie-chart"), {

      type: 'pie',
      data: {
        labels:  keywordList,
        datasets: [{
          label: "Population (millions)",
          backgroundColor: colorList,
          data:  keywordvalueList
        }]
      },
      options: {
        tooltips: {
          callbacks: {
            label: function(tooltipItem, data) {
              var label = data.labels[tooltipItem.index];
              var value = data.datasets[0].data[tooltipItem.index];
              return label + ': ' + value;
            }
          }
        },
        
        responsive: false,
       legend:{
        labels:{

          fontSize:15,
        },
       position:'bottom'
       },
       
        title: {
          display: true,
          text: '실시간 키워드 차트',
          
        }
      }
    });


  },
  error:function(){

  }})


