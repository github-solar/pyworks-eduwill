
var watch = setInterval(myWatch,1000)

function myWatch(){
    var date = new Date()
    var now = date.toLocaleTimeString(); //년월일 빼고 시분초만 표시되도록
    document.getElementById("demo").innerHTML = now;
}