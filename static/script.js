/*
* @Author: ananayarora
* @Date:   2017-02-11 13:21:37
* @Last Modified by:   ananay
* @Last Modified time: 2017-02-11 13:29:54
*/

$(document).ready(function(){
	$("#form").submit(function(e){
		e.preventDefault();
		var data = "url="+$("#url").val();
		$(".status").html("Processing....");
		$.post("/check", data, function(r){
			$(".status").html(r);
		});
	});
	$(".btn").click(function(){
		$("#form").submit();
	});
});