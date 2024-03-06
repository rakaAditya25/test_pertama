from odoo import models, api, fields, _
import requests

class WizardsGetDataRO(models.TransientModel):
    _name = 'wz.get_data.ro'
    _description = "Get Data RAJA ONGKIR"

    name = fields.Selection([('provinsi', 'Provinsi'), ('city', 'Kota'), ('kurir', 'Kurir'), ('cost', 'Check Cost')], required=True, default='provinsi', string="Pilih Data")
    province_awal_id = fields.Many2one('city', string="From")
    province_tujuan_id = fields.Many2one('city',string="To")
    kurir = fields.Selection([('jne', 'JNE'), ('pos', 'POS'), ('tiki', 'TIKI')])
    kurir_id = fields.Many2one('jenis.kurir')
    berat = fields.Float()
    service_kurir_ids = fields.Many2many('service.kurir', string="To")

    def get_data_ro(self):
        if self.name == 'provinsi':
            url = "https://api.rajaongkir.com/starter/province"
            payload = {}
            headers = {
                'key': '8dc9e7af902189fe4210b56af68ca959'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            cek = [value for rec, value in response.json().items()]
            for rec in cek:
                if rec['results']:
                    for prov in rec['results']:
                        print(prov['province_id'], prov['province'])
                        provinsi_odoo = self.env['res.country.state'].search([('name', '=', prov['province'])])
                        if provinsi_odoo:
                            print("===TEREKSEKUSI===",prov['province_id'], prov['province'])
                            provinsi_odoo.write({
                                'prov_ro_id' : int(prov['province_id'])
                        })
        elif self.name == 'city':
            odoo_city = self.env['city']
            url = "	https://api.rajaongkir.com/starter/city"
            payload = {}
            headers = {
                'key': '8dc9e7af902189fe4210b56af68ca959'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            cek = [value for rec, value in response.json().items()]
            for rec in cek:
                if rec['results']:
                    for prov in rec['results']:
                        provinsi_odoo = self.env['res.country.state'].search([('name', '=', prov['province'])])
                        if provinsi_odoo:
                            print(provinsi_odoo, "===TEREKSEKUSI===",prov['province_id'], prov['province'])
                            odoo_city.create({
                                'name': prov['city_name'],
                                'state_id': provinsi_odoo.id,
                                'code_pos': prov['postal_code'],
                                'type_daerah': prov['type'],
                                'city_ro_id': int(prov['city_id'])
                            })

        elif self.name == 'kurir':
            jenis_kurir = self.env['jenis.kurir']
            if self.province_awal_id and self.province_tujuan_id and self.kurir and self.berat:
                url = "https://api.rajaongkir.com/starter/cost"
                payload = {
                    'origin': self.province_awal_id.city_ro_id,
                    'destination': self.province_tujuan_id.city_ro_id,
                    'weight': self.berat,
                    'courier': self.kurir
                }
                files=[]
                headers = {
                'key': '8dc9e7af902189fe4210b56af68ca959'
                }
                response = requests.request("POST", url, headers=headers, data=payload, files=files)
                cek = [value for rec, value in response.json().items()]
                for rec in cek:
                    if rec['results']:
                        for prov in rec['results']:
                            jenis_kurir.create({
                                'name': prov['name'],
                                'code': prov['code']
                            })
        else:
            if self.province_awal_id and self.province_tujuan_id and self.kurir_id and self.berat:
                url = "https://api.rajaongkir.com/starter/cost"
                payload = {
                    'origin': self.province_awal_id.city_ro_id,
                    'destination': self.province_tujuan_id.city_ro_id,
                    'weight': self.berat,
                    'courier': self.kurir_id.code
                }
                files=[]
                headers = {
                'key': '8dc9e7af902189fe4210b56af68ca959'
                }
                response = requests.request("POST", url, headers=headers, data=payload, files=files)
                cek = [value for rec, value in response.json().items()]
                jenis = self.env['jenis.kurir'].search([('id', '=', self.kurir_id.id)])
                service = self.env['service.kurir'].search([('kurir_id', '=', jenis.id)])
                for rec in cek:
                    if service:
                        service.unlink()
                    for cost in rec['results']:
                        for cos in cost['costs']:
                            for c in cos['cost']:
                                print("====", cos['service'], c['etd'], c['value'], jenis.name)
                                jenis.write({
                                    'kurir_line':[(1, self.kurir_id.kurir_line.ids[0],{
                                        'name': cos['service'],
                                        'price': float(c['value']),
                                        'estimasi': c['etd'],
                                    })]
                                    # 'kurir_line' [(0, 0, {
                                    #     'name': cos['service'],
                                    #     'price': float(c['value']),
                                    #     'estimasi': c['etd'],
                                    #     'kurir_id': jenis.id
                                    #     })]
                                })
            # return{
            #     'type': 'ir.actions.act_window',
            #     'view_mode': 'form',
            #     'res_model': 'wz.get_data.ro',
            #     'target': 'new',
            #     'res_id': self.id
            # }