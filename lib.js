$(document).ready(function() { 
	var options = {
		target: '#logbox'
	};

	$('#former').ajaxForm(options);

});

function getName (str){
    if (str.lastIndexOf('\\')){
        var i = str.lastIndexOf('\\')+1;
    }
    else{
        var i = str.lastIndexOf('/')+1;
    }						
    var filename = str.slice(i);			
    var uploaded = document.getElementById("fileformlabel");
    uploaded.innerHTML = filename;
};

function getName1 (str){
    if (str.lastIndexOf('\\')){
        var i = str.lastIndexOf('\\')+1;
    }
    else{
        var i = str.lastIndexOf('/')+1;
    }						
    var filename = str.slice(i);			
    var uploaded = document.getElementById("fileformlabel1");
    uploaded.innerHTML = filename;
};

function validateForm () {
	
	// var options = {
		// target: '#logbox'
	// };

	// $('#former').validate({

		// Правила
		// rules:{
			// xml: 'required',
			// xsd: 'required'
		// },
		// Текста предупреждений
		// messages:{
			// xml: 'Fill in the field, please',
			// xsd: 'Fill in the field, please'
		// },
		// Обработчик и отправка данных
		// submitHandler: function(form){
			// $(form).ajaxForm(options);
		// }

	// });	
var x=document.forms["theForm"]["xml"].value;
if (x==null || x=="")
  {
  alert("Please, fill in what's empty");
  return false;
  }
};