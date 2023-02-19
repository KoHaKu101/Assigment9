from __future__ import unicode_literals
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProfileApp', '0001_initial'),
    ]
    operations = [
        migrations.RunSQL("INSERT INTO profileapp_goodscategory VALUES " \
                          "('gc_0001', 'ปืนกลเบา', 'ปืนกลเบา')," \
                          "('gc_0002', 'ปืนกลหนัก', 'ปืนกลหนัก'), " \
                          "('gc_0003', 'ปืนสไนเปอร์','ปืนสไนเปอร์')," \
                          "('gc_0004', 'ปืนพก', 'ปืนพก'), " \
                          "('gc_0005', 'ปืนลูกซอง', 'ปืนลูกซอง');"
                          ),
        migrations.RunSQL("INSERT INTO profileapp_goods VALUES " \
                          "('g_0001','ElderFlame Operator', 'ElderFlame','ElderFlame',3150,10,'ปืนสไนเปอร์ลายมังกร','gc_0003')," \
                          "('g_0002','ElderFlame Vandal', 'ElderFlame','ElderFlame',3150,30,'ปืนกลหนักลายมังกร','gc_0002'), " \
                          "('g_0003','Prime 2.0 Phantom', 'Prime','Prime 2.0',1011.51,5,'ปืนกลเบาลายPrime','gc_0001')," \
                          "('g_0004','Phoenixs Frenzy', 'Phoenixs','Phoenix',500,10,'Phoenixs ลาย','gc_0004'), " \
                          "('g_0005','Glitchpop Bulldog', 'Glitchpop','Glitchpop Pink',2175,9,'Glitchpop ลาย สีชมพู','gc_0002');"
                          ),
    ]
