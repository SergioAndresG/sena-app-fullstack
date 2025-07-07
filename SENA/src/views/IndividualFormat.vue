<template>
    <Header></Header>
    <section class="container-if">

        <!-- <div>
            <img class="icon-docs" src="../assets/submit.png" alt="">
        </div> -->

        <h1 class="title-if">
            Para consultar el formato por aprendiz, digite el número de la ficha y el número de documento del aprendiz
        </h1>

        <form action="">
            <div class="form-group">
                <label class="label-if">Número de ficha</label>
                <input class="input-if" type="text">
            </div>

            <div class="form-group">
                <label class="label-if">Documento de identidad</label>
                <input class="input-if" type="text">
            </div>

            <div>
                <button class="button-if">Consultar Aprendiz</button>
            </div>
        </form>

    </section>
    
</template>

<script>
import Header from '../components/Header.vue';

export default {
  components: {
    Header
  },
  data() {
    return {
      fichas: [
        {
          grupo_id: 123456,
          personas: [
            {
              tipo_documento: "CC",
              numero_documento: "1020304050",
              nombre: "Laura",
              apellidos: "Martínez Gómez",
              celular: "3104567890",
              correo_electronico: "laura.martinez@example.com",
              estado: "EN FORMACION"
            },
            {
              tipo_documento: "TI",
              numero_documento: "1122334455",
              nombre: "Juan",
              apellidos: "Pérez Rodríguez",
              celular: "3001234567",
              correo_electronico: "juan.perez@example.com",
              estado: "CANCELADO"
            }
          ]
        },
        {
          grupo_id: 654321,
          personas: [
            {
              tipo_documento: "CE",
              numero_documento: "987654321",
              nombre: "Ana",
              apellidos: "Gómez Ruiz",
              celular: "3119876543",
              correo_electronico: "ana.gomez@example.com",
              estado: "EN FORMACION"
            },
            {
              tipo_documento: "NUIP",
              numero_documento: "1234567890",
              nombre: "Carlos",
              apellidos: "Díaz Torres",
              celular: "3132223344",
              correo_electronico: "carlos.diaz@example.com",
              estado: "RETIRO VOLUNTARIO"
            }
          ]
        },
        {
          grupo_id: 789012,
          personas: [
            {
              tipo_documento: "PPT",
              numero_documento: "5678901234",
              nombre: "María",
              apellidos: "Fernández Salazar",
              celular: "3124567891",
              correo_electronico: "maria.fernandez@example.com",
              estado: "EN FORMACION"
            },
            {
              tipo_documento: "CC",
              numero_documento: "9988776655",
              nombre: "Diego",
              apellidos: "Ramírez López",
              celular: "3145678902",
              correo_electronico: "diego.ramirez@example.com",
              estado: "CANCELADO"
            }
          ]
        }
      ]
    }
  }
}
</script>

<style scoped>
.container-if {
    width: 50%;
    height: 500px;
    background-color: rgb(255, 255, 255);
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin: 0 auto;
    margin-top: 50px;
    margin-bottom: 50px;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    flex-direction: column;
}

.title-if {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 1.3rem;
    margin-top: 15px;
    margin-bottom: 35px;
    padding: 10px;
}

.form-group {
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  align-items: center; /* para centrar el contenido */
  text-align: left;
  width: 100%;
}

.label-if {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 1.1rem;
    margin-top: 10px;
}

.input-if {
    width: 100%;
    padding: 0.8rem 0.8rem 0.8rem 2.5rem;
    border: 1px solid #d1d5db;
    border-radius: 0.5rem;
    font-size: 1rem;
    transition: all 0.3s ease;
    box-sizing: border-box;
    margin: 0.5rem auto;
}

.button-if {
    width: 80%;
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white;
    font-size: 1.1rem;
    padding: 0.7rem;
    border-radius: 0.5rem;
    font-weight: 500;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    animation: slideUp 0.6s ease-out;
    margin: 0 auto;
    margin-top: 30px;
}

.button-if:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(8, 106, 73, 0.382);
}

/* ✅ Estilos responsive para pantallas menores a 768px */

@media (max-width: 768px) {

 .container-if {
        width: 60%;
        height: 480px;
        margin: 0 auto;
        margin-top: 40px;
        margin-bottom: 40px;
        padding: 1rem;
    }
  .input-if, .label-if {
    width: 80%;
  }

}

@media (max-width: 600px) {
    .container-if {
        width: 65%;
        height: 480px;
        margin: 0 auto;
        margin-top: 40px;
        margin-bottom: 40px;
        padding: 1rem;
    }

    .icon-if {
        height: 5rem;
        width: 5rem;
    }

    .title-if {
        font-size: 1.1rem;
        text-align: center;
    }

    .label-if {
        font-size: 0.9rem;
        margin-top: 10px;
    }

    .button-if {
        width: 60%;
        font-size: 0.9rem;
        padding: 0.8rem;
        margin-bottom: 15px;
    }
}


</style>