function edit_validate(){
	var first_name = document.getElementById("first_name").value.trim();
	var last_name = document.getElementById("last_name").value.trim();
	var gender = document.getElementsByName("gender");
	var dob = document.getElementById("dob").value.trim();
	var mobile = document.getElementById("mobile").value.trim();
	var address = document.getElementById("address").value.trim();
	var street = document.getElementById("street").value.trim();
	var city = document.getElementById("city").value.trim();
	var zip =document.getElementById("zip").value.trim();
	var image = document.getElementById("image").value;
	var end = image.substring(image.lastIndexOf('.') + 1);


	var text="";
	pattern_alpha=/^[A-Za-z]+$/;
	pattern_date=/^\d{4}-\d{1,2}-\d{1,2}$/;
	pattern_mobile=/^[0-9]{10}$/g;
	pattern_zip=/^[0-9]{6}$/g;
	

	if (first_name == "" || first_name == "None" || !first_name.match(pattern_alpha)){
		text += "Please enter first name field and use alphabets only\n";
	}

	else if (last_name == "" || last_name == "None" || !last_name.match(pattern_alpha)){
		text += "Please enter last name field and use alphabets only\n";
	}
	else if (gender[0].checked == false && gender[1].checked == false){
		text += "Please select gender field\n";
	}
	else if (dob == "" || dob == "None" || !dob.match(pattern_date)){
		text += " Date of birth field invalid, please enter in YYYY-MM-DD format\n";
	}
	else if (mobile == "" || mobile == "None" || !mobile.match(pattern_mobile)){
		text += "Please enter mobile number and mobile should contain 10 digits only\n";
	}
	else if (address == "" || address == "None"){
		text += "Please enter address field\n";
	}
	else if (street == "" || street == "None" || !street.match(pattern_alpha)){
		text += "Please enter street field and use alphabets only\n";
	}
	else if (city == "" || city == "None" || !city.match(pattern_alpha)){
		text += "Please enter city field and use alphabets only\n";
	}
	else if (zip == "" || zip == "None" || !zip.match(pattern_zip)){
		text += "Please enter zip field and zip code should contain 6 digits only\n";
	}
	if( !(end == "JPEG" || end == "jpeg" || end == "jpg" || end == "JPG" || end == "png" || end == "PNG" || end == "gif" || end == "GIF") && (image != "") ) {
	text += "Only JPG, PNG and GIF images are allowed for profile picture";
	}



	if (text !=""){
		alert(text);
		return false;
	}

}