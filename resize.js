function resize(){

  let img = document.getElementById("photoTest");
  let buttonName = document.getElementById("resize");
  if(img.width == 800 && img.height==600){
      img.height = 240;
      img.width = 320;
      buttonName.innerHTML = "Agrandar";
  }
  else{
      img.height = 600;
  img.width = 800;
  buttonName.innerHTML = "Achicar";
  }


}


