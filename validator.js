
let lista_fotos = [1];

function insertImage(num){
  let addimagen = document.getElementById(`imageContainer${num}`);
  let len = addimagen.getElementsByTagName('input').length;
  if(len<5) {
    let nuevaImagen = '<input type="file" accept="image/*" name="foto-avistamiento'
      + `${num}`+len.toString()+'">';
    let node = document.createElement("div");
    node.innerHTML = nuevaImagen
    addimagen.appendChild(node);
  }
  else{
    alert("No puedes agregar más fotos de este avistamiento");
  }


}







function insertInformation() {

  lista_fotos.push(1);

  let addInformation = document.getElementById("informationContainer");

  let newInfo =
      `<br>
      <div class="field">
        <div class="text">Día hora</div>
        <input type="text" name="dia-hora-avistamiento" placeholder="yyyy-mm-dd hh:mm" size="20">
      </div>
      <div class="field">
        <div class="text">Tipo</div>
        <select name="tipo-avistamiento">
          <option value="" disabled selected hidden>Seleccione tipo de insecto</option>
          <option value="Insecto">Insecto</option>
          <option value="Arácnido">Arácnido</option>
          <option value="Miriápodo">Miriápodo</option>
          <option value="No sé">No sé</option>
        </select>
      </div>

      <div class="field">
        <div class="text">Estado</div>
        <select name="estado-avistamiento">
          <option value="" disabled selected hidden>Seleccione el estado</option>
          <option value="Vivo">Vivo</option>
          <option value="Muerto">Muerto</option>
          <option value="No sé">No sé</option>
        </select>
      </div>

      <div class="field">
        <div class="photo">
          <div class="text">Foto</div>

        </div>
      </div>
      <div class="field" id='imageContainer`+lista_fotos.length+`'>
      <input type="file" name='foto-avistamiento`+lista_fotos.length+`0'>
      </div>
      <br>
       <button type="button"  onclick="insertImage(`+lista_fotos.length+`)"> Agregar otra foto</button>
      <br>
    </div>`; // comillas multi linea

    var infoChild = document.createElement('div');
    infoChild.innerHTML = newInfo;

    addInformation.appendChild(infoChild)

}


function formValidator(){

  let region = document.getElementsByName("region")[0].value;
  if (!region){
    alert('Selecciona una region');
    return false;
  }

  let comuna = document.getElementsByName("comuna")[0].value;
  if (!comuna){
    alert('Selecciona una comuna');
    return false;
  }

  let sector = document.getElementsByName("sector")[0].value;
  if (sector.length > 100){
      alert("excediste el largo maximo");
    return false;
  }


  let nombre = document.getElementsByName(  "nombre")[0].value;
  let name_regex = /^[a-zA-Z ]*$/;
  if (nombre.length==0 || nombre.length > 200 || !name_regex.test(nombre)) {/*o si no pasó el testeo del regex está malo */
        alert("nombre incorrecto");
        return false;

    }

  let mail = document.getElementsByName("email")[0].value;
  let email_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if ( !email_regex.test(mail) ) {/*o si no pasó el testeo del regex está malo */
        alert("email incorrecto");
        return false;
    }

  let phoneNumber = document.getElementsByName("celular")[0].value;
  let phone_regex = /^[2-9]([0-9]{8})*$/;
  if ( phoneNumber.length >0 && !phone_regex.test(phoneNumber)) {/*o si no pasó el testeo del regex está malo */
        alert("numero celular incorrecto");
        return false;
    }



  let all_dates = document.getElementsByName("dia-hora-avistamiento");
  let date_regex = /^(19|20)[0-9]{2}[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01]) (2[0-3]|[0-1][0-9]):([0-5][0-9])*$/;
  for(let i = 0; i<all_dates.length; i++){
    let date = all_dates[i].value;
    if (!date_regex.test(date)){
      alert("fecha incorrecta");
    return false;
    }
  }



  let all_tipos = document.getElementsByName("tipo-avistamiento");
  for(let i in all_tipos){
    let tipo = all_tipos[i].value;
    if (tipo == "") {
        alert('Selecciona un tipo');
        return false;
      }
    }

  let all_estados = document.getElementsByName("estado-avistamiento");
  for(let i in all_estados){
      let estado = all_estados[i].value;
      if (estado == "") {
        alert('Selecciona un estado');
        return false;
      }
  }


  for (let i = 1; i<=lista_fotos.length; i++) {
    let vacio = isEmpty(i);
    if(vacio){
      alert("no agregaste ninguna foto")
      return false;
    }
  }

  for (let i = 1; i<=lista_fotos.length; i++){
    let imagenContainer = document.getElementById(`imageContainer${i}`);
    let inputImg = imagenContainer.getElementsByTagName('input');
    for(var j = 1; j<=inputImg.length; j++){
      let imagen = inputImg[j-1].value;
      let formato_nofilter = imagen.split(".");
      let formato = formato_nofilter.pop();
      let img_regex = /^(gif|jpe?g|tiff?|png|webp|bmp)*$/;
      if(!img_regex.test(formato)) {
        alert(`inserta una imagen válida, recibí un archivo .${formato}`);
        return false;
      }
    }
  }

  return sendForm();

}
/*

  */

function isEmpty(num){
    let imagenContainer = document.getElementById(`imageContainer${num}`);
    let inputImg = imagenContainer.getElementsByTagName('input');
    for(let j = 1; j<=inputImg.length; j++){
      let imagen = inputImg[j-1];
      if (imagen.files.length != 0){
        return false;
      }
    }
  return true;
}



var regions = {
            "15": ["Gral. Lagos","Putre","Arica","Camarones"],
            "1": ["Camiña","Huara","Pozo Almonte","Iquique","Pica","Colchane","Alto Hospicio"],
            "2": ["Tocopilla","Maria Elena","Ollague","Calama","San Pedro Atacama","Sierra Gorda","Mejillones","Antofagasta","Taltal"],
            "3": ["Diego de Almagro","Chañaral","Caldera","Copiapo","Tierra Amarilla","Huasco","Freirina","Vallenar","Alto del Carmen"],
            "4": ["La Higuera","La Serena","Vicuña","Paihuano","Coquimbo","Andacollo","Rio Hurtado","Ovalle","Monte Patria","Punitaqui","Combarbala","Mincha","Illapel","Salamanca","Los Vilos"],
            "5": ["Petorca","Cabildo","Papudo","La Ligua","Zapallar","Putaendo","Santa Maria","San Felipe","Pencahue","Catemu","Llay Llay","Nogales","La Calera","Hijuelas","La Cruz","Quillota","Olmue","Limache","Los Andes","Rinconada","Calle Larga","San Esteban","Puchuncavi","Quintero","Viña del Mar","Villa Alemana","Quilpue","Valparaiso","Juan Fernandez","Casablanca","Concon","Isla de Pascua","Algarrobo","El Quisco","El Tabo","Cartagena","San Antonio","Santo Domingo"],
            "13": ["Tiltil","Colina","Lampa","Conchali","Quilicura","Renca","Las Condes","Pudahuel","Quinta Normal","Providencia","Santiago","La Reina","Ñuñoa","San Miguel","Maipu","La Cisterna","La Florida","La Granja","Independencia","Huechuraba","Recoleta","Vitacura","Lo Barrenechea","Macul","Peñalolen","San Joaquin","La Pintana","San Ramon","El Bosque","Pedro Aguirre Cerda","Lo Espejo","Estacion Central","Cerrillos","Lo Prado","Cerro Navia","San Jose de Maipo","Puente Alto","Pirque","San Bernardo","Calera de Tango","Buin","Paine","Peñaflor","Talagante","El Monte","Isla de Maipo","Curacavi","Maria Pinto","Melipilla","San Pedro","Alhue","Padre Hurtado"],
            "6": ["Mostazal","Codegua","Graneros","Machali","Rancagua","Olivar","Doñihue","Requinoa","Coinco","Coltauco","Quinta Tilcoco","Las Cabras","Rengo","Peumo","Pichidegua","Malloa","San Vicente","Navidad","La Estrella","Marchigue","Pichilemu","Litueche","Paredones","San Fernando","Peralillo","Placilla","Chimbarongo","Palmilla","Nancagua","Santa Cruz","Pumanque","Chepica","Lolol"],
            "7": ["Teno","Romeral","Rauco","Curico","Sagrada Familia","Hualañe","Vichuquen","Molina","Licanten","Rio Claro","Curepto","Pelarco","Talca","Pencahue","San Clemente","Constitucion","Maule","Empedrado","San Rafael","San Javier","Colbun","Villa Alegre","Yerbas Buenas","Linares","Longavi","Retiro","Parral","Chanco","Pelluhue","Cauquenes"],
            "16": ["Cobquecura","Ñiquen","San Fabian","San Carlos","Quirihue","Ninhue","Trehuaco","San Nicolas","Coihueco","Chillan","Portezuelo","Pinto","Coelemu","Bulnes","San Ignacio","Ranquil","Quillon","El Carmen","Pemuco","Yungay","Chillan Viejo"],
            "8": ["Tome","Florida","Penco","Talcahuano","Concepcion","Hualqui","Coronel","Lota","Santa Juana","Chiguayante","San Pedro de la Paz","Hualpen","Cabrero","Yumbel","Tucapel","Antuco","San Rosendo","Laja","Quilleco","Los Angeles","Nacimiento","Negrete","Santa Barbara","Quilaco","Mulchen","Alto Bio Bio","Arauco","Curanilahue","Los Alamos","Lebu","Cañete","Contulmo","Tirua"],
            "9": ["Renaico","Angol","Collipulli","Los Sauces","Puren","Ercilla","Lumaco","Victoria","Traiguen","Curacautin","Lonquimay","Perquenco","Galvarino","Lautaro","Vilcun","Temuco","Carahue","Melipeuco","Nueva Imperial","Puerto Saavedra","Cunco","Freire","Pitrufquen","Teodoro Schmidt","Gorbea","Pucon","Villarrica","Tolten","Curarrehue","Loncoche","Padre Las Casas","Cholchol"],
            "14": ["Lanco","Mariquina","Panguipulli","Mafil","Valdivia","Los Lagos","Corral","Paillaco","Futrono","Lago Ranco","La Union","Rio Bueno"],
            "10": ["San Pablo","San Juan","Osorno","Puyehue","Rio Negro","Purranque","Puerto Octay","Frutillar","Fresia","Llanquihue","Puerto Varas","Los Muermos","Puerto Montt","Maullin","Calbuco","Cochamo","Ancud","Quemchi","Dalcahue","Curaco de Velez","Castro","Chonchi","Queilen","Quellon","Quinchao","Puqueldon","Chaiten","Futaleufu","Palena","Hualaihue"],
            "11": ["Guaitecas","Cisnes","Aysen","Coyhaique","Lago Verde","Rio Ibañez","Chile Chico","Cochrane","Tortel","O'Higins"],
            "12": ["Torres del Paine","Puerto Natales","Laguna Blanca","San Gregorio","Rio Verde","Punta Arenas","Porvenir","Primavera","Timaukel","Antartica"]
        };

function cargarComunas(){

  let regionesHTML = document.getElementById("region");
  let numeroRegion = regionesHTML.value;

  let comunasHTML = document.getElementById("comuna");
  comunasHTML.innerHTML = '<option value="" disabled selected hidden>Seleccione comuna</option>';

  for (var x in regions[`${numeroRegion}`]){
    let comunasHTML = document.getElementById("comuna");
      let comuna = document.createElement("option")
        comuna.textContent = regions[numeroRegion][x];
        comunasHTML.appendChild(comuna);

  }



}

function sendForm(){
    let message = confirm("Deseas enviar el formulario?");
    if(message){
      return true;
    }
    else{
      return false;
    }

}




