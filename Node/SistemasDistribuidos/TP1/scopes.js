/*function foo(){
    var bar;
}*/
/*
function foo(){
    function zip(){
        var quux;
    }

}*/



function foo(){
    var bar;
    quux=2;
    function zip(){
        var quux;
        bar=true;
    }
    return zip;
}