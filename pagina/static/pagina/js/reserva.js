$(document).ready(function () {
    $("#fecha").on("change", function () {
        const fecha = $(this).val();
        if (!fecha) return;

        $.ajax({
            url: "/reserva/",
            type: "GET",
            data: { fecha: fecha },
            headers: { 'X-Requested-With': 'XMLHttpRequest' },  
            success: function (response) {
                const horas = response.horas;
                const $container = $("#horas-disponibles");
                $container.empty();

                if (horas.length > 0) {
                    horas.forEach(hora => {
                        $container.append(
                            `<button type="button" class="btn btn-outline-primary m-1 hora-btn">${hora}</button>`
                        );
                    });
                    $("#horas-container").show();
                    $("#datos-cliente").hide();
                } else {
                    $container.append("<p>No hay horas disponibles.</p>");
                    $("#horas-container").show();
                    $("#datos-cliente").hide();
                }
            },
            error: function () {
                alert("Error al obtener horas disponibles.");
            }
        });
    });

    $(document).on("click", ".hora-btn", function () {
        $(".hora-btn").removeClass("active");
        $(this).addClass("active");
        $("#hora-elegida").val($(this).text());
        $("#datos-cliente").slideDown();
    });
});
