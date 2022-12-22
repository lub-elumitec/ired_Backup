from odoo import api, fields, models
from odoo.addons.base.models.res_partner import _lang_get


class MyPatentEventRegistration(models.Model):
    _inherit = 'event.registration'

    firstname = fields.Char("First Name", index=True,
                            )
    lastname = fields.Char("Last Name", index=True,
                           )
    name = fields.Char(
        compute="_compute_name",
        inverse="_inverse_name_after_cleaning_whitespace",
        required=False,
        store=True,
        readonly=False,
    )
    title_id = fields.Many2one('res.partner.title', string='Title',
                               compute='_compute_title_id', store=True)
    title = fields.Char('Title')
    salutation_id = fields.Many2one('res.partner.salutation',
                                    string='Salutation', ondelete="restrict",
                                    compute='_compute_salutation_id', store=True)
    gender_id = fields.Many2one('res.partner.gender', string='Gender',
                                ondelete="restrict")
    country_id = fields.Many2one('res.country', string='Country',
                                 ondelete='restrict',
                                 compute='_compute_country_id', store=True)
    company_name = fields.Char(string='Company Name',
                               compute='_compute_company_name', store=True)
    voucher_code = fields.Char('Voucher Code')
    city = fields.Char('City', compute='_compute_city', store=True)
    street = fields.Char('Street', compute='_compute_street', store=True)
    zip = fields.Char('Zip', compute='_compute_zip', store=True)
    lang = fields.Selection(_lang_get, string='Language',
                            help="All the emails sent to this attendee will be translated in this language.")

    def _get_website_registration_allowed_fields(self):
        res = super(MyPatentEventRegistration,
                    self)._get_website_registration_allowed_fields()
        res.update(['voucher_code', 'company_name', 'country_id',
                    'salutation_id', 'title', 'firstname', 'lastname',
                    'city', 'street', 'zip', 'lang', 'gender_id'])
        return res

    @api.depends('partner_id')
    def _compute_city(self):
        for registration in self:
            if not registration.city and registration.partner_id:
                registration.city = registration._synchronize_partner_values(
                    registration.partner_id,
                    fnames=['city']
                ).get('city') or False

    @api.depends('partner_id')
    def _compute_street(self):
        for registration in self:
            if not registration.street and registration.partner_id:
                registration.street = registration._synchronize_partner_values(
                    registration.partner_id,
                    fnames=['street']
                ).get('street') or False

    @api.depends('partner_id')
    def _compute_zip(self):
        for registration in self:
            if not registration.zip and registration.partner_id:
                registration.zip = registration._synchronize_partner_values(
                    registration.partner_id,
                    fnames=['zip']
                ).get('zip') or False

    @api.depends('partner_id')
    def _compute_title_id(self):
        for registration in self:
            if not registration.title_id and registration.partner_id:
                registration.title_id = registration._synchronize_partner_values(
                    registration.partner_id,
                    fnames=['title']
                ).get('title') or False

    @api.depends('partner_id')
    def _compute_salutation_id(self):
        for registration in self:
            if not registration.salutation_id and registration.partner_id:
                registration.salutation_id = registration._synchronize_partner_values(
                    registration.partner_id,
                    fnames=['salutation_id']
                ).get('salutation_id') or False

    @api.depends('partner_id')
    def _compute_country_id(self):
        for registration in self:
            if not registration.country_id and registration.partner_id:
                registration.country_id = registration._synchronize_partner_values(
                    registration.partner_id,
                    fnames=['country_id']
                ).get('country_id') or False

    @api.depends('partner_id')
    def _compute_company_name(self):
        for registration in self:
            if not registration.company_name and registration.partner_id:
                registration.company_name = registration._synchronize_partner_values(
                    registration.partner_id,
                    fnames=['company_name']
                ).get('company_name') or False

    @api.model
    def _names_order_default(self):
        return "first_last"

    @api.model
    def _get_names_order(self):
        """Get names order configuration from system parameters.
        You can override this method to read configuration from language,
        country, company or other"""
        return (
            self.env["ir.config_parameter"]
                .sudo()
                .get_param("attendees_names_order", self._names_order_default())
        )

    @api.model
    def _get_computed_name(self, lastname, firstname):
        """Compute the 'name' field according to splitted data.
        You can override this method to change the order of lastname and
        firstname the computed name"""
        order = self._get_names_order()
        if order == "last_first_comma":
            return ", ".join(p for p in (lastname, firstname) if p)
        elif order == "first_last":
            return " ".join(p for p in (firstname, lastname) if p)
        else:
            return " ".join(p for p in (lastname, firstname) if p)

    @api.depends("firstname", "lastname")
    def _compute_name(self):
        """Write the 'name' field according to splitted data."""
        for record in self:
            record.name = record._get_computed_name(record.lastname,
                                                    record.firstname)

    def _inverse_name_after_cleaning_whitespace(self):
        """Clean whitespace in :attr:`~.name` and split it.

        The splitting logic is stored separately in :meth:`~._inverse_name`, so
        submodules can extend that method and get whitespace cleaning for free.
        """
        for record in self:
            # Remove unneeded whitespace
            clean = record._get_whitespace_cleaned_name(record.name)
            record.name = clean
            record._inverse_name()

    @api.model
    def _get_whitespace_cleaned_name(self, name, comma=False):
        """Remove redundant whitespace from :param:`name`.

        Removes leading, trailing and duplicated whitespace.
        """
        try:
            name = " ".join(name.split()) if name else name
        except UnicodeDecodeError:
            # with users coming from LDAP, name can be a str encoded as utf-8
            # this happens with ActiveDirectory for instance, and in that case
            # we get a UnicodeDecodeError during the automatic ASCII -> Unicode
            # conversion that Python does for us.
            # In that case we need to manually decode the string to get a
            # proper unicode string.
            name = " ".join(name.decode("utf-8").split()) if name else name

        if comma:
            name = name.replace(" ,", ",")
            name = name.replace(", ", ",")
        return name

    @api.model
    def _get_inverse_name(self, name):
        """Compute the inverted name.

        When this method is called, :attr:`~.name` already has unified and
        trimmed whitespace.
        """

        if not name:
            parts = [False, False]
        # Guess name splitting
        else:
            order = self._get_names_order()
            # Remove redundant spaces
            name = self._get_whitespace_cleaned_name(
                name, comma=(order == "last_first_comma")
            )
            parts = name.split("," if order == "last_first_comma" else " ", 1)
            if len(parts) > 1:
                if order == "first_last":
                    parts = [" ".join(parts[1:]), parts[0]]
                else:
                    parts = [parts[0], " ".join(parts[1:])]
            else:
                if self.firstname:
                    parts.append(parts[0])
                    parts[0] = False
                while len(parts) < 2:
                    parts.append(False)
        return {"lastname": parts[0], "firstname": parts[1]}

    def _inverse_name(self):
        """Try to revert the effect of :meth:`._compute_name`."""
        for record in self:
            parts = record._get_inverse_name(record.name)
            record.lastname = parts["lastname"]
            record.firstname = parts["firstname"]

    def _synchronize_partner_values(self, partner, fnames=None):
        if fnames is None:
            fnames = ['name', 'email', 'phone', 'mobile', 'title',
                      'salutation_id', 'country_id', 'company_name',
                      'city', 'street', 'zip']
        res = super(MyPatentEventRegistration,
                    self)._synchronize_partner_values(partner, fnames)
        return res
