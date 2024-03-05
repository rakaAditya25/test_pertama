from odoo import models, fields, api, _

class Provinsi(models.Model):
    _name = 'provinsi'
    _description = "List Provinsi"

    name = fields.Char()
    city_line = fields.One2many('city', 'state_id')

class City(models.Model):
    _name = 'city'
    _description = "List city"

    state_id = fields.Many2one('res.country.state')
    name = fields.Char()
    code_pos = fields.Char()
    type_daerah = fields.Char()
    city_ro_id = fields.Integer()

class ServiceKurir(models.Model):
    _name = 'service.kurir'
    _description = "List Service Kurir"

    name = fields.Char()
    price = fields.Float()
    estimasi = fields.Char()
    kurir_id = fields.Many2one('jenis.kurir')

class JenisKurir(models.Model):
    _name = "jenis.kurir"
    _description = "Pilihan Kurir yang tersedia"
    _rec_name = 'code'

    name = fields.Char()
    code = fields.Char()
    kurir_line = fields.One2many('service.kurir', 'kurir_id')

class InheritReState(models.Model):
    _inherit = 'res.country.state'

    prov_ro_id = fields.Integer()

# class CekHargaKurir(models.Model):
#     _name = "cek.harga.kurir"
#     _description = "Cek Harga Kurir"

#     kota_asal = fields.Many2one('res.city',string="Kota Asal")
#     kota_tujuan = fields.Many2one('res.city',string="Kota Tujuan")
#     berat = fields.Float()
#     kurir = fields.Many2one('kurir', string="Jasa")


# class JenisKurirLine(models.Model):
#     _name = 'jenis.kurir.line'
#     _description = "Detail Kurir yang tersdia"

#     kurir_id = fields.Many2one('jenis.kurir')
#     service_name = fields.Char("Service")
#     harga = fields.Monetary("Harga")
#     estimasi = fields.Integer("ETD")