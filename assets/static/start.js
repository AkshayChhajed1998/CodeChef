console.log("Linked");

var questions = document.getElementById("questions");
var canvas = document.getElementById("canvas");
var pre_ID;
var firstlogintime30;
var ctx = canvas.getContext("2d");
var t,ctr,i;

function degToRad(degree){
			var factor = Math.PI/180;
			return degree*factor;
		}


$.get('get/firstlogintime',function(data,status){
	firstlogintime30 = Date.parse(data)+30*60*1000;
	Timer();
});

$.get('get/question',{'ID':' '},function(data,status){
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


$('#next').click(function()
{
  $.get('get/question',{'ID':pre_ID},function(data,status){
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
	// var time=hrs+":"+min+":"+sec;
	var time=min+":"+sec;
	// ctx.strokeStyle = '#00ff00';
	ctx.lineWidth = 10;
	ctx.beginPath();
	ctx.arc(135, 75, 55, degToRad(270), degToRad(-90+(min+sec/60)*12));
	ctx.stroke();

	ctx.font = "bold 25px Courier New";
	// ctx.fillStyle = 'rgba(0, 255, 0, 1)';
	ctx.fillText(time, 100, 80);

	if(sec<0 || min<0 || hrs<0)
	{
		$.get('/finish',{'ID':pre_ID},function(data,status)
		{
			questions.innerHTML=data;
			ctx.clearRect(0, 0, canvas.width, canvas.height);
			clearInterval(t);
			$("#next").attr('disabled',true);

		});
	}

	if(min>20)
	{
		ctx.strokeStyle = '#00ff00';
		ctx.fillStyle = 'rgba(0, 255, 0, 1)';
	}

	if(min<=20 && min >10)
	{
		ctx.strokeStyle = '#ff6700';
		ctx.fillStyle = 'rgba(255, 103, 0, 1)';
	}

	if(min<=10)
	{
		ctx.strokeStyle = '#ff0000';
		ctx.fillStyle = 'rgba(255, 0, 0, 1)';
	}
			
};

t=setInterval(Timer,1000);



$(window).on("unload",function () {
   $.ajax({
     type: 'GET',
     async: false,
     url: '/finish?ID='+pre_ID,
   });
});