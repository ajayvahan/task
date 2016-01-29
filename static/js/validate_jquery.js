$(document).ready(function(){
	$("#submit").on("click", function(){
		var first_name = $.trim($("#first_name").val());
		var last_name = $.trim($("#last_name").val());
		var username = $.trim($("#username").val());
		var password = $("#password").val();
		var confirm_password = $("#confirm_password").val();
		var dob = $.trim($("#dob").val());
		var email = $.trim($("#email").val());
		var mobile = $.trim($("#mobile").val());
		var text = "";

		var pattern_alpha=/^[A-Za-z]+$/;
		var pattern_date=/^\d{4}-\d{1,2}-\d{1,2}$/;
		var pattern_email=/^([a-zA-Z0-9.])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})+$/g;
		var pattern_mobile=/^[0-9]{10}$/g;


		if (first_name == "" || first_name == "None" || !first_name.match(pattern_alpha)){
		text += "Please enter first name field and use alphabets only\n";
		}
		else if (last_name == "" || last_name == "None" || !last_name.match(pattern_alpha)){
		text += "Please enter last name field and use alphabets only\n";
		}
		else if (username == "" || username == "None"){
			text +=  "Please enter username field "
		}
		else if (password == "" || password == "None"){
			text += "Please enter password field\n";
		}
		else if (confirm_password == "" || confirm_password == "None"){
			text += "Please enter confirm password field\n";
		}
		else if(!$('input[name=gender]:checked').val()) {
			text += "Please select gender field\n";
		}
		else if (dob == "" || dob == "None" || !dob.match(pattern_date)){
		text += " Date of birth field invalid, please enter in YYYY-MM-DD format\n";
		}
		else if (email == "" || email == "None" || !email.match(pattern_email)){
			text += "Invalid email address, please enter valid email address\n";
		}
		else if (mobile == "" || mobile == "None" || !mobile.match(pattern_mobile)){
			text += "Please enter mobile number and mobile should contain 10 digits only\n";
		}
		else if (password != confirm_password){
				text += "Password didn't  match, please enter correct password\n";
		}
		if (text !=""){
			alert(text);
			return false;
		}

	});
});