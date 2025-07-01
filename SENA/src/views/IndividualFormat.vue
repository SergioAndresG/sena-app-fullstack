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
    margin-top: 100px;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    flex-direction: column;
}


.icon {
    height: 12rem;
    width: 12rem;
}

.title-if {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 2rem;
    margin-top: 35px;
    margin-bottom: 55px;
}

.button-if {
    width: 80%;
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white;
    font-size: 1.4rem;
    padding: 1rem;
    border-radius: 0.5rem;
    font-weight: 500;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    animation: slideUp 0.6s ease-out;
    margin: 0 auto;
    margin-top: 30px;
}

.label-if {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 1.5rem;
}

.input-if {
    width: 70%;
    /* ← antes 80% */
    padding: 1rem 1rem 1rem 3rem;
    border: 1px solid #d1d5db;
    border-radius: 0.5rem;
    font-size: 1rem;
    transition: all 0.3s ease;
    box-sizing: border-box;
    margin: 0.5rem auto;
    /* para centrar y separar */
}

.button-if:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(8, 106, 73, 0.382);
}

/* ✅ Estilos responsive para pantallas menores a 768px */
@media (max-width: 1400px) {
    .container-if {
        width: 60%;
        height: 300px;
        margin-top: 50px;
        padding: 1rem;
    }

    .icon-if {
        height: 8rem;
        width: 8rem;
    }

    .title-if {
        font-size: 1.5rem;
        text-align: center;
    }

    .button-if {
        width: 30%;
        font-size: 1.1rem;
        padding: 0.8rem;
    }
}

@media (max-width: 600px) {
    .container-if {
        width: 50%;
        height: 280px;
        margin: 0 auto;
        margin-top: 80px;
        padding: 1rem;
    }

    .icon-if {
        height: 5rem;
        width: 5rem;
    }

    .title-if {
        font-size: 1.3rem;
        text-align: center;
    }

    .button-if {
        width: 50%;
        font-size: 1.1rem;
        padding: 0.8rem;
    }
}

@media (max-width: 600px) {
    .button-if {
        font-size: 0.9rem;

    }
}
</style>