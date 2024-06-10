from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/folder-file', views.FolderFileListApiView.as_view(), name='folder-file'),

    path('api/v1/canhan-hogiadinh', views.CaNhan_HoGiaDinhListListApiView.as_view(), name='canhan-hogiadinh'),
    path('api/v1/tochuc-congdongdancu', views.ToChuc_CongDongDanCuListApiView.as_view(), name='tochuc-congdongdancu'),
    path('api/v1/thua', views.ThuaListApiView.as_view(), name='thua'),
    path('api/v1/nha-canho', views.Nha_CanHoListApiView.as_view(), name='nha-canho'),
    path('api/v1/congtrinhxaydung', views.CongTrinhXayDungListApiView.as_view(), name='congtrinhxaydung'),
    path('api/v1/rung', views.RungListApiView.as_view(), name='rung'),
    path('api/v1/taisankhac', views.TaiSanKhacListApiView.as_view(), name='taisankhac'),



    path('api/v1/field-label', views.FieldLabelApiView.as_view(), name='field-label'),



]
