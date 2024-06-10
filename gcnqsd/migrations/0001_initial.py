# Generated by Django 4.2.11 on 2024-06-07 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaNhan_HoGiaDinh',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False, help_text='Trạng thái xoá', verbose_name='Trạng thái xoá')),
                ('deleted_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('loaiGiayTo1', models.CharField(choices=[('CMND', 'Cmnd'), ('CCCD', 'Cccd'), ('CMSQ', 'Cmsq'), ('Hộ khẩu', 'Ho Khau'), ('Hộ chiếu', 'Ho Chieu')], default='CMND', max_length=10)),
                ('ngayCap1', models.DateField(blank=True, null=True)),
                ('noiCap1', models.TextField(null=True)),
                ('hoVaTen1', models.CharField(max_length=255)),
                ('gioiTinh1', models.IntegerField(default=0)),
                ('namSinh1', models.CharField(max_length=20)),
                ('danToc1', models.CharField(max_length=20)),
                ('diaChi1', models.TextField(null=True)),
                ('quocTich11', models.CharField(max_length=50)),
                ('quocTich12', models.CharField(max_length=50)),
                ('loaiGiayTo2', models.CharField(choices=[('CMND', 'Cmnd'), ('CCCD', 'Cccd'), ('CMSQ', 'Cmsq'), ('Hộ khẩu', 'Ho Khau'), ('Hộ chiếu', 'Ho Chieu')], default='CMND', max_length=10)),
                ('ngayCap2', models.DateField(blank=True, null=True)),
                ('noiCap2', models.TextField(null=True)),
                ('hoVaTen2', models.CharField(max_length=255)),
                ('gioiTinh2', models.IntegerField(default=0)),
                ('namSinh2', models.CharField(max_length=20)),
                ('danToc2', models.CharField(max_length=20)),
                ('diaChi2', models.TextField(null=True)),
                ('quocTich21', models.CharField(max_length=50)),
                ('quocTich22', models.CharField(max_length=50)),
                ('hoGiaDinh', models.BooleanField(default=False)),
                ('hoOngBa', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_deleted_by_gcn', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CongTrinhXayDung',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False, help_text='Trạng thái xoá', verbose_name='Trạng thái xoá')),
                ('deleted_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('tenCongTrinh', models.TextField(null=True)),
                ('chuSoHuu', models.TextField(null=True)),
                ('dienTichXayDung', models.TextField(null=True)),
                ('diaChi', models.TextField(null=True)),
                ('ngayCap', models.TextField(null=True)),
                ('noiCap', models.TextField(null=True)),
                ('dacDiem', models.TextField(null=True)),
                ('thoiDiemHinhThanh', models.TextField(null=True)),
                ('hinhThanhTrongTuongLai', models.BooleanField(default=False)),
                ('nguonGoc', models.TextField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_deleted_by_gcn', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FolderFileModel',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False, help_text='Trạng thái xoá', verbose_name='Trạng thái xoá')),
                ('deleted_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('folder_name', models.CharField(blank=True, max_length=255, null=True)),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('FOLDER', 'Folder'), ('FILE', 'File')], default='FOLDER', max_length=7)),
                ('size', models.PositiveBigIntegerField(default=0)),
                ('number_file', models.IntegerField(default=0)),
                ('labeled_time_receive', models.DateTimeField(null=True)),
                ('labeled_time_complete', models.DateTimeField(null=True)),
                ('reviewed_time_receive', models.DateTimeField(null=True)),
                ('reviewed_time_complete', models.DateTimeField(null=True)),
                ('full_path_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('request_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_status', models.CharField(choices=[('UPLOADING', 'Uploading'), ('OCR', 'Ocr'), ('UPLOADED', 'Uploaded'), ('LABELING', 'Labeling'), ('LABELED', 'Labeled'), ('REVIEWING', 'Reviewing'), ('REVIEWED', 'Reviewed')], default='UPLOADING', max_length=10)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_deleted_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('labeled_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_labeled_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parent_folder', to='gcnqsd.folderfilemodel')),
                ('reviewed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_reviewed_by_gcn', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tochuc_CongDongDanCu',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False, help_text='Trạng thái xoá', verbose_name='Trạng thái xoá')),
                ('deleted_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('soGiayPhepKinhDoanh', models.CharField(max_length=255)),
                ('ngayCap', models.DateField(blank=True, null=True)),
                ('noiCap', models.TextField(null=True)),
                ('tenToChuc', models.TextField(null=True)),
                ('diaChi', models.TextField(null=True)),
                ('doiTuongSuDung', models.TextField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_deleted_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.folderfilemodel')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by_gcn', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Thua',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False, help_text='Trạng thái xoá', verbose_name='Trạng thái xoá')),
                ('deleted_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('soThuTuThua', models.TextField(null=True)),
                ('dienTichThua', models.TextField(null=True)),
                ('soHieuBanDo', models.TextField(null=True)),
                ('dienTichPhapLy', models.BooleanField(default=False)),
                ('soThuaCu', models.BooleanField(default=False)),
                ('soToCu', models.BooleanField(default=False)),
                ('suDungSoThuaSoToCu', models.BooleanField(default=False)),
                ('datDoThi', models.BooleanField(default=False)),
                ('khuDanCu', models.BooleanField(default=False)),
                ('diaChiThuaDat', models.TextField(null=True)),
                ('manhBanDoGoc', models.TextField(null=True)),
                ('nguonGocGiaoDat', models.TextField(null=True)),
                ('nguonGocKhac', models.TextField(null=True)),
                ('quaTringSuDung', models.TextField(null=True)),
                ('thoiHanSuDung', models.TextField(null=True)),
                ('dienTich', models.TextField(null=True)),
                ('nguonGocGiaoDat_mucDichSuDung', models.TextField(null=True)),
                ('nguonGocKhac_mucDichSuDung', models.TextField(null=True)),
                ('suDungChung', models.BooleanField(default=False)),
                ('datTrangChap', models.BooleanField(default=False)),
                ('mdsdTrenGCN', models.TextField(null=True)),
                ('mdsdQuyHoach', models.TextField(null=True)),
                ('mdsdKiemKe', models.TextField(null=True)),
                ('mdsdChiTiet', models.TextField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_deleted_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.folderfilemodel')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by_gcn', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaiSanKhac',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False, help_text='Trạng thái xoá', verbose_name='Trạng thái xoá')),
                ('deleted_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('tenTaiSan', models.TextField(null=True)),
                ('dienTich', models.TextField(null=True)),
                ('loaiTaiSan', models.TextField(null=True)),
                ('diaChiTaiSan', models.TextField(null=True)),
                ('mucDichSuDung', models.TextField(null=True)),
                ('chuSoHuu', models.TextField(null=True)),
                ('dacDiem', models.TextField(null=True)),
                ('thoiDiemHinhThanh', models.TextField(null=True)),
                ('hinhThanhTrongTuongLai', models.BooleanField(default=False)),
                ('nguonGoc', models.TextField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_deleted_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.folderfilemodel')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by_gcn', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rung',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False, help_text='Trạng thái xoá', verbose_name='Trạng thái xoá')),
                ('deleted_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('chuSoHuu', models.TextField(null=True)),
                ('diaChiRung', models.TextField(null=True)),
                ('diaChiCu', models.TextField(null=True)),
                ('dienTichRung', models.TextField(null=True)),
                ('loaiRung', models.TextField(null=True)),
                ('mucDichSuDung', models.TextField(null=True)),
                ('nguonGocRung', models.TextField(null=True)),
                ('thoiDiemHinhThanh', models.TextField(null=True)),
                ('hinhThanhTrongTuongLai', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_deleted_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.folderfilemodel')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by_gcn', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nha_CanHo',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False, help_text='Trạng thái xoá', verbose_name='Trạng thái xoá')),
                ('deleted_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('thuocChungCu', models.TextField(null=True)),
                ('diaChiNha', models.TextField(null=True)),
                ('loaiCongNang', models.TextField(null=True)),
                ('soTang', models.TextField(null=True)),
                ('capNha', models.TextField(null=True)),
                ('ketCau', models.TextField(null=True)),
                ('ketCauChiTiet', models.TextField(null=True)),
                ('dienTichXayDung', models.TextField(null=True)),
                ('dienTichSan', models.TextField(null=True)),
                ('dienTichSuDung', models.TextField(null=True)),
                ('dienTichSanPhu', models.TextField(null=True)),
                ('hinhThucSuDungSanRieng', models.TextField(null=True)),
                ('hinhThucSuDungSanChung', models.TextField(null=True)),
                ('namXayDung', models.TextField(null=True)),
                ('namHoanThanh', models.TextField(null=True)),
                ('thoiHanSuDung', models.TextField(null=True)),
                ('hinhThanhTrongTuongLai', models.BooleanField(default=False)),
                ('nguonGoc', models.TextField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_deleted_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.folderfilemodel')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by_gcn', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FieldModel',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False, help_text='Trạng thái xoá', verbose_name='Trạng thái xoá')),
                ('deleted_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('descriptions', models.CharField(blank=True, max_length=1000, null=True)),
                ('input_type', models.CharField(choices=[('TEXT', 'Text'), ('SELECT', 'Select'), ('DATE', 'Date'), ('BOOLEAN', 'Boolean')], default='TEXT', max_length=10)),
                ('input_value_option', models.JSONField(blank=True, null=True)),
                ('order', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('OWNER_INDIVIDUAL', 'Owner Individual'), ('OWNER_ORGANIZATION', 'Owner Organization'), ('PARCEL_OF_LAND', 'Parcel Of Land'), ('HOUSE_DEPARTMENT', 'House Department'), ('CONSTRUCTION', 'Construction'), ('FOREST', 'Forest'), ('OTHERS', 'Others')], default='OWNER_INDIVIDUAL', max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_deleted_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by_gcn', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FieldLabelModel',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False, help_text='Trạng thái xoá', verbose_name='Trạng thái xoá')),
                ('deleted_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('predicted_coordinate', models.JSONField(default=None, null=True)),
                ('predicted_time', models.DateTimeField(null=True)),
                ('predicted_value', models.TextField(blank=True, null=True)),
                ('labeled_time', models.DateTimeField(null=True)),
                ('labeled_value', models.TextField(blank=True, null=True)),
                ('labeled_verified', models.BooleanField(default=False)),
                ('reviewed_time', models.DateTimeField(null=True)),
                ('reviewed_value', models.TextField(blank=True, null=True)),
                ('reviewed_verified', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_deleted_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.fieldmodel')),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.folderfilemodel')),
                ('labeled_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_labeled_by_gcn_field', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('reviewed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_reviewed_by_gcn_field', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('modified_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False, help_text='Trạng thái xoá', verbose_name='Trạng thái xoá')),
                ('deleted_time', models.DateTimeField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('construction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.congtrinhxaydung')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_deleted_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.folderfilemodel')),
                ('forest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.rung')),
                ('house_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.nha_canho')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by_gcn', to=settings.AUTH_USER_MODEL)),
                ('others', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.taisankhac')),
                ('owner_individual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.canhan_hogiadinh')),
                ('owner_organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.tochuc_congdongdancu')),
                ('parcel_of_land', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.thua')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='congtrinhxaydung',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.folderfilemodel'),
        ),
        migrations.AddField(
            model_name='congtrinhxaydung',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by_gcn', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='canhan_hogiadinh',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gcnqsd.folderfilemodel'),
        ),
        migrations.AddField(
            model_name='canhan_hogiadinh',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by_gcn', to=settings.AUTH_USER_MODEL),
        ),
    ]
