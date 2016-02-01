function error_call(element_id,txt){
	$(element_id).parent().addClass("has-error has-feedback");
	$(element_id).next().addClass("glyphicon glyphicon-remove form-control-feedback");
	$(element_id).next().next().html('<div class="text-danger">'+txt+'</div>');
}
function error_call_radio(element_id,txt){
	$(element_id).html('<div class="text-danger">'+txt+'</div>');

}

$(document).ready(function(){
	$("input,textarea").keypress(function(){
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
		var dob = $.trim($("#dob").val());
		var mobile = $.trim($("#mobile").val());
		var address = $.trim($("#address").val());
		var street = $.trim($("#street").val());
		var city = $.trim($("#city").val());
		var zip =$.trim($("#zip").val());
		var image = $("#image").val();
		var end = image.substring(image.lastIndexOf('.') + 1);
		var error_flag=1;


		var text="";
		pattern_alpha=/^[A-Za-z]+$/;
		pattern_date=/^\d{4}-\d{1,2}-\d{1,2}$/;
		pattern_mobile=/^[0-9]{10}$/g;
		pattern_zip=/^[0-9]{6}$/g;
		

		if (first_name == "" || first_name == "None" || !first_name.match(pattern_alpha)){
			error_call('#first_name','Please enter first name field and use alphabets only');
			error_flag=0;
		}

		if (last_name == "" || last_name == "None" || !last_name.match(pattern_alpha)){
			error_call('#last_name','Please enter last name field and use alphabets only');
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
		if (mobile == "" || mobile == "None" || !mobile.match(pattern_mobile)){
			error_call('#mobile','Please enter mobile number and mobile should contain 10 digits only');
			error_flag=0;
		}
		if (address == "" || address == "None"){
			error_call('#address','Please enter address field');
			error_flag=0;
		}
		if (street == "" || street == "None" || !street.match(pattern_alpha)){
			error_call('#street','Please enter street field and use alphabets only');
			error_flag=0;
		}
		if (city == "" || city == "None" || !city.match(pattern_alpha)){
			error_call('#city','Please enter city field and use alphabets only');
			error_flag=0;
		}
		if (zip == "" || zip == "None" || !zip.match(pattern_zip)){
			error_call('#zip','Please enter zip field and zip code should contain 6 digits only');
			error_flag=0;
		}
		if( !(end == "JPEG" || end == "jpeg" || end == "jpg" || end == "JPG" || end == "png" || end == "PNG" || end == "gif" || end == "GIF") && (image != "") ) {
			alert("Only JPG, PNG and GIF images are allowed for profile picture");
			$("#image").next().removeClass("help-block");
			$("#image").next().addClass("text-danger");
			$("#image").next().html("Only JPG, PNG and GIF images are allowed for profile picture")
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