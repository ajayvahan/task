function error_call(element_id,txt){
	// $(element_id).parent().removeClass("has-feedback");
	$(element_id).parent().addClass("has-error");
	$(element_id).next().removeClass("glyphicon glyphicon-user glyphicon-eye-open form-control-feedback");
	$(element_id).next().addClass("glyphicon glyphicon-remove form-control-feedback");
	$(element_id).next().next().html('<div class="text-danger">'+txt +'</div>');
}


$(document).ready(function(){
	$("input").keypress(function(){
		$(this).parent().removeClass("has-error");
		$(this).next().removeClass("glyphicon-remove");
		$("#username").next().addClass("glyphicon-user");
		$("#password").next().addClass("glyphicon-eye-open");
		$(this).next().next().html('');

	});
	
	$("#login_submit").on("click", function(e){
		e.preventDefault();
		var username= $("#username").val();
		var password = $("#password").val();
		var error_flag=0;
		

		if(username =="" || username == "None"){
			error_call('#username','please fill username field');
			error_flag = 1;
		}

		if(password == "" || password == "None"){
			error_call("#password",'please fill password field')
			error_flag = 1; 


		}

		if(error_flag){
			return false;
		}
		else{
			$.ajax({
				type: "POST",
				dataType: "json",
				url: "/cgi-bin/app/login.py",
				data : $("#myForm").serialize(),

				success: function(data) {
					console.log(data);
					console.log(data['success']);
					if(data['success']){
						if(data['status'] == 'not active'){
							$("#error_message").addClass("alert alert-danger")
							$("#error_message").children().html('<strong>Error!'+data['message']+'</strong>');
							$("#username").parent().addClass("has-error");
							$("#username").next().removeClass("glyphicon glyphicon-user glyphicon-eye-open form-control-feedback");
							$("#username").next().addClass("glyphicon glyphicon-remove form-control-feedback");
							$('#username').next().next().html('');
							$("#password").parent().addClass("has-error");
							$("#password").next().removeClass("glyphicon glyphicon-user glyphicon-eye-open form-control-feedback");
							$("#password").next().addClass("glyphicon glyphicon-remove form-control-feedback");
							$('#password').next().next().html('');

							error_flag = 1;
							return false;	
						}
						else if(data['status'] == 'error'){
							alert(data['message']);
							error_call("#username","wrong username or password");
							error_call("#password","wrong username or password");
							error_flag = 1;
							return false;
							
						}
						else if (data['status'] == 'exception'){
							$("#error_message").addClass("alert alert-danger")
							$("#error_message").children().html('<strong>Error!'+data['message']+'</strong>');
							$("#username").parent().addClass("has-error");
							$("#username").next().removeClass("glyphicon glyphicon-user glyphicon-eye-open form-control-feedback");
							$("#username").next().addClass("glyphicon glyphicon-remove form-control-feedback");
							$('#username').next().next().html('');
							$("#password").parent().addClass("has-error");
							$("#password").next().removeClass("glyphicon glyphicon-user glyphicon-eye-open form-control-feedback");
							$("#password").next().addClass("glyphicon glyphicon-remove form-control-feedback");
							$('#password').next().next().html('');

							error_flag = 1;
							return false;
						}
						
					}
				},
				error : function(data){
					$("#myForm").submit();		
				}	

			});
		}

	});

});