//初始数独定义
sdArr = [];//生成的数独数组
errorArr = [];//错误的格子
blankNum = 30;//空白格子数量
backupSdArr = [];//数独数组备份

//初始化界面
setDemo=function(){
	var $ul=$("<ul>");
	$ul.attr("class","ulsudoku");
	for(var i=1;i<=9;i++){
	    var $li=$("<li>");
	    $li.attr("class","lirow");
        for(var j=1;j<=9;j++){
            var $span=$("<span>");

            $span.text(j);
            i==3||i==6?$span.addClass("spanbottom"):"";
            j==3||j==6?$span.addClass("spanright"):"";
            $span.addClass("spancell");
            $li.append($span);
        }

        $ul.append($li);
	}
	$(".sudoku").append($ul);
}
//获取随机数
getRandom=function (n){
    return Math.floor(Math.random()*n+1)
}
//两个简单数组的并集。
function getConnect(arr1,arr2){
	var i,len = arr1.length,resArr = arr2.slice();
	for(i=0;i<len;i++){
		if($.inArray(arr1[i], arr2)<0){
			resArr.push(arr1[i]);
		}
	}
	return resArr;
}

//两个简单数组差集，arr1为大数组
function　arrMinus(arr1,arr2){
	var resArr = [],len = arr1.length;
	for(var i=0;i<len;i++){
		if($.inArray(arr1[i], arr2)<0){
			resArr.push(arr1[i]);
		}
	}
	return resArr;
}
//在对角线上生成随机数
function setdiagonal(i,j){
    var numArr = [1,2,3,4,5,6,7,8,9];
    var sortedNumArr= numArr.sort(function(){return Math.random()-0.5>0?-1:1});
    var cenNum = parseInt(i+''+j);
    var thIndexArr = [cenNum-11,cenNum-1,cenNum+9,cenNum-10,cenNum,cenNum+10,cenNum-9,cenNum+1,cenNum+11];
    for(var a=0;a<9;a++){
        sdArr[thIndexArr[a]] = sortedNumArr[a];
    }
}
getXArr=function(j,sdArr){
		//获取所在行的值。
		var arr = [];
		for(var a =1;a<=9;a++){
			if(sdArr[parseInt(a+""+j)]){
				arr.push(sdArr[parseInt(a+""+j)])
			}
		}
		return arr;
}
getYArr=function(i,sdArr){
		//获取所在列的值。
		var arr = [];
		for(var a =1;a<=9;a++){
			if(sdArr[parseInt(i+''+a)]){
				arr.push(sdArr[parseInt(i+''+a)])
			}
		}
		return arr;
}
getThArr=function(i,j,sdArr){
		//获取所在三宫格的值。
		var arr = [];
		var cenNum = getTh(i,j);
		var thIndexArr = [cenNum-11,cenNum-1,cenNum+9,cenNum-10,cenNum,cenNum+10,cenNum-9,cenNum+1,cenNum+11];
		for(var a =0;a<9;a++){
			if(sdArr[thIndexArr[a]]){
				arr.push(sdArr[thIndexArr[a]]);
			}
		}
		return arr;
}
getTh=function(i,j){
		//获取所在三宫格的中间位坐标。
		var cenArr = [22,52,82,25,55,85,28,58,88];
		var index = (Math.ceil(j/3)-1) * 3 +Math.ceil(i/3) -1;
		var cenNum = cenArr[index];
		return cenNum;
}
//生成数独数组
function creatsdArr(){
    var that = this;
    sdArr = [];
    setdiagonal(2,2);
    setdiagonal(5,5);
    setdiagonal(8,8);
    var allNum = [1,2,3,4,5,6,7,8,9];
    outerfor:
    for(var i=1;i<=9;i++){
        innerfor:
        for(var j=1;j<=9;j++){
            if(sdArr[parseInt(i+''+j)]){
                continue innerfor;
            }
            var XArr = getXArr(j,sdArr);
            var YArr = getYArr(i,sdArr);
            var thArr = getThArr(i,j,sdArr);
            var arr = getConnect(getConnect(XArr,YArr),thArr);
            var ableArr = arrMinus(allNum,arr);

            if(ableArr.length == 0){
                creatsdArr();
                return;
                break outerfor;
            }

            var item;
            //如果生成的重复了就重新生成。
            do{
                item = ableArr[getRandom(ableArr.length)-1];
            }while(($.inArray(item, arr)>-1));

            sdArr[parseInt(i+''+j)] = item;
        }
    }
    backupSdArr = sdArr.slice();
    return sdArr;
}