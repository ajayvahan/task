function error_call(element_id,txt){
	// $(element_id).parent().removeClass("has-feedback");
	$(element_id).parent().addClass("has-error");
	$(element_id).next().removeClass("glyphicon glyphicon-user glyphicon-lock form-control-feedback");
	$(element_id).next().addClass("glyphicon glyphicon-remove form-control-feedback");
	$(element_id).next().next().html('<div class="text-danger">'+txt +'</div>');
}


$(document).ready(function(){
	$("input").keypress(function(){
		$(this).parent().removeClass("has-error has-feedback");
		$(this).next().removeClass("glyphicon glyphicon-remove form-control-feedback");
		$(this).next().next().html('');

	});
	
	$("#submit").on("click", function(){
		var username= $("#username").val();
		var password = $("#password").val();
		var error_flag=1;
		

		if(username =="" || username == "None"){
			error_call('#username','please fill username field');
			error_flag = 0;
		}

		if(password == "" || password == "None"){
			error_call("#password",'please fill password field')
			error_flag = 0; 


		}

		if(error_flag){
			return true;
		}
		else{
			return false;
		}

	});

});