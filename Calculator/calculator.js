//console.log("helloooo");
const express = require("express");
const bodyparser = require("body-parser");

const app  =express();
app.use(bodyparser.urlencoded({extended:true}));

app.get("/", function(req , res){
    //console.log(__dirname);
    res.sendFile(__dirname +"/index.html");
});

app.post("/" , function(req , res){
    //console.log(req.body.num1+req.body.num2);
    var num1 = Number(req.body.num1);
    var num2 = Number(req.body.num2);
    var result = num1+num2
    res.send("The result is " + result); 
})

app.get("/bmicalculator", function(req,res){
    res.sendFile(__dirname +"/bmicalculator.html")
})

app.post("/bmicalculator",function(req,res){
    var weight =parseFloat(req.body.weight);
    var height =parseFloat(req.body.height);
    
    var bmi = weight / (height * height);
    
    res.send("your bmi result is " + bmi )
});

app.listen(3000,function(){
    console.log("server started");
})