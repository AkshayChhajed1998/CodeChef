var Qnvi = document.getElementById('Qnvi');
var questions = document.getElementById('questions');
var firstlogintime30;
var ctx = canvas.getContext("2d");

function degToRad(degree){
			var factor = Math.PI/180;
			return degree*factor;
		}


$.get('get/firstlogintime',function(data,status){
	firstlogintime30 = Date.parse(data)+50*60*1000;
	Timer();
});


var update_list = function()
{
	$.get('/user_list',function(data,status){
		var arr = data.split(' ');
		var html="";
		console.log(arr);
		for(var i=1;i<arr.length;i++)
		{
			html+="<button class=\"list\">"+arr[i]+"</button>";
		}
		Qnvi.innerHTML=html;
		$('.list').click(function(){
			console.log($(this).text());
			$.get('/Qrender',{'ID':$(this).text()},function(data,status){
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
		$('button').on('click', function(){		//
    		$('button').removeClass('selected');	//
    		$(this).addClass('selected');			//
			});										//
	});

};

update_list();


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
	// var time=min+":"+sec;
	// ctx.strokeStyle = '#00ff00';
	ctx.lineWidth = 10;
	ctx.beginPath();
	ctx.arc(135, 75, 55, degToRad(270), degToRad(-90+(min+sec/60)*6));
	ctx.stroke();

	ctx.font = "bold 20px Courier New";
	// ctx.fillStyle = 'rgba(0, 255, 0, 1)';
	ctx.fillText(time, 100, 80);

	if(sec<0 || min<0 || hrs<0)
	{
		$.get('/r3finishf',function(data,status)
		{
			questions.innerHTML=data;
			ctx.clearRect(0, 0, canvas.width, canvas.height);
			clearInterval(t);
			$('.list').attr('disabled',true);

		});
	}

	if(hrs==1)
	{
		ctx.strokeStyle = '#00ff00';
		ctx.fillStyle = 'rgba(0, 255, 0, 1)';
	}

	if(hrs ==0 && min<60 && min >30)
	{
		ctx.strokeStyle = '#ff6700';
		ctx.fillStyle = 'rgba(255, 103, 0, 1)';
	}

	if(min<=30)
	{
		ctx.strokeStyle = '#ff0000';
		ctx.fillStyle = 'rgba(255, 0, 0, 1)';
	}
			
};

t=setInterval(Timer,1000);