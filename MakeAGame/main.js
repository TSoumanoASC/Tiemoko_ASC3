
function setup(){
	createCanvas(700,700);
	background(0);
	y=650;
}
function draw(){
	background(0);
	fill(255,69,0);
    x=mouseX;
    y=mouseY;
	
	if (x>=670)
		x=650;
			if (y<=601)
				y=600;
			if (y>=670)
				y=665;

	if (x<= 20)
		x=48;
			if (y<=601)
				y=600;
			if (y>=670)
				y=665;

	ellipse(x,y,100,100,100,100);
	if (mouseIsPressed) {
    if (mouseButton == LEFT)
    ellipse(x,y,100,100,100,100);
      	y=y+30;
      		
    if (mouseButton == RIGHT)
      rect(25, 25, 50, 50);



}
}




