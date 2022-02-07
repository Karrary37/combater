
    $(document).ready(function () {
    toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": false,
        "progressBar": true,
        "positionClass": "toast-bottom-center",
        "preventDuplicates": true,
        "onclick": null,
        "showDuration": "30000",
        "hideDuration": "100000",
        "timeOut": "5000",
        "extendedTimeOut": "100000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    };
    $("#contact-form").submit(function (e) {
        e.preventDefault();
        let ask_for_a_sample_email = $("#email");

        if ($(ask_for_a_sample_email).val() === "") {
            toastr.warning('Erro ! Envie novamente.');
        } else {
            $.ajax({
                url: "/enviar-contato/",
                type: "POST",
                data: $("#contact-form").serialize(),
                success: function (data) {
                    if (data === "OK") {
                        toastr.success('Sua mensagem foi enviada com sucesso!');
                        $(ask_for_a_sample_email).val('');
                    } else {
                        toastr.error('Ops! Algo deu errado ao enviar o formulário.');
                    }
                },
                error: function () {
                    toastr.error('Ops! Algo deu errado ao enviar o formulário.');
                }
            });
        }
    });

});
