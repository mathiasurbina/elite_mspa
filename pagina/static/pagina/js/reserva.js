$(document).ready(function () {
    $('#fecha').change(function () {
        const fechaSeleccionada = $(this).val();
        if (fechaSeleccionada) {
            $.ajax({
                url: '',
                type: 'GET',
                data: {
                    'fecha': fechaSeleccionada
                },
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                },
                success: function (response) {
                    const horasContainer = $('#horas-disponibles');
                    horasContainer.empty();

                    if (response.horas.length > 0) {
                        $('#horas-container').show();
                        $('#datos-cliente').hide();
                        response.horas.forEach(function (hora) {
                            const btn = $(`<button type="button" class="btn btn-outline-primary m-1">${hora}</button>`);
                            btn.click(function () {
                                $('#hora-elegida').val(hora);
                                $('#datos-cliente').show();
                                $('#horas-container button').removeClass('active');
                                $(this).addClass('active');
                            });
                            horasContainer.append(btn);
                        });
                    } else {
                        $('#horas-container').show();
                        horasContainer.html('<p class="text-danger">No hay horas disponibles para esta fecha.</p>');
                        $('#datos-cliente').hide();
                    }
                }
            });
        }
    });
});
