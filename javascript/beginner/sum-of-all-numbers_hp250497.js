const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const sum_all=(arr)=>{
    try{
        let i,sum=0;
        let min=Math.min(...arr);
        let max=Math.max(...arr);
        for(i=min;i<=max;i++){
            sum+=i;
        }
        return sum;
    }
    catch(err){
        return(err);
    }
    
}

function question(theQuestion) {
    return new Promise(resolve => rl.question(theQuestion, answ => resolve(parseInt(answ))))
}

(async ()=>{
    try{
        var arr=[];
        arr.push(await question("Enter 1st number  "));
        arr.push(await question("Enter 2nd number  "));
        
        console.log("Sum of the array is: "+sum_all(arr));
        process.exit();
    }
    catch(err){
        console.log(err)
        process.exit(1);
    }
    
    
})();