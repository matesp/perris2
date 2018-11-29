// Editar
function editarRescate(id,nombre,descripcion,raza,estado){
  $("#editId").val(id)
  $("#editNombre").val(nombre)
  $("#editDescripcion").val(descripcion)
  $("#editRaza").val(raza)
  $("#editEstado").val(estado)
}

// Requerimientos del formulario agregar
$(function() {
  $( "#nuevoRescate" ).validate({
    rules: {
      nombre:{
          required: true,
          minlength: 3
      },
      descripcion:{
        required: true,
        minlength: 3
      },
      raza:{
        required: true,
        minlength: 3
      },
      estado:{
        required: true
      },
      foto: {
        required: true,
        extension: "jpg|png"
      }
    },
    messages:{
      nombre:{
        required: "Ingresa tu nombre",
        minlength: "Debe tener tres caracteres mínimo"
      },
      descripcion:{
        required: "Ingresa una descripción",
        minlength: "Debe tener tres caracteres mínimo"
      },
      raza:{
        required: "Ingresa una raza",
        minlength: "Debe tener tres caracteres mínimo"
      },
      estado:{
        required: "Selecciona un estado"
      },
      foto:{
        required: "Agrega una foto",
        extension: "Debe ser una imágen JPG o PNG"
      }
    }
  });
});

// Requerimientos del formulario modificar
$(function() {
  $( "#nuevoRescate" ).validate({
    rules: {
      editNombre:{
          required: true,
          minlength: 3
      },
      editDescripcion:{
        required: true,
        minlength: 3
      },
      editRaza:{
        required: true,
        minlength: 3
      },
      editEstado:{
        required: true
      },
      editFoto: {
        required: true,
        extension: "jpg|png"
      }
    },
    messages:{
      editNombre:{
        required: "Ingresa tu nombre",
        minlength: "Debe tener tres caracteres mínimo"
      },
      editDescripcion:{
        required: "Ingresa una descripción",
        minlength: "Debe tener tres caracteres mínimo"
      },
      editRaza:{
        required: "Ingresa una raza",
        minlength: "Debe tener tres caracteres mínimo"
      },
      editEstado:{
        required: "Selecciona un estado"
      },
      editFoto:{
        required: "Agrega una foto",
        extension: "Debe ser una imágen JPG o PNG"
      }
    }
  });
});