odoo.define('mypatent_cb_event_registration.event_ticket', function (require) {
    var ajax = require('web.ajax');
    var core = require('web.core');
    var EventRegistrationForm = require('website_event.website_event');
    EventRegistrationForm.include({

        on_click: function (ev) {
            ev.preventDefault();
            ev.stopPropagation();
            var $form = $(ev.currentTarget).closest('form');
            var $button = $(ev.currentTarget).closest('[type="submit"]');
            var $checkbox = $(ev.currentTarget).closest('.same_event_ticket');
            var post = {};
            $('#registration_form table').siblings('.alert').remove();
            $('#registration_form select').each(function () {
                post[$(this).attr('name')] = $(this).val();
            });
            var tickets_ordered = _.some(_.map(post, function (value, key) { return parseInt(value); }));
            if (!tickets_ordered) {
                $('<div class="alert alert-info"/>')
                    .text(_t('Please select at least one ticket.'))
                    .insertAfter('#registration_form table');
                return new Promise(function () {});
            } else {
                $button.attr('disabled', true);
                var salutation;
                var title;
                var email;
                var firstname;
                var lastname;
                var phone;
                var country;
                var city;
                var zip;
                var company;
                var voucher;
                return ajax.jsonRpc($form.attr('action'), 'call', post).then(function (modal) {
                    var $modal = $(modal);
                    $modal.on('change', '#o_ticket_form_one .form-control', function (e) {
                        var checkbox = $(".same_event_ticket input");
                        var event_ticket = $(".no-first_ticket .form-control");
                        if (checkbox[0].checked == true){
                            var attr_name = e.target.parentElement.attributes[0].nodeValue
                            if(attr_name == 'attendee_gender'){
                                salutation = e.target.value
                            }
                            if(attr_name == 'attendee_title'){
                                title = e.target.value
                            }
                            if(attr_name == 'attendee_email'){
                                email = e.target.value
                            }
                            if(attr_name == 'attendee_firstname'){
                                firstname = e.target.value
                            }
                            if(attr_name == 'attendee_lastname'){
                                lastname = e.target.value
                            }
                            if(attr_name == 'attendee_phone'){
                                phone = e.target.value
                            }
                            if(attr_name == 'attendee_country'){
                                country = e.target.value
                            }
                            if(attr_name == 'attendee_city'){
                                city = e.target.value
                            }
                            if(attr_name == 'attendee_zip'){
                                zip = e.target.value
                            }
                            if(attr_name == 'attendee_company'){
                                company = e.target.value
                            }
                            if(attr_name == 'attendee_voucher'){
                                voucher = e.target.value
                            }
                            if(attr_name == 'attendee_street'){
                                street = e.target.value
                            }

                            for(var i=0; i<event_ticket.length; i++){
                                var name_attr = event_ticket[i].parentElement.attributes[0].nodeValue
                                if(name_attr == 'attendee_gender'){
                                    event_ticket[i].value = salutation
                                }
                                if(name_attr == 'attendee_title'){
                                    event_ticket[i].value = title
                                }
                                if(name_attr == 'attendee_email'){
                                    event_ticket[i].value = email

                                }
                                if(name_attr == 'attendee_firstname'){
                                    event_ticket[i].value = firstname
                                }
                                if(name_attr == 'attendee_lastname'){
                                    event_ticket[i].value = lastname
                                }
                                if(name_attr == 'attendee_phone'){
                                    event_ticket[i].value = phone
                                }
                                if(name_attr == 'attendee_country'){
                                    event_ticket[i].value = country
                                }
                                if(name_attr == 'attendee_city'){
                                    event_ticket[i].value = city
                                }
                                if(name_attr == 'attendee_zip'){
                                    event_ticket[i].value = zip
                                }
                                if(name_attr == 'attendee_company'){
                                    event_ticket[i].value = company
                                }
                                if(name_attr == 'attendee_voucher'){
                                    event_ticket[i].value = voucher
                                }
                                if(name_attr == 'attendee_street'){
                                    event_ticket[i].value = street
                                }
                                event_ticket[i].disabled = true;
                            }
                        }
                    });
                    $modal.on('change', '.same_event_ticket', function (e) {
                        var first_ticket = $("#o_ticket_form_one .form-control");
                        var event_ticket = $(".no-first_ticket .form-control");
                        if (e.target.checked == true){
                            for(var i=0; i<first_ticket.length; i++){
                                var name_attr_first = first_ticket[i].parentElement.attributes[0].nodeValue
                                if(name_attr_first == 'attendee_gender'){
                                    salutation = first_ticket[i].value
                                }
                                if(name_attr_first == 'attendee_title'){
                                    title = first_ticket[i].value
                                }
                                if(name_attr_first == 'attendee_email'){
                                    email = first_ticket[i].value
                                }
                                if(name_attr_first == 'attendee_firstname'){
                                    firstname = first_ticket[i].value
                                }
                                if(name_attr_first == 'attendee_lastname'){
                                    lastname = first_ticket[i].value
                                }
                                if(name_attr_first == 'attendee_phone'){
                                    phone = first_ticket[i].value
                                }
                                if(name_attr_first == 'attendee_country'){
                                    country = first_ticket[i].value
                                }
                                if(name_attr_first == 'attendee_city'){
                                    city = first_ticket[i].value
                                }
                                if(name_attr_first == 'attendee_zip'){
                                    zip = first_ticket[i].value
                                }
                                if(name_attr_first == 'attendee_company'){
                                    company = first_ticket[i].value
                                }
                                if(name_attr_first == 'attendee_voucher'){
                                    voucher = first_ticket[i].value
                                }
                                if(name_attr_first == 'attendee_street'){
                                    street = first_ticket[i].value
                                }
                            }

                            for(var i=0; i<event_ticket.length; i++){
                                var name_attr = event_ticket[i].parentElement.attributes[0].nodeValue
                                if(name_attr == 'attendee_gender'){
                                    event_ticket[i].value = salutation
                                }
                                if(name_attr == 'attendee_title'){
                                    event_ticket[i].value = title
                                }
                                if(name_attr == 'attendee_email'){
                                    event_ticket[i].value = email

                                }
                                if(name_attr == 'attendee_firstname'){
                                    event_ticket[i].value = firstname
                                }
                                if(name_attr == 'attendee_lastname'){
                                    event_ticket[i].value = lastname
                                }
                                if(name_attr == 'attendee_phone'){
                                    event_ticket[i].value = phone
                                }
                                if(name_attr == 'attendee_country'){
                                    event_ticket[i].value = country
                                }
                                if(name_attr == 'attendee_city'){
                                    event_ticket[i].value = city
                                }
                                if(name_attr == 'attendee_zip'){
                                    event_ticket[i].value = zip
                                }
                                if(name_attr == 'attendee_company'){
                                    event_ticket[i].value = company
                                }
                                if(name_attr == 'attendee_voucher'){
                                    event_ticket[i].value = voucher
                                }
                                if(name_attr == 'attendee_street'){
                                    event_ticket[i].value = street
                                }
                                event_ticket[i].classList.add('select_readonly');
                                event_ticket[i].tabindex = -1
                                event_ticket[i].ariaDisabled= true
                            }
                        }
                        else{
                            console.log("remove")
                            for(var i=0; i<event_ticket.length; i++){
                                event_ticket[i].classList.remove('select_readonly');
                                event_ticket[i].tabindex = 0
                                event_ticket[i].ariaDisabled= false
                            }
                        }

                    });
                    $modal.modal({backdrop: 'static', keyboard: false});
                    $modal.find('.modal-body > div').removeClass('container'); // retrocompatibility - REMOVE ME in master / saas-19
                    $modal.appendTo('body').modal();
                    $modal.on('click', '.js_goto_event', function () {
                        $modal.modal('hide');
                        $button.prop('disabled', false);
                    });
                    $modal.on('click', '.close', function () {
                        $button.prop('disabled', false);
                    });
                });
            }
        },
    });
});
