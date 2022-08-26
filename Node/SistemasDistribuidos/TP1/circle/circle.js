    var area = function (r) 
    {
        return 3.14 * Math.pow(r, 2);
    }
    var circumference = function (r) 
    {
        return 2 * 3.14 * r;
    }
    module.exports = {
        area:area,
        circumference:circumference
    }