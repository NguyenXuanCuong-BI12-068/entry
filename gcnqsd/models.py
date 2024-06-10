from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import FileExtensionValidator

# Create your models here.
class SuperBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        null=False,
        related_name="%(class)s_created_by_gcn"
    )
    modified_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="%(class)s_modified_by_gcn"

    )
    deleted = models.BooleanField(verbose_name="Trạng thái xoá", default=False, help_text="Trạng thái xoá")
    deleted_time = models.DateTimeField(null=True)
    deleted_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="%(class)s_deleted_by_gcn"
    )

    created_time = models.DateTimeField(editable=False, auto_now_add=True)
    modified_time = models.DateTimeField(auto_created=True, auto_now=True)

    class Meta:
        abstract = True


class FOLDER_FILE_TYPE(models.TextChoices):
    FOLDER = "FOLDER"
    FILE = "FILE"


class PROCESS_STATUS(models.TextChoices):
    UPLOADING = 'UPLOADING'
    OCR = 'OCR'
    UPLOADED = 'UPLOADED'
    LABELING = 'LABELING'
    LABELED = 'LABELED'
    REVIEWING = 'REVIEWING'
    REVIEWED = 'REVIEWED'


class FolderFileModel(SuperBase):
    folder_name = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to='upload/%Y/%m/%d',
                            validators=[FileExtensionValidator(['pdf', 'png', 'jpg', 'jpeg'])],
                            null=True,
                            blank=True,
                            max_length=255
                            )
    page = models.IntegerField(null=True)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='parent_folder')
    type = models.CharField(max_length=7, choices=FOLDER_FILE_TYPE.choices, default=FOLDER_FILE_TYPE.FOLDER)
    size = models.PositiveBigIntegerField(default=0)
    number_file = models.IntegerField(default=0)
    labeled_by = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, null=True,
                                   related_name="%(class)s_labeled_by_gcn")
    labeled_time_receive = models.DateTimeField(null=True)  # thời gian nhận file để nhập liệu
    labeled_time_complete = models.DateTimeField(null=True)  # thời gian nhập xong

    reviewed_by = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, null=True,
                                    related_name="%(class)s_reviewed_by_gcn")
    reviewed_time_receive = models.DateTimeField(null=True)  # thời gian nhận file để review
    reviewed_time_complete = models.DateTimeField(null=True)  # thời gian review xong

    full_path_id = models.CharField(max_length=1000, null=True, blank=True)
    request_id = models.CharField(max_length=1000, null=True, blank=True)
    process_status = models.CharField(max_length=10, choices=PROCESS_STATUS.choices, default=PROCESS_STATUS.UPLOADING)


@receiver(post_save, sender=FolderFileModel)
def set_full_path_id(sender, instance, **kwargs):
    if instance.full_path_id is None:
        parent = FolderFileModel.objects.get(id=instance.parent_id)
        if parent.full_path_id:
            path = f'{parent.full_path_id}/{instance.id}'
        else:
            path = f'{parent.id}/{instance.id}'
        instance.full_path_id = path
        instance.save()


class INPUT_TYPE(models.TextChoices):
    TEXT = 'TEXT'
    SELECT = 'SELECT'
    DATE = 'DATE'
    BOOLEAN = 'BOOLEAN'


class CATEGORY(models.TextChoices):
    OWNER_INDIVIDUAL = 'OWNER_INDIVIDUAL'
    OWNER_ORGANIZATION = 'OWNER_ORGANIZATION'
    PARCEL_OF_LAND = 'PARCEL_OF_LAND'
    HOUSE_DEPARTMENT = 'HOUSE_DEPARTMENT'
    CONSTRUCTION = 'CONSTRUCTION'
    FOREST = 'FOREST'
    OTHERS = 'OTHERS'


class FieldModel(SuperBase):
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    descriptions = models.CharField(max_length=1000, null=True, blank=True)
    input_type = models.CharField(max_length=10, choices=INPUT_TYPE.choices, default=INPUT_TYPE.TEXT)
    input_value_option = models.JSONField(null=True, blank=True)  # các giá trị option khi trường là select
    order = models.IntegerField(default=0)
    category = models.CharField(max_length=100, choices=CATEGORY.choices, default=CATEGORY.OWNER_INDIVIDUAL)


class FieldLabelModel(SuperBase):
    field = models.ForeignKey(FieldModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    file = models.ForeignKey(FolderFileModel, on_delete=models.DO_NOTHING, null=False)

    predicted_coordinate = models.JSONField(default=None, null=True, blank=False)
    predicted_time = models.DateTimeField(null=True)
    predicted_value = models.TextField(null=True, blank=True)

    labeled_by = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, null=True, related_name="%(class)s_labeled_by_gcn_field")
    labeled_time = models.DateTimeField(null=True)
    labeled_value = models.TextField(null=True, blank=True)
    labeled_verified = models.BooleanField(default=False)

    reviewed_by = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, null=True, related_name="%(class)s_reviewed_by_gcn_field")
    reviewed_time = models.DateTimeField(null=True)
    reviewed_value = models.TextField(null=True, blank=True)
    reviewed_verified = models.BooleanField(default=False)


class LOAIGIAYTO(models.TextChoices):
    CMND = 'CMND'
    CCCD = 'CCCD'
    CMSQ = 'CMSQ'
    HO_KHAU = 'Hộ khẩu'
    HO_CHIEU = 'Hộ chiếu'


class CaNhan_HoGiaDinh(SuperBase):
    file = models.ForeignKey(FolderFileModel, on_delete=models.DO_NOTHING, null=True, blank=True)

    # thông tin chủ sử dụng
    loaiGiayTo1 = models.CharField(max_length=10, choices=LOAIGIAYTO.choices, default=LOAIGIAYTO.CMND)
    ngayCap1 = models.DateField(null=True, blank=True)
    noiCap1 = models.TextField(null=True)
    hoVaTen1 = models.CharField(max_length=255)
    gioiTinh1 = models.IntegerField(default=0)  # 0 - nam , 1 - nu
    namSinh1 = models.CharField(max_length=20)
    danToc1 = models.CharField(max_length=20)
    diaChi1 = models.TextField(null=True)
    quocTich11 = models.CharField(max_length=50)
    quocTich12 = models.CharField(max_length=50)

    # thông tin vợ/chồng
    loaiGiayTo2 = models.CharField(max_length=10, choices=LOAIGIAYTO.choices, default=LOAIGIAYTO.CMND)
    ngayCap2 = models.DateField(null=True, blank=True)
    noiCap2 = models.TextField(null=True)
    hoVaTen2 = models.CharField(max_length=255)
    gioiTinh2 = models.IntegerField(default=0)  # 0 - nam , 1 - nu
    namSinh2 = models.CharField(max_length=20)
    danToc2 = models.CharField(max_length=20)
    diaChi2 = models.TextField(null=True)
    quocTich21 = models.CharField(max_length=50)
    quocTich22 = models.CharField(max_length=50)

    hoGiaDinh = models.BooleanField(default=False)
    hoOngBa = models.BooleanField(default=False)


class Tochuc_CongDongDanCu(SuperBase):
    file = models.ForeignKey(FolderFileModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    soGiayPhepKinhDoanh = models.CharField(max_length=255)
    ngayCap = models.DateField(null=True, blank=True)
    noiCap = models.TextField(null=True)
    tenToChuc = models.TextField(null=True)
    diaChi = models.TextField(null=True)
    doiTuongSuDung = models.TextField(null=True)


class Thua(SuperBase):
    file = models.ForeignKey(FolderFileModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    soThuTuThua = models.TextField(null=True)
    dienTichThua = models.TextField(null=True)
    soHieuBanDo = models.TextField(null=True)
    dienTichPhapLy = models.BooleanField(default=False)
    soThuaCu = models.BooleanField(default=False)
    soToCu = models.BooleanField(default=False)
    suDungSoThuaSoToCu = models.BooleanField(default=False)
    datDoThi = models.BooleanField(default=False)
    khuDanCu = models.BooleanField(default=False)
    diaChiThuaDat = models.TextField(null=True)
    manhBanDoGoc = models.TextField(null=True)
    nguonGocGiaoDat = models.TextField(null=True)
    nguonGocKhac = models.TextField(null=True)
    quaTringSuDung = models.TextField(null=True)
    thoiHanSuDung = models.TextField(null=True)
    dienTich = models.TextField(null=True)
    nguonGocGiaoDat_mucDichSuDung = models.TextField(null=True)
    nguonGocKhac_mucDichSuDung = models.TextField(null=True)
    suDungChung = models.BooleanField(default=False)
    datTrangChap = models.BooleanField(default=False)
    mdsdTrenGCN = models.TextField(null=True)
    mdsdQuyHoach = models.TextField(null=True)
    mdsdKiemKe = models.TextField(null=True)
    mdsdChiTiet = models.TextField(null=True)


class Nha_CanHo(SuperBase):
    file = models.ForeignKey(FolderFileModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    thuocChungCu = models.TextField(null=True)
    diaChiNha = models.TextField(null=True)
    loaiCongNang = models.TextField(null=True)
    soTang = models.TextField(null=True)
    capNha = models.TextField(null=True)
    ketCau = models.TextField(null=True)
    ketCauChiTiet = models.TextField(null=True)
    dienTichXayDung = models.TextField(null=True)
    dienTichSan = models.TextField(null=True)
    dienTichSuDung = models.TextField(null=True)
    dienTichSanPhu = models.TextField(null=True)
    hinhThucSuDungSanRieng = models.TextField(null=True)
    hinhThucSuDungSanChung = models.TextField(null=True)
    namXayDung = models.TextField(null=True)
    namHoanThanh = models.TextField(null=True)
    thoiHanSuDung = models.TextField(null=True)
    hinhThanhTrongTuongLai = models.BooleanField(default=False)
    nguonGoc = models.TextField(null=True)


class CongTrinhXayDung(SuperBase):
    file = models.ForeignKey(FolderFileModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    tenCongTrinh = models.TextField(null=True)
    chuSoHuu = models.TextField(null=True)
    dienTichXayDung = models.TextField(null=True)
    diaChi = models.TextField(null=True)
    ngayCap = models.TextField(null=True)
    noiCap = models.TextField(null=True)
    dacDiem = models.TextField(null=True)
    thoiDiemHinhThanh = models.TextField(null=True)
    hinhThanhTrongTuongLai = models.BooleanField(default=False)
    nguonGoc = models.TextField(null=True)


class Rung(SuperBase):
    file = models.ForeignKey(FolderFileModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    chuSoHuu = models.TextField(null=True)
    diaChiRung = models.TextField(null=True)
    diaChiCu = models.TextField(null=True)
    dienTichRung = models.TextField(null=True)
    loaiRung = models.TextField(null=True)
    mucDichSuDung = models.TextField(null=True)
    nguonGocRung = models.TextField(null=True)
    thoiDiemHinhThanh = models.TextField(null=True)
    hinhThanhTrongTuongLai = models.BooleanField(default=False)


class TaiSanKhac(SuperBase):
    file = models.ForeignKey(FolderFileModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    tenTaiSan = models.TextField(null=True)
    dienTich = models.TextField(null=True)
    loaiTaiSan = models.TextField(null=True)
    diaChiTaiSan = models.TextField(null=True)
    mucDichSuDung = models.TextField(null=True)
    chuSoHuu = models.TextField(null=True)
    dacDiem = models.TextField(null=True)
    thoiDiemHinhThanh = models.TextField(null=True)
    hinhThanhTrongTuongLai = models.BooleanField(default=False)
    nguonGoc = models.TextField(null=True)


class Document(SuperBase):
    file = models.ForeignKey(FolderFileModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    owner_individual = models.ForeignKey(CaNhan_HoGiaDinh, on_delete=models.DO_NOTHING, null=True, blank=True)
    owner_organization = models.ForeignKey(Tochuc_CongDongDanCu, on_delete=models.DO_NOTHING, null=True, blank=True)
    parcel_of_land = models.ForeignKey(Thua, on_delete=models.DO_NOTHING, null=True, blank=True)
    house_department = models.ForeignKey(Nha_CanHo, on_delete=models.DO_NOTHING, null=True, blank=True)
    construction = models.ForeignKey(CongTrinhXayDung, on_delete=models.DO_NOTHING, null=True, blank=True)
    forest = models.ForeignKey(Rung, on_delete=models.DO_NOTHING, null=True, blank=True)
    others = models.ForeignKey(TaiSanKhac, on_delete=models.DO_NOTHING, null=True, blank=True)
