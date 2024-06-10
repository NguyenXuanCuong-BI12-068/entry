import logging
import requests
import io
import time

from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from gcnqsd.serializer import *
from core.apis import CustomListAPIView, CustomObjectAPIView
from decouple import config

logger = logging.getLogger(__name__)


class FolderFileListApiView(CustomListAPIView, CreateAPIView):
    permission_classes = [IsAuthenticated]
    model_class = FolderFileModel
    serializer_class = FolderFileSerializer

    def download_file(self, filename, request_id):
        domain = config('OCR_CORE_API_DOMAIN', default=True, cast=str)
        path = config('PATH_API_DOWNLOAD_FILE', default=True, cast=str)
        token = self.gen_token()

        url = f'''{domain}{path}{request_id}/image/{filename}'''

        payload = {}
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {token}',
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        # with open(f'''{BASE_DIR}/media/upload/{filename}''', "wb") as binary_file:
        #     binary_file.write(response.content)
        return response.content

    def call_api_upload_ocr_general(self, filename):
        file_id = self.call_api_file_upload(filename)
        response = self.call_api_ocr_general(file_id)
        return file_id, response.json()

    def call_api_ocr_general(self, file_id, cached="true"):
        domain = config('OCR_CORE_API_DOMAIN', default=True, cast=str)
        path = config('PATH_API_OCR_GENERAL', default=True, cast=str)
        token = self.gen_token()

        url = f'''{domain}{path}?file_id={file_id}&export_file=false&cached=''' + cached

        headers = {
            'Authorization': f'Bearer {token}',
        }
        response = self.retry_call_api_ocr_general(url, headers)
        return response

    def retry_call_api_ocr_general(self, url, headers, retry=0):
        if retry > 8:
            return None

        response = requests.request("POST", url, headers=headers, json={}, timeout=600)
        if response.status_code == 200:
            return response
        # chờ để retry
        time_to_sleep = 2 ** retry
        time.sleep(time_to_sleep)
        return self.retry_call_api_ocr_general(url, headers, retry=retry + 1)

    def gen_token(self):
        url = "https://ocr-core-api.tcgroup.vn/token"
        payload = 'grant_type=password&username=test&password=test&scope=&client_id=string&client_secret=string'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()['access_token']

    def call_api_file_upload(self, filename):
        domain = config('OCR_CORE_API_DOMAIN', default=True, cast=str)
        token = self.gen_token()
        headers = {
            'Authorization': f'Bearer {token}',
        }
        file = open(filename, 'rb')
        path = config('PATH_API_FILE_UPLOAD', default=True, cast=str)
        url = f'{domain}{path}'
        files = [('file', (file))]

        response = requests.request("POST", url, headers=headers,  files=files, timeout=600)
        try:
            response = response.json()
            return response['file_id']
        except Exception as e:
            print(response.text)
            raise Exception

    def post(self, request, *args, **kwargs):
        data = self.request.data.copy()

        data_type = data.get('type')
        if data_type == FOLDER_FILE_TYPE.FOLDER:
            FolderFileModel.objects.create(
                created_by_id=self.request.user.id,
                folder_name=data.get('folder_name'),
                type=data_type,
                size=0,
                number_file=0,
                process_status=PROCESS_STATUS.UPLOADED,
                parent_id=data.get('parent'),
            )
            response = {
                'status_code': 0,
                'message': "Tạo thư mục thành công"
            }
        else:

            # lưu vào bảng file
            data['created_by'] = self.request.user.id
            serializer = FolderFileSerializer(data=data)
            file_upload = None
            if serializer.is_valid():
                file_upload = serializer.save()
            else:
                logger.error(serializer.errors)

            # lưu ảnh được cắt ra
            request_id, response_api_extract = self.call_api_upload_ocr_general("/Users/hungdinhvan/Desktop/TC/data_entry_tool/src/media/" + file_upload.file.name)
            for page in response_api_extract['pages']:
                file_name = f'''{request_id}_{page["page_idx"]}.jpg'''
                file = self.download_file(file_name, request_id)
                data = {}

                file_buffer = io.BytesIO(file)
                uploaded_file = InMemoryUploadedFile(
                    file=file_buffer,
                    field_name=None,  # Tên trường FileField (nếu áp dụng)
                    name=file_name,
                    content_type=file_name.split('.')[-1],  # Định dạng file (nếu có)
                    size=len(file),
                    charset=None,
                )

                data['file'] = uploaded_file

                FolderFileModel.objects.create(
                    folder_name=file_upload.file.name,
                    file=data.get('file', None),
                    created_by_id=self.request.user.id,
                    created_time=timezone.now(),
                    size=uploaded_file.size,
                    type=FOLDER_FILE_TYPE.FILE,
                    parent=file_upload,
                    page=page["page_idx"],
                )

            response = {
                'status_code': 0,
                'message': "Tải tài liệu thành công, hệ thống sẽ tự động xử lý"
            }

        return Response(response, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = super(FolderFileListApiView, self).get_queryset()
        parent = self.request.query_params.get('parent')
        if parent:
            queryset = queryset.filter(parent_id=parent)

        return queryset


# Create your views here.

class CaNhan_HoGiaDinhListListApiView(CustomListAPIView):
    permission_classes = [IsAuthenticated]
    model_class = CaNhan_HoGiaDinh
    serializer_class = CaNhan_HoGiaDinhSerializer


class ToChuc_CongDongDanCuListApiView(CustomListAPIView):
    permission_classes = [IsAuthenticated]
    model_class = Tochuc_CongDongDanCu
    serializer_class = ToChuc_CongDongDanCuSerializer


class ThuaListApiView(CustomListAPIView):
    permission_classes = [IsAuthenticated]
    model_class = Thua
    serializer_class = ThuaSerializer


class Nha_CanHoListApiView(CustomListAPIView):
    permission_classes = [IsAuthenticated]
    model_class = Nha_CanHo
    serializer_class = Nha_CanHoSerializer


class CongTrinhXayDungListApiView(CustomListAPIView):
    permission_classes = [IsAuthenticated]
    model_class = CongTrinhXayDung
    serializer_class = CongTringXayDungSerializer


class CongTrinhXayDungObjectApiView(CustomObjectAPIView):
    permission_classes = [IsAuthenticated]
    model_class = CongTrinhXayDung
    serializer_class = CongTringXayDungSerializer


class RungListApiView(CustomListAPIView):
    permission_classes = [IsAuthenticated]
    model_class = Rung
    serializer_class = RungSerializer


class TaiSanKhacListApiView(CustomListAPIView):
    permission_classes = [IsAuthenticated]
    model_class = TaiSanKhac
    serializer_class = TaiSanKhacSerializer


class FieldLabelApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        datas = self.request.data.get('data')
        list_data_create = []
        for data in datas:
            field_label = FieldLabelModel(field_id=data['field_id'],
                                          labeled_value=data['value'],
                                          labeled_verified=True,
                                          labeled_time=timezone.now(),
                                          created_by_id=self.request.user.id)
            list_data_create.append(field_label)
        objs = FieldLabelModel.objects.bulk_create(list_data_create)

        response = {
            'status_code': 0,
            'message': f'Xác nhận thành công {len(objs)} trường nhập liệu'
        }
        return Response(response, status=status.HTTP_200_OK)



