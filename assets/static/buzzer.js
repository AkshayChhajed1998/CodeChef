console.log("Linked");

var questions = document.getElementById("questions");
var canvas = document.getElementById("canvas");
var pop = document.getElementById("pop");
var pre_ID;
var firstlogintime30;
var ctx = canvas.getContext("2d");
var t,ctr=0,i,s;
var count=0;
var players=2;

function degToRad(degree){
			var factor = Math.PI/180;
			return degree*factor;
		}

$.get('get/firstlogintime',function(data,status){
	firstlogintime30 = Date.parse(data)+1*60*1000;
	console.log(firstlogintime30)
	Timer();
});

$.get('r3get/question',{'buzz':'0'},function(data,status){
	if(data[0]=='<')
	{
		questions.innerHTML=data;
	}
	else
	{
		var obj=JSON.parse(data);
    	console.log(obj);
    	pre_ID=obj.pk;
    	questions.innerHTML=obj.fields.question;
	}
});

var update_Q = function()
{
	$.ajax({
		type:'GET',
		url:'/r3get/currQ',
		success:function(data,status){
		if(data[0]=='<')
		{
			questions.innerHTML=data;
		}
		else
		{
			var obj=JSON.parse(data);
			if(pre_ID!=obj.pk)
			{
				$('#skip').attr('disabled',false);
				$('#buzz').attr('disabled',false);
			}
			pre_ID=obj.pk;
    		questions.innerHTML=obj.fields.question;
		}		
	},
	});
};

//s=setInterval(update_Q,1500);



$('#buzz').click(function()
{
	count=0;
  $.get('r3get/question',{'buzz':'1'},function(data,status){
    if(data[0]=='<')
	{
		questions.innerHTML=data;
	}
	else
	{
		var obj=JSON.parse(data);
    	console.log(obj);
    	pre_ID=obj.pk;
    	questions.innerHTML=obj.fields.question;
	}
  }); 
  pop.innerHTML="<b>Now it's Yours</b>";
  $('#skip').attr('disabled',false);
});

$('#skip').click(function(){
	count=0;
	$('#skip').attr('disabled',true);
	$('#buzz').attr('disabled',true);
	$.get('/r3skip',function(data,status){

		});
});


var Timer=function()
{
	
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	var hrs,min,sec,ms;
	ms = firstlogintime30-(new Date()).getTime();
	console.log(ms)
	hrs = Math.floor(ms/(60*60*1000));
	min = Math.floor((ms-hrs*60*60*1000)/(60*1000));
	sec = Math.floor((ms-hrs*60*60*1000-min*60*1000)/1000);
	var time=hrs+":"+min+":"+sec;
	//var time=min+":"+sec;
	// ctx.strokeStyle = '#00ff00';
	ctx.lineWidth = 10;
	ctx.beginPath();
	ctx.arc(135, 75, 55, degToRad(270), degToRad(-90+(min+sec/60)*36));
	ctx.stroke();

	ctx.font = "bold 25px Courier New";
	// ctx.fillStyle = 'rgba(0, 255, 0, 1)';
	ctx.fillText(time, 100, 80);
	

	if(sec<0 || min<0 || hrs<0)
	{
		$("#buzz").attr('disabled',true);
		$("#skip").attr('disabled',true);
		//clearInterval(s);
		clearInterval(t);
		$.get('/r3finish',{'ID':pre_ID},function(data,status)
		{
			
			questions.innerHTML=data;
			ctx.clearRect(0, 0, canvas.width, canvas.height);
			

		});
	}
	else
	{
		update_Q();
	}

	if(count++ == 60)
	{
		$.get('/r3skip',function(data,status){

		});
		count=0;
	}

	if(min>6)
	{
		ctx.strokeStyle = '#00ff00';
		ctx.fillStyle = 'rgba(0, 255, 0, 1)';
	}

	if(min<=6 && min >3)
	{
		ctx.strokeStyle = '#ff6700';
		ctx.fillStyle = 'rgba(255, 103, 0, 1)';
	}

	if(min<=3)
	{
		ctx.strokeStyle = '#ff0000';
		ctx.fillStyle = 'rgba(255, 0, 0, 1)';
	}
			
};

$('#nextpage').click(function(){
	$.get('/nextpage',function(data,status){

	});
});


t=setInterval(Timer,1000);




$(window).on("unload",function () {
   $.ajax({
     type: 'GET',
     async: false,
     url: '/r3finish?ID='+pre_ID,
   });
});