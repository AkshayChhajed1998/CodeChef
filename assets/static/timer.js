var cnt=0;
var canvas = document.getElementById("canvas");
		var ctx = canvas.getContext("2d");

		ctx.strokeStyle = '#00ffff';
		ctx.lineWidth = 17;
		ctx.shadowBlur= 15;
		ctx.shadowColor = '#00ffff'

		function degToRad(degree){
			var factor = Math.PI/180;
			return degree*factor;
		}
                
		function renderTime(){
                        cnt++;
			var hrs = Math.floor(60-(cnt/3600)%60);
			var min = Math.floor(60-(cnt/600)%60);
			var sec = Math.floor(60-(cnt/10)%60);
			var mil = 10-cnt%10;
			var smoothsec = 60-(cnt/10)%60;
                        var time = min+":"+(sec<10?'0':'')+sec+":"+(mil-1);
                        
                        
                        if(cnt>36000){
                            alert("TIME OUT!!! well coded...");
                            window.location="login.html";
                        }
      var smoothmin = min+(smoothsec/60);

			//Background
			gradient = ctx.createRadialGradient(250, 250, 5, 250, 250, 300);
			gradient.addColorStop(0, "#03303a");
			gradient.addColorStop(1, "black");
			ctx.fillStyle = gradient;
			//ctx.fillStyle = 'rgba(00 ,00 , 00, 1)';
			ctx.fillRect(0, 0, 500, 500);
			//Minutes
			ctx.beginPath();
			ctx.arc(250,250,170, degToRad(270), degToRad((smoothmin*6)-90));
			ctx.stroke();
			//Seconds
			ctx.beginPath();
			ctx.arc(250,250,140, degToRad(270), degToRad((smoothsec*6)-90));
			ctx.stroke();
			//Time
			ctx.font = "45px Courier New";
			ctx.fillStyle = 'rgba(00, 255, 255, 1)';
			ctx.fillText(time, 150, 270);

		}
		setInterval(renderTime, 100);