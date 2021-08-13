function resize(i){

  let img = document.getElementById("foto"+i.toString());

  if(img.width == 800 && img.height==600){
      img.height = 240;
      img.width = 320;
  }
  else{
      img.height = 600;
      img.width = 800;
  }


}


