function error_call(element_id,txt){
	$(element_id).parent().addClass("has-error has-feedback");
	$(element_id).next().addClass("glyphicon glyphicon-remove form-control-feedback");
	$(element_id).next().next().html('<div class="text-danger">'+txt+'</div>');
}
function error_call_radio(element_id,txt){
	$(element_id).html('<div class="text-danger">'+txt+'</div>');

}

$(document).ready(function(){
	$("input").keypress(function(){
		$(this).parent().removeClass("has-error has-feedback");
		$(this).next().removeClass("glyphicon glyphicon-remove form-control-feedback");
		$(this).next().next().html('');
	});
	$("#gender_male,#gender_female").click(function(){
		$("#div_gender").html('');
	});
	$("#submit").on("click", function(){
		var first_name = $.trim($("#first_name").val());
		var last_name = $.trim($("#last_name").val());
		var username = $.trim($("#username").val());
		var password = $("#password").val();
		var confirm_password = $("#confirm_password").val();
		var dob = $.trim($("#dob").val());
		var email = $.trim($("#email").val());
		var mobile = $.trim($("#mobile").val());
		var error_flag=1;
		var text="";

		var pattern_alpha=/^[A-Za-z]+$/;
		var pattern_date=/^\d{4}-\d{1,2}-\d{1,2}$/;
		var pattern_email=/^([a-zA-Z0-9.])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})+$/g;
		var pattern_mobile=/^[0-9]{10}$/g;


		if (first_name == "" || first_name == "None" || !first_name.match(pattern_alpha)){
			error_call('#first_name','Please enter first name field and use alphabets only');
			error_flag=0;
		
		}
		if (last_name == "" || last_name == "None" || !last_name.match(pattern_alpha)){
			error_call('#last_name','Please enter last name field and use alphabets only');
			error_flag=0;
		}
		if (username == "" || username == "None"){
			error_call('#username','Please enter username field');
			error_flag=0;
		}
		if (password == "" || password == "None"){
			error_call('#password','Please enter password field');
			error_flag=0;
		}
		if (confirm_password == "" || confirm_password == "None"){
			error_call('#confirm_password','Please enter confirm password field');
			error_flag=0;
		}
		if(!$('input[name=gender]:checked').val()) {
			error_call_radio('#div_gender','Please select gender field');
			error_flag=0;
		}
		if (dob == "" || dob == "None" || !dob.match(pattern_date)){
			error_call('#dob','Date of birth field invalid, please enter in YYYY-MM-DD format');
			error_flag=0;
		}
		if (email == "" || email == "None" || !email.match(pattern_email)){
			error_call('#email','Invalid email address, please enter valid email address');
			error_flag=0;
		}
		if (mobile == "" || mobile == "None" || !mobile.match(pattern_mobile)){
			error_call('#mobile','Please enter mobile number and mobile should contain 10 digits only');
			error_flag=0;
		}
		else if (password != confirm_password){
			error_call('#password',"password didn't match");
			error_call('#confirm_password',"password didn't match");
			error_flag=0;
			
		}
		if (error_flag){
			return true;
		}
		else{
			return false;	
		}

	});
});