import os
import json
import pandas as pd
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def upload_page(request):
    return render(request, 'upload.html')

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        
        # 파일 저장
        file_path = default_storage.save('test_data.xlsx', ContentFile(excel_file.read()))
        file_full_path = os.path.join(settings.MEDIA_ROOT, file_path)
        
        # 엑셀 파일 읽기
        excel_data = pd.read_excel(file_full_path)
        
        # 엑셀 데이터를 JSON 형식으로 변환
        json_data = excel_data.to_json(orient='records', force_ascii=False)
        struct_data = json.loads(json_data)
        
        # JSON 파일 경로 생성
        json_file_path = os.path.join(settings.MEDIA_ROOT, 'output.json')
        
        # JSON 파일로 저장
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(struct_data, f, ensure_ascii=False, indent=2)
        
        # 성공적인 응답 반환
        return JsonResponse({'message': 'File uploaded and converted successfully', 'json_file_path': json_file_path})
    
    return HttpResponse("Only POST method is allowed", status=405)