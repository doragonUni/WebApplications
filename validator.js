

function insertImage(num){
  let addimagen = document.getElementById(`imageContainer${num}`);
  if(addimagen.getElementsByTagName('input').length<5) {
    var nuevaImagen = document.createElement('input');
    nuevaImagen.type = "file";
    nuevaImagen.name = "foto-avistamiento"
    addimagen.appendChild(nuevaImagen)
  }
  else{
    alert("No puedes agregar más fotos de este avistamiento");
  }


}





let lista_fotos = [1];

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
          <option value="3">Insecto</option>
          <option value="4">Arácnido</option>
          <option value="5">Miriápodo</option>
          <option value="2">No sé</option>
        </select>
      </div>

      <div class="field">
        <div class="text">Estado</div>
        <select name="estado-avistamiento">
          <option value="" disabled selected hidden>Seleccione el estado</option>
          <option value="3">Vivo</option>
          <option value="4">Muerto</option>
          <option value="2">No sé</option>
        </select>
      </div>

      <div class="field">
        <div class="photo">
          <div class="text">Foto</div>

        </div>
      </div>
      <div class="field" id='imageContainer`+lista_fotos.length+`'>
      <input type="file" name='foto-avistamiento'>
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

/*
  let tipo = document.getElementsByName("tipo-avistamiento")[0].value;
  if (tipo ==""){
    alert('Selecciona un tipo');
    return false;
  }
*/

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

/*
  let estado = document.getElementsByName("estado-avistamiento")[0].value;
  if (!estado){
    alert('Selecciona un estado');
    return false;
  }
*/

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

/*
  let imagen = document.getElementsByName("foto-avistamiento")[0].value;
  let formato_nofilter = imagen.split(".");
  let formato = formato_nofilter.pop();
  console.log(formato);
  let img_regex = /^(gif|jpe?g|tiff?|png|webp|bmp)*$/;
  if( !img_regex.test(formato)) {
    alert(`inserta una imagen válida, recibí un archivo .${formato}`);
    return false;
  }
 */



var regions = {
  15: ["Arica", "Camarones", "Putre", "General Lagos"],
  1: ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"],
  2: ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena"],
  3: ["Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"],
  4: ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paihuano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"],
  5: ["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "La Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llay-Llay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limanche", "Olmué", "Villa Alemana"],
  0: ["Santiago", "Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cissterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "Til Til", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"],
  6: ["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Renquínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chéíca", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"],
  7: ["Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "ROmeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longavi", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas0"],
  16: ["Chillán", "Bulnes", "Chillán Viejo", "El Carmen", "Pemuco", "Pinto", "Quillón", "San Ignacio", "Yungay", "Quirihue", "Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Ránquil", "Treguaco", "San Carlos", "Coihueco", "Ñiquén", "San Fabián", "San Nicolás"],
  8: ["Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de La Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Álamos", "Tirúa", "Los Ángeles", "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel", "Alto Biobío"],
  9: ["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre Las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria"],
  14: ["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Union", "Futrono", "Lago Ranco", "Río Bueno"],
  10: ["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "Frutilllar", "Los muermos", "LLanquihue", "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"],
  11: ["Coyhaique", "Lago Verde", "Aysén", "Cisnes", "Guaitecas", "Cochrane", "O'Higgins", "Tortel", "Chile Chico", "Río Ibáñez"],
  12: ["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Cabo de Hornos", "Antártica", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]
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




