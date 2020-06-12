  $(document).ready(function(){

        $(".work-class").click(function (e){
            e.preventDefault();

            var idClick = '#' + $(this).attr('id'); // id элемента по которому кликнули
            var url = $(this).attr('href'); // url передаем в ajax
            var disc = ('#disc' + $(this).attr('id')); // узнаем поле в которое будем вставлять контент
            var md = String(document.getElementById(disc.slice(1)).innerHTML) // извлекае поле в которое нужно вывести значение для проверки

            if ( md == '') {    // если в поле пусто добавляем контент
              $(idClick).ready(function(){

                $.ajax({
                    method: 'GET',
                    url: url,
                    data: '',
                    dataType: 'json',

                    success: function(data) {
                        console.log(data)

                        //$(disc).html('');
                        // alert("Successfully sent the URL to Django"),
                        // $(data)
                        for(var i = 0; i < data.elem.length; i++)
                        {
                            console.log(data.elem[i].responsibilities)
                            var row = (
                                '<br><h3> Position: ' + data.elem[i].position + '</h3><br><hr class="my-1">' +
                                '<h4> My responsibilities: </h4>' +
                                '<p>' + (data.elem[i].responsibilities).replace(/\r\n/g, '<br>') + '</p>' +
                                '<p> Started - ' + data.elem[i].started_work.slice(0,10) + '</p>' +
                                '<p> Finished - ' + data.elem[i].finished_work.slice(0,10) + '</p>');

                            $(disc).append(row);
                            // console.log(row)
                        };
                    },
                    error : function(xhr,errmsg,err) {
                        console.log('error'),
                        alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
                    }
                });
            });
            }
            else {    // удаляем контент
              $(idClick).ready(function(){
                                $(disc).html('');
                                });
              }
        });
  });
